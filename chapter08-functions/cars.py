from operator import mod


def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    print(car_info)

if __name__ == "__main__":
    make_car('subaru', 'outback')
    make_car('subaru', 'outback', color='blue', tow_package=True)