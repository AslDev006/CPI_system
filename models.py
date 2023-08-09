from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class DirectorModel(Base):
    __tablename__ = 'director'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    Active_time = Column(Integer)
    Create_time = Column(Integer)
    boss_id = Column(Integer, ForeignKey('boss.id'))
    pre_director_id = Column(Integer, ForeignKey("pre_director.id"))
    workers_id = Column(Integer, ForeignKey('workers.id'))

    boss = relationship("BossModel", back_populates="director")
    pre_director = relationship("Pre_DirectorModel", back_populates="director")
    workers = relationship("WorkersModel", back_populates="director")


class BossModel(Base):
    __tablename__ = 'boss'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    Active_time = Column(Integer)
    Create_time = Column(Integer)
    workers_id = Column(Integer, ForeignKey('workers.id'))

    director = relationship("DirectorModel", back_populates="boss")
    workers = relationship("WorkersModel", back_populates="boss")


class Pre_DirectorModel(Base):
    __tablename__ = 'pre_director'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    Active_time = Column(Integer)
    workers_id = Column(Integer, ForeignKey('workers.id'))

    director = relationship("DirectorModel", back_populates="pre_director")
    workers = relationship("WorkersModel", back_populates="pre_director")


class WorksModel(Base):
    __tablename__ = 'works'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    join_data = Column(Integer)
    complete_data = Column(Integer)
    status = Column(String)
    price = Column(Integer)
    employer = Column(Integer)
    worker = Column(Integer)


class WorkersModel(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    Active_time = Column(Integer)
    Create_time = Column(Integer)  

    director = relationship("DirectorModel", back_populates="workers")
    boss = relationship("BossModel", back_populates="workers")
    pre_director = relationship("Pre_DirectorModel", back_populates="workers")


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
