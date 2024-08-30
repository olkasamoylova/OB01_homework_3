class Task():
    def __init__(self):
        self.tasks = [] # создаем класс и заготовку под добавление списка задач (список - скобки квадратные)

    def add_task(self, deadline, description): # функция для добавления списка задач с атрибутами дедлайна, описания и статуса (по умолчанию - не выполнено)
        self.tasks.append({'deadline' : deadline, 'description' : description, 'status' : "not completed"}) # словарь пар "ключ-значение"

    def complete_task(self, description): #важный параметр для нас - это описание
        for task in self.tasks: #перебираем список наших задач циклом
            if task['description'] == description: #если описание нашей задачи совпадает с выполнено, то меняем статус
                task['status'] = "complete"
                print(f"Задача {task['description']} выполнена")
            #else:
                #print(f"Задача {task['description']} не найдена")

    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task['status'] == "not completed":
                print(f"{task['description']} - {task['deadline']}")


t = Task()
t.add_task("01-06-2025", "Прочитать книгу")
t.add_task("01-07-2025", "Пробежать марафон")
t.add_task("01-08-2025", "Погладить кота")
t.add_task("01-09-2025", "Полить цветок")
t.add_task("01-10-2025", "Починить машину")

t.show_tasks()

t.complete_task("Прочитать книгу")

t.show_tasks()
