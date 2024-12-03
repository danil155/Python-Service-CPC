from requesting_data import get_info_pizza
from data.add_pizza import add_pizza, add_price_history
from data.query_pizza import get_id_by_name


data = list()


def get_data() -> None:
    global data
    data = get_info_pizza()


def add_pizza_in_db() -> None:
    global data
    if not data:
        print('ERROR in scrapping.add_data: data is empty.')

    for item in data:
        add_pizza(item.name, image_path=item.image)


def add_pizza_price_in_db() -> None:
    global data
    if not data:
        print('ERROR in scrapping.add_data: data is empty.')

    for item in data:
        pizza_id = get_id_by_name(item.name)
        if pizza_id != -1:
            add_price_history(pizza_id, item.price)
        else:
            print(f'WARNING in scrapping.add_data: pizza {item.name} not found in database')


if __name__ == '__main__':
    get_data()
    add_pizza_in_db()
