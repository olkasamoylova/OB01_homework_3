class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {} #так как нам нужно хранить пару "ключ - значение": "товар - цена

    def add_items(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен в магазин {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} был удален из магазина {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на {item_name} обновллена в магазине {self.name}")
        else:
            print(f"Товар {item_name} не найден")


store1 = Store("Пятерочка", "Петровка 38")
store2 = Store("Азбука вкуса", "Серебрякова 12")
store3 = Store("ВкусВилл", "Ахматовой 6")

store1.add_items("Хлеб", 85)
store1.add_items("Яблоки", 105)
store1.add_items("Вино белое", 670)

store1.remove_item("Хлеб")

print(store1.get_price("Яблоки"))

store1.update_price("Вино белое", 800)



