from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./clinic_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase): pass


class Tags(Base):
    """ Класс для хранения информации о тэгах четвероногих """
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, name="tagid")
    name = Column(String)


class Category(Base):
    """ Класс для хранения информации о категории питомцев """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, name="categoryid")
    name = Column(String)


class Pet(Base):
    """ Класс для хранения и обновления информации для четвероногих питомцев """
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, name="petid")
    name = Column(String)
    photourls = Column(String)
    status = Column(String)
    categoryid = Column(Integer)
    #category = relationship("Category", back_populates="pets")
    tagid = Column(Integer)
    #tag = relationship("Tags", back_populates="pets")


SessionLocal = sessionmaker(autoflush=False, bind=engine)

#Base.metadata.create_all(bind=engine)
