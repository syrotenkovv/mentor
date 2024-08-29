class Smartphone:
    def __init__(self, lable, model, ram, isc, price):
        self.lable = lable
        self.model = model
        self.ram = ram
        self.isc = isc
        self.price = price

    def display_info(self):
        print(f"{self.lable} - {self.model} - {self.ram} - {self.isc} - {self.price}")

    def is_high_end(self):
        if self.ram >= 128:
            print(f"{self.model}")