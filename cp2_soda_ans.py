class Soda:
    def __init__(self, item, quantity, total):
        self.item = item
        self.quantity = quantity
        self.total = total 
    def count_price(self):
        if self.item.lower() == "coke":
            self.total =  25 * self.quantity
        elif self.item.lower() == "sprite":
            self.total =  30 * self.quantity
        elif self.item.lower() == "fanta":
            self.total =  35 * self.quantity
        return self.total

def main():
    total = 0  
    item = input("你想買什麼汽水? ")
    quantity = input("需要多少個? ")
    quantity = int(quantity)
    soda = Soda(item, quantity, total)
    print("總共: ", soda.count_price(), "元")

if __name__=="__main__": 
    main() 