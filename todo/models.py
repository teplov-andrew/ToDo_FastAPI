from todo.database.base import Base, engine
from sqlalchemy import Column, String, Integer, Boolean


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)
    is_in_progress = Column(Boolean, default=False)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
