from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import SessionLocal
from .models import Pet, Category, Tags
from .schemas import PetGet, CategoryGet, TagGet

app = FastAPI()


def get_session():
    with SessionLocal() as session:
        return session


@app.get("/", response_model=str)
def root():
    """Возвращает строку с приветствием клиники для питомцев"""
    return 'Добро пожаловать в нашу ветеринарную клинику!'


@app.get("/pets/all", response_model=List[PetGet])
def get_all_pets(limit: int = 10, db: Session = Depends(get_session)):
    """Функция, которая возвращает список всех питомцев из клиники"""

    return db.query(Pet).limit(limit).all()


@app.get("/category/all", response_model=List[CategoryGet])
def get_all_categories(limit: int = 1, db: Session = Depends(get_session)):
    """Функция, которая возвращает список всех категорий питомцев из клиники"""

    return db.query(Category).limit(limit).all()


@app.get("/tags/all", response_model=List[TagGet])
def get_all_tags(limit: int = 10, db: Session = Depends(get_session)):
    """Функция, которая возвращает список всех тэгов питомцев из клиники"""

    return db.query(Tags).limit(limit).all()
