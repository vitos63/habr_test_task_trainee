from time import sleep


class DistributionSystem:

    def __init__(self, servers_count: int):
        self.servers = {}
        for i in range(1, servers_count + 1):
            self.servers[i] = {"current_task": 0, "queue": []}

    def add_task(self, task: int):
        """Метод для добавления задания
        Данный метод принимает один аргумент task - время выполнения задания
        и добавляет задание очередь менее нагруженного сервера"""

        print(f"Команда: добавить {task}")

        for i in self.servers:
            if not self.servers[i]["current_task"]:
                self.servers[i]["current_task"] = task
                print(f"Задание с {task} секундами выполнения направлено на Сервер {i}.")
                break

        else:
            min_time_server = min(self.servers, key=lambda x: self.servers[x]["current_task"] + sum(self.servers[x]["queue"]))
            self.servers[min_time_server]["queue"].append(task)
            print(f"Задание с {task} секундами выполнения добавлено в очередь на выполнение {min_time_server} сервером")

    def check_status(self):
        """Метод для проверки состояния серверов
        Данный метод выводит на экран состояние сервера, а так же состояние очереди сервера
        """
        for i in self.servers:
            if not self.servers[i]["current_task"]:
                print(f"Сервер {i}: пусто")

            else:
                print(f"Сервер {i}: выполняет задание (осталось {self.servers[i]['current_task']} сек.)")
                if self.servers[i]["queue"]:
                    print(f"Очередь заданий сервера {i}: {self.servers[i]['queue']}")
                else:
                    print(f"Очередь заданий сервера {i} пуста")

    def task_processing(self):
        """Метод выполнения заданий
        Данный метод уменьшает оставшееся время выполнения текущего задания для каждого сервера, если таковые имеются, и выводит состояние серверов.
        Работает до тех пор, пока не выполнятся все задания"""
        
        
        
        self.check_status()
        print("Обработка:")
        flag = True
        while flag:
            flag = False
            for i in self.servers:
                if not self.servers[i]["current_task"]:
                    continue
                flag = True
                self.servers[i]["current_task"] -= 1
                if self.servers[i]["current_task"] == 0:
                    if self.servers[i]["queue"]:
                        self.servers[i]["current_task"] = self.servers[i]["queue"][0]
                        self.servers[i]["queue"] = self.servers[i]["queue"][1:]
                        print(f"- Сервер {i} освобождается и приступает к следующему заданию из очереди")
                    else:
                        print(f"- Сервер {i} завершает выполнение.")
                    self.check_status()

            sleep(1)

        print("Выполнение заданий окончено")


def main():
    servers_count = int(input("Добро пожаловать в симулятор распределенной системы.\nВведите количество серверов: "))
    system = DistributionSystem(servers_count)
    system.check_status()
    system.add_task(5)
    system.add_task(3)
    system.add_task(7)
    system.add_task(2)
    system.task_processing()


if __name__ == '__main__':
    main()
