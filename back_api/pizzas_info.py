import datetime

from data.query_pizza import get_all_pizzas, get_id_by_name, get_pizza_image
from data.query_pizza import get_pizza_prices, get_dates_for_pizza, get_times_for_pizza


def get_main_page_info():
    pizzas = get_all_pizzas()

    info = []
    for pizza in pizzas:
        pizza_id = get_id_by_name(pizza)

        image_path = get_pizza_image(pizza_id)

        price_history = get_pizza_prices(pizza_id)
        dates_temp = get_dates_for_pizza(pizza_id)
        times_temp = get_times_for_pizza(pizza_id)

        dates_current = list()
        for date, time in zip(dates_temp, times_temp):
            if date != datetime.date.today():
                dates_current.append(date.strftime('%d.%m.%Y'))
            else:
                dates_current.append(time)

        info.append({
            'name': pizza,
            'image': image_path,
            'priceHistory': {
                "dates": dates_current,
                "prices": price_history
            }
        })

    return info


if __name__ == '__main__':
    print(get_main_page_info())
