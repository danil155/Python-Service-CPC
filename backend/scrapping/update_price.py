from apscheduler.schedulers.blocking import BlockingScheduler

from scrapping.add_data import get_data, add_pizza_in_db, add_pizza_price_in_db


def update_pizza_price():
    get_data()
    add_pizza_price_in_db()
    print('Цены успешно добавлены!')


scheduler = BlockingScheduler()

scheduler.add_job(update_pizza_price, 'interval', minutes=30)

if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
