import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Session
from datetime import date

Base = declarative_base()


class Pizza(Base):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image = Column(String, nullable=False)

    # Связь с таблицей PriceHistory
    price_history = relationship('PriceHistory', back_populates='pizza', cascade='all, delete-orphan')


class PriceHistory(Base):
    __tablename__ = 'price_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)
    price = Column(Integer, nullable=False)
    date = Column(Date, default=date.today)
    time = Column(String, default='00:00:00')

    # Связь с таблицей Pizza
    pizza = relationship('Pizza', back_populates='price_history')


def get_engine() -> create_engine:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'base_main.db')
    engine = create_engine(f'sqlite:///{db_path}')
    return engine


def create_tables() -> Base.metadata:
    engine = get_engine()
    Base.metadata.create_all(engine)


def get_session() -> Session:
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    get_session()
