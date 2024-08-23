from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base, SessionLocal


class Pet(Base):
    """ Класс для хранения и обновления информации для четвероногих питомцев """
    __tablename__ = "pets"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name="petid")
    name = Column(String)
    photourls = Column(String)
    status = Column(String)
    category = Column(Integer)
    tag = Column(Integer)

    #category_id = Column(Integer, ForeignKey("public.categories.categoryid"), name="categoryid")
    #category = relationship("Category", remote_side=[id])
    #tag_id = Column(Integer, ForeignKey("public.tags.tagid"), name="tagid")
    #tag = relationship("Tags", remote_side=[id])


class Category(Base):
    """ Класс для хранения информации о категории питомцев """
    __tablename__ = "categories"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name="categoryid")
    name = Column(String)


class Tags(Base):
    """ Класс для хранения информации о тэгах четвероногих """
    __tablename__ = "tags"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name="tagid")
    name = Column(String)


if __name__ == "__main__":
    session = SessionLocal()
    results = (session.query(Pet).all())

    for result in results:
        print(f'''
                 name = {result.name}
                 status = {result.status}
                 photourl = {result.photourls}
                 category = {result.category}
                 tag = {result.tag}
                 '''
            )







