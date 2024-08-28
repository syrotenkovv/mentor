class Car:
    def __init__(self, lable, model, engine, price):
        from data import StartGame

        self.lable = lable
        self.model = model
        self.engine = engine
        self.price = price

    def info(self):
        print(f"{self.lable}, {self.model}, {self.engine}, {self.price}")

    def type_engine(self):
        choise = input("Вивести всі? y/n: ")
        if choise == "y" or choise == 'Y':
            print(f"{self.lable}, {self.model}, {self.engine}, {self.price}")
        elif choise == "n" or choise == "N":
            print(f"Обери")

