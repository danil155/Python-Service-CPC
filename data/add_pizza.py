from data.db_session import get_session, Pizza, PriceHistory
from datetime import date, datetime


def add_pizza(name: str,
              description: str = None,
              image_path: str = 'https://clck.ru/3EzRmJ') -> None:
    session = get_session()

    availability_pizza = session.query(Pizza).filter_by(name=name).first()
    if availability_pizza:
        if not availability_pizza.image:
            availability_pizza.image = image_path
            session.commit()
            print(f'LOG in data.add_pizza: for pizza {name} src has been added.')
        else:
            print(f'WARNING in data.add_pizza: pizza {name} already in the database.')
        session.close()
        return

    new_pizza = Pizza(name=name, description=description, image=image_path)
    session.add(new_pizza)
    session.commit()
    print(f'LOG in data.add_pizza: pizza {name} successfully added in database.')
    session.close()


def add_price_history(pizza_id: int,
                      price: int,
                      date_value: date = date.today(),
                      time_value: str = str(datetime.now().time())[:8]) -> None:
    session = get_session()

    price_record = PriceHistory(pizza_id=pizza_id, price=price, date=date_value, time=time_value)
    session.add(price_record)
    session.commit()

    print(f'LOG in data.add_pizza: price {price} for Pizza ID {pizza_id} added on {date_value}.')
    session.close()


if __name__ == '__main__':
    pass
