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
            else:
                print(f"Задача {task['description']} не найдена")

    def show_tasks(self):
        print("Текущие задачи")
        for task in self.tasks:
            if task['status'] == "not completed":
                print(f"{task['description']} - {task['deadline']}")







