from typing import List

from sqlitedb import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse
from schemas import PetGet, CategoryGet, TagGet

SQLALCHEMY_DATABASE_URL = "sqlite:///./clinic_app.db"

#работаем в SQLite, потому что postgres хороша для продакшена, потому что там фракфурт, потому ...
# и вообще привет джанго!

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

app = FastAPI()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()


# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=str)
def root():
    """Возвращает строку с приветствием клиники для питомцев"""
    return 'Добро пожаловать в нашу ветеринарную клинику!'


@app.get("/api/pets", response_model=List[PetGet])
def get_pets(db: Session = Depends(get_db)):
    """Функция, которая возвращает список питомцев из клиники"""
    return db.query(Pet).all()


@app.get("/api/pets/{id}", summary="Получить питомца по id" )
def get_pet(id, db: Session = Depends(get_db)):
    """Функция, которая возвращает питомца из клиникиby по id"""

    # получаем питомцa по id
    pet = db.query(Pet).filter(Pet.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if pet is None:
        return JSONResponse(status_code=404, content={"message": "Питомец не найден!"})

    return pet


@app.post("/api/pets", summary="Cоздать питомца")
def create_pet(data=Body(), db: Session = Depends(get_db)):
    """Функция, которая создает питомца из клиники и помещает запись в базу данных"""

    pet = Pet(name=data["name"], photourls=data["photourls"], status=data["status"], categoryid=data["categoryid"],
              tagid=data["tagid"])
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet


@app.put("/api/pets", summary="Изменить питомца")
def edit_pet(data=Body(), db: Session = Depends(get_db)):
    """Функция, которая позволяет обновление записи о питомце из клиники и помещает запись в базу данных"""

    pet = db.query(Pet).filter(Pet.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if pet is None:
        return JSONResponse(status_code=404, content={"message": "Питомец не найден!"})
    # если  найден, изменяем его данные и отправляем обратно

    pet.name = data["name"]
    pet.photourls = data["photourls"]
    pet.status = data["status"]
    pet.categoryid = data["categoryid"]
    pet.tagid = data["tagid"]
    db.commit()  # сохраняем изменения
    db.refresh(pet)
    return pet


@app.delete("/api/pets/{id}", summary="Удалить питомца")
def delete_pet(id, db: Session = Depends(get_db)):
    """Функция, которая удаляет запись о питомце из клиники """

    pet = db.query(Pet).filter(Pet.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if pet is None:
        return JSONResponse(status_code=404, content={"message": "Питомец не найден!"})

    # если найден, удаляем его
    db.delete(pet)  # удаляем объект
    db.commit()  # сохраняем изменения
    return pet


@app.get("/api/categories", response_model=List[CategoryGet])
def get_pets(db: Session = Depends(get_db)):
    """Функция, которая возвращает список  категорий питомцев из клиники"""
    return db.query(Category).all()


@app.get("/api/tags", response_model=List[TagGet])
def get_pets(db: Session = Depends(get_db)):
    """Функция, которая возвращает список  тэгов питомцев из клиники"""
    return db.query(Tags).all()
