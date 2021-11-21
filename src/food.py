class Food:
    def __init__(self, id, quantity, type, unit, price, currency):
        self.id = id
        self.quantity = quantity
        self.currency = currency
        self.unit = unit
        self.type = type
        self.price = price


class JunkFood(Food):
    def __init__(self,id,type,unit,quantity,price):
        super().__init__(1,type,quantity,unit,price,"$")
        self.drinks = unit
        self.quantity = quantity
        self.price = price
        self.type = type
        self.id = id
    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price   

    def to_string(self):
        s = str(self.id) + ". " + "JunkFood :"+" --> "+ "Unit: " + str(self.drinks)+" --> "+"Price: " + str(self.currency)+ str(self.get_price()) + " --> " + "Quantity: " + str(self.get_quantity())
        return s

class Meal(Food):
    def __init__(self,id,type,unit,quantity,price):
        super().__init__(1,type,quantity,unit,price,"$")
        self.drinks = unit
        self.quantity = quantity
        self.price = price
        self.type = type
        self.id = id

    def get_quantity(self):
        return self.quantity
    #get price
    def get_price(self):
        return self.price

    def to_string(self):
        s = str(self.id) + ". " + "Meal :"+" --> "+ "Unit: " + str(self.drinks)+" --> "+"Price: " + str(self.currency)+ str(self.get_price()) + " --> " + "Quantity: " + str(self.get_quantity())
        return s

class Drinks(Food):
    def __init__(self,id,type,unit,quantity,price):
        super().__init__(1,type,quantity,unit,price,"$")
        self.drinks = unit
        self.quantity = quantity
        self.price = price
        self.type = type
        self.id = id
    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price   

    def to_string(self):
        s = str(self.id) + ". " + "Drinks :"+" --> "+ "Unit: " + str(self.drinks)+" --> "+"Price: " + str(self.currency)+ str(self.get_price()) + " --> " + "Quantity: " + str(self.get_quantity())
        return s
        
class Dessert(Food):
    def __init__(self,id,type,unit,quantity,price):
        super().__init__(1,type,quantity,unit,price,"$")
        self.drinks = unit
        self.quantity = quantity
        self.price = price
        self.type = type
        self.id = id

    def get_quantity(self):
        return self.quantity
    #get price
    def get_price(self):
        return self.price

    def to_string(self):
        s = str(self.id) + ". " + "Dessert :"+" --> "+ "Unit: " + str(self.drinks)+" --> "+"Price: " + str(self.currency)+ str(self.get_price()) + " --> " + "Quantity: " + str(self.get_quantity())
        return s

class Combo(Food):
    def __init__(self,price,type, food_list,quantity):
        self.food_list = food_list
        self.total_quantity = quantity
        self.type = type
        self.price = price
    def get_quantity(self):
        return self.total_quantity

    def get_price(self):
        return self.price

    def to_string(self):
        print("Items you ordered")
        for item in self.food_list:
            s =str(item.type)+" ------> "+"Total Price: " + str(item.currency)+ str(f'{self.get_price():.2f}') +" ------> "+ " Total Quantity: "+ str(self.get_quantity())
            return s

