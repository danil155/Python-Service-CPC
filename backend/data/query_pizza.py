from data.db_session import get_session, Pizza, PriceHistory


def get_all_pizzas() -> list:
    session = get_session()
    pizzas_object = session.query(Pizza).all()
    session.close()
    pizzas = [pizza.name for pizza in pizzas_object]

    return pizzas


def get_pizza_by_id(pizza_id: int) -> object:
    session = get_session()
    pizza = session.query(Pizza).filter_by(id=pizza_id).first()
    session.close()

    if not pizza:
        return None
    return pizza.name


def get_id_by_name(name: str) -> int:
    session = get_session()
    pizza = session.query(Pizza).filter_by(name=name).first()
    session.close()

    if not pizza:
        return -1
    return pizza.id


def get_pizza_image(pizza_id: int) -> str:
    session = get_session()
    image_path = session.query(Pizza.image).filter_by(id=pizza_id).first()
    session.close()

    if not image_path:
        return ''
    return image_path[0]


def get_pizza_prices(pizza_id: int) -> list:
    session = get_session()
    prices = session.query(PriceHistory.price).filter_by(pizza_id=pizza_id).all()
    session.close()

    return [price[0] for price in prices[:10]]


def get_dates_for_pizza(pizza_id: int) -> list:
    session = get_session()
    dates = session.query(PriceHistory.date).filter_by(pizza_id=pizza_id).all()
    session.close()

    return [date[0] for date in dates[:10]]


def get_times_for_pizza(pizza_id: int) -> list:
    session = get_session()
    times = session.query(PriceHistory.time).filter_by(pizza_id=pizza_id).all()
    session.close()

    return [time[0] for time in times[:10]]


if __name__ == '__main__':
    print(get_pizza_by_id(45))
    print(get_pizza_image(45))
