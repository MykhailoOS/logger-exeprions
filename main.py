import logging

# Task 1
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class Specific_Error(Exception):
    def __str__(self):
        return "Can't be 0 or less then 0!"


class Logger:

    def create_log(self, log_message, level=logging.DEBUG):
        log = logging.log(level, log_message)


class Dish(Logger):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        self.create_log("send name and price")
        try:
            if self.price > 0:
                return f'{self.name}: {self.price}'
        except Specific_Error as error:
            print(error)


class MenuCategories(Logger):
    def __init__(self):
        self.menu = {}

    def add_category(self, name):
        try:
            if name not in self.menu:
                self.menu[name] = set()
        except Exception:
            print("Error1")

    def add_dish(self, category, dish):
        try:
            if category in self.menu:
                self.create_log("Check if category in menu")
                self.menu[category].add(dish)
        except Exception:
            print("Error2")

    def __str__(self):
        s = ''
        for category, dishes in self.menu.items():
            s += f'\n{category}:\n' + '\n'.join(map(str, dishes))
            self.create_log("returned list of items")
        return s


dish_1 = Dish('Salad 1', 'Super dish', 0)
dish_2 = Dish('Salad 2', 'Super dish', 101)
dish_3 = Dish('Salad 3', 'Super dish', 102)
dish_4 = Dish('Salad 4', 'Super dish', 103)

print(dish_1)
print(dish_2)
print(dish_3)
print(dish_4)

menu = MenuCategories()
menu.add_category('Сніданки')
menu.add_category('Перші страви')
menu.add_dish('Сніданки', dish_1)
menu.add_dish('Сніданки', dish_2)

menu.add_dish('Перші страви', dish_3)
menu.add_dish('Перші страви', dish_4)

print(menu)

# Task2
# import logging
#
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
#
# class Logs:
#     def __int__(self, *args, **kwargs):
#         super().__int__(*args, **kwargs)
#
#     def send_logs(self, information, level=logging.INFO):
#         logging.log(level, information)
#
#
# class Discount:
#     def __init__(self, get_sale):
#         self.get_sale = get_sale
#
#     def discount(self):
#         self.get_sale = 0.10
#
#
# class RegularDiscount(Discount, Logs):
#
#     def __init__(self, get_sale):
#         super().__init__(get_sale)
#
#     def discount(self):
#         self.get_sale = 0.20
#         self.send_logs("Using regular discount")
#
#
# class SilverDiscount(Discount, Logs):
#     def __init__(self, get_sale):
#         super().__init__(get_sale)
#
#     def discount(self):
#         self.get_sale = 0.50
#         self.send_logs("Using silver discount")
#
#
# class GoldDiscount(Discount, Logs):
#
#     def __init__(self, get_sale):
#         super().__init__(get_sale)
#
#     def discount(self):
#         self.get_sale = 0.80
#         self.send_logs("Using gold discount")
#
#
# class Client(Logs):
#     def __init__(self, price, name):
#         self.price = price
#         self.name = name
#
#         self.discount = None
#
#     def get_total_price(self, order: Discount):
#         try:
#             self.send_logs("get price with add sale card")
#             self.discount = self.price * order.get_sale
#         except Exception as error:
#             print(f"Error: {error} ")
#
#     def __str__(self):
#         return f"Користувач {self.name};\nсума з урахуванням знижки - {self.discount}"
#
#
# sale = SilverDiscount(0.20)
# res = Client(3500, "Vitya")
# res.get_total_price(sale)
# print(res)
