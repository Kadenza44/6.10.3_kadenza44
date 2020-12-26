class Client:

    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Баланс: {self.balance}$"


client1 = Client("Иван", "Петров", 50)

print(client1)
