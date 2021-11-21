from src.food import Drinks, Combo, Meal, JunkFood, Dessert
import sys
import os
from src.util import *
  
def main():
    food ={"UNIT1":["JunkFoods"]
           ,"UNIT2":["Drinks"]
           ,"UNIT3":["Dessert"]
           ,"UNIT4":["Meal"]
           ,"QUIT":["Exit"]}
    # print food tabulated
    # clear screen
    os.system('cls')
    banner()
    name = input("Please enter your name: ")
    number = gp.getpass(prompt="Please enter your phone number(+63): ", stream=None)
    if validate(number):
        print("Valid")
    else:
        print("Invalid")
        main()
    list = ["1","2","3","4","5","6","7","8","9","0","*","#"]
    while name == "" and number == "":
        os.system('cls')
        banner()
        
        try:
            name = input("Please enter your name: ")
            if name == list:
                print("Please enter your name")
                continue

        except ValueError:
            print("Please enter a valid name")
            continue
        if number == "":
            try:
                number = gp.getpass(prompt="Please enter your phone number(+63): ", stream=None)

            except ValueError:
                print("Please enter a valid phone number")
                continue
        elif number[0] != '+':
            number = '+63' + number 
        
        
        elif x == False:
            print("Please enter a valid phone number")
            
    while True:
        os.system('cls')
        product()
        print(tabulate.tabulate(food, headers='keys', tablefmt='psql'))
        try:
            unit = input("Please select the unit you want to order from the following list[Unit<Number>]:").upper()
        except ValueError:
            print("Please enter a valid unit")
            continue
        if unit in food:
            print("\n----------------------------------------------")
            print("You have selected the unit: ",food.get(unit))
            print("----------------------------------------------")
            if unit == "UNIT1":
                print("Do you want to continue to order?")
                ans = input("Y/N: ").upper()
                total =0.00
                qtotal =0
                customer_cash = 0.00
                list = []
                price = []
                brand_list = []
                i = 0
                while ans == "Y":
                    os.system('cls')
                    # invoke prodoct banner
                    product()
                    # print only "Drinks" ta
                    print("---------------JunkFoods-----------------")
                    print(tabulate.tabulate([product.var["JunkFoods"]],tablefmt="pretty"))
                    BURGER = product.BURGER 
                    PIZZA = product.PIZZA 
                    PASTA = product.PASTA
                    NOODLES = product.NOODLES 
                    
                    types = input("Please select the type of JF you want to order from the following list(x to cancel):").upper()
                    if types == "X":
                        main()
                    try:
                        quantity = int(input("Please enter the quantity of JF you want to order(0 to cancel): "))
                        if types == 0:
                            main()
                    except ValueError:
                        print("Please enter a valid quantity")
                        continue
                    if types == "BURGER" or types == "1":
                        
                        brand = BURGER
                        __unit = "Burger"
                        i += 1 #for id iteration
                        junkfood = JunkFood(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of JF orderd
                        list.append(junkfood.to_string())
                        #don't append repeated __list
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        qtotal+=total_quantity(quantity)
                        #don't append the repated price
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper() 

                    elif types == "PIZZA" or types == "2":
            
                        brand = PIZZA
                        __unit = "Pizza"
                        i += 1 #for id iteration
                        junkfood = JunkFood(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of JF orderd
                        list.append(junkfood.to_string())

                        qtotal+=total_quantity(quantity)

                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                    elif types == "PASTA" or types == "3":
                     
                        brand = PASTA
                        __unit = "Pasta"
                        i += 1 #for id iteration
                        junkfood = JunkFood(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of JF orderd
                        list.append(junkfood.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                            
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)
                        
                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                    elif types == "NOODLES" or types == "4":
               
                        brand = NOODLES
                        __unit = "Noodles"
                        i += 1 #for id iteration
                        junkfood = JunkFood(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of JF orderd
                        list.append(junkfood.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()

                    if types != "BURGER" and types != "1" and types != "PIZZA" and types != "2" and types != "PASTA" and types != "3" and types != "NOODLES" and types != "4":
                        os.system('cls')
                        print("------------Invalid input value-------------")
                    
                    elif ans != "Y" and ans  != "N":
                        ans = "Y"      
                    if ans == "N":
                        all(total,food.get(unit),[junkfood],qtotal)
                        toCash(customer_cash,total,name,number,brand_list,qtotal)
                        main()
                        
                if ans.upper() == "N":
                    main()  #return to main menu
            elif unit == "UNIT2":
                print("Do you want to continue to order?")
                ans = input("Y/N: ")
                total =0.00
                qtotal =0
                customer_cash = 0.00
                list = []
                price = []
                brand_list = []
                i = 0
                while ans.upper() == "Y":
                    os.system('cls')
                    # invoke product banner
                    product()
                    print("---------------Drinks-----------------")
                    print(tabulate.tabulate([product.var["Drinks"]],tablefmt="pretty"))
                    COKE = product.COKE
                    FANTA = product.FANTA
                    SPRITE = product.SPRITE
                    MILKTEA = product.MILKTEA
                    
                    types = input("Please select the type of Drinks you want to order from the following list(x to cancel):").upper()
                    if types == "X":
                        main()
                    try:
                        quantity = int(input("Please enter the quantity of Drink(s) you want to order(0 to cancel): "))
                        if types == 0:
                            main()
                    except ValueError:
                        print("Please enter a valid quantity")
                        continue
                    if types == "COKE" or types == "1":
                        
                        brand = COKE
                        __unit = "Coke"
                        i += 1 #for id iteration
                        drinks = Drinks(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(drinks.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()

                    elif types == "FANTA" or types == "2":
            
                        brand = FANTA
                        __unit = "Fanta"
                        i += 1 #for id iteration
                        drinks = Drinks(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(drinks.to_string())
                        qtotal+=total_quantity(quantity)
                        
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)
                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper

                    elif types == "SPRITE" or types == "3":
                     
                        brand = SPRITE
                        __unit = "Sprite"
                        i += 1 #for id iteration
                        drinks = Drinks(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(drinks.to_string())
                        qtotal+=total_quantity(quantity)
                        
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                    elif types == "MILKTEA" or types == "4":
               
                        brand = MILKTEA
                        __unit = "Milktea"
                        i += 1 #for id iteration
                        drinks = Drinks(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(drinks.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)


                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()

                    if types != "COKE" and types != "1" and types != "FANTA" and types != "2" and types != "SPRITE" and types != "3" and types != "MILKTEA" and types != "4" or quantity < 1:
                        os.system('cls')
                        print("------------Invalid input value-------------")
                    elif ans != "Y" and ans  != "N":
                        ans = "Y"      
                    if ans == "N":
                        all(total,food.get(unit),[drinks],qtotal)
                        toCash(customer_cash,total,name,number,brand_list,qtotal)
                        main()
                        

                if ans.upper() == "N":
                    main()  #return to main menu
            elif unit == "UNIT3":
                print("Do you want to continue to order?")
                ans = input("Y/N: ")
                total =0.00
                qtotal =0
                customer_cash = 0.00
                list = []
                price = []
                brand_list = []
                i = 0
                while ans.upper() == "Y":
                    os.system('cls')
                    # invoke product banner
                    product()
                    print("----------------Dessert---------------------")
                    print(tabulate.tabulate([product.var["Dessert"]],tablefmt="pretty"))
                    EGGPIE = product.EGGPIE
                    SALAD = product.SALAD 
                    UBE = product.UBE 


                    types = input("Please select the type of Dessert you want to order from the following list(x to cancel):").upper()
                    if types == "X":
                        main()
                    try:
                        quantity = int(input("Please enter the quantity of Dessert you want to order(0 to cancel): "))
                        if types == 0:
                            main()
                    except ValueError:
                        print("Please enter a valid quantity")
                        continue

                    if types == "EGGPIE" or types == "1":
                        brand = EGGPIE
                        __unit = "Eggpie"
                        # print(quantity)
                        i += 1 #for id iteration
                        dessert = Dessert(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of dessert orderd
                        list.append(dessert.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)
                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                        
                    elif types == "SALAD" or types == "2":
                        brand = SALAD
                        __unit = "Salad"
                        # print(quantity)
                        i += 1 #for id iteration
                        dessert = Dessert(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of dessert orderd
                        list.append(dessert.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                        
                    elif types == "UBE" or types == "3":
                        brand = UBE
                        __unit = "Ube"
                        # print(quantity)
                        i += 1 #for id iteration
                        dessert = Dessert(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of dessert orderd
                        list.append(dessert.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                
                    if types != "EGGPIE" and types != "1" and types != "SALAD" and types != "2" and types != "UBE" and types != "3" or quantity < 1:
                        os.system('cls')
                        print("------------Invalid input value-------------")
                    elif ans != "Y" and ans  != "N":
                        ans = "Y"      
                    if ans == "N":
                        all(total,food.get(unit),[dessert],qtotal)
                        toCash(customer_cash,total,name,number,brand_list,qtotal)
                        main()
                        
                if ans.upper() == "N":
                    main()  #return to main menu            
            elif unit == "UNIT4":
                print("Done")
                print("Do you want to continue to order?")
                ans = input("Y/N: ")

                total =0.00
                qtotal =0
                customer_cash = 0.00
                list = []
                price = []
                brand_list = []
                i = 0

                while ans.upper() == "Y":
                    os.system('cls')
                    # invoke prodoct banner
                    product()
                    # print only "Drinks" ta
                    print("----------------Meals---------------------")
                    print(tabulate.tabulate([product.var["Meal"]],tablefmt="pretty"))
                    HOTSILOG = product.HOTSILOG = .90
                    LONGSILOG = product.LONGSILOG = 1.50
                    TAPSILOG = product.TAPSILOG = 1.00
                    TOSILOG = product.TOSILOG = 1.00

                    types = input("Please select the type of Meal you want to order from the following list(x to cancel):").upper()
                    if types == "X":
                        main()
                    try:
                        quantity = int(input("Please enter the quantity of Meal you want to order(0 to cancel): "))
                        if types == 0:
                            main()
                    except ValueError:
                        print("Please enter a valid quantity")
                        continue

                    if types == "HOTSILOG" or types == "1":
                        brand = HOTSILOG
                        __unit = "Hotsilog"
                        # print(quantity)
                        i += 1 #for id iteration
                        meal = Meal(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(meal.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                    elif types == "LONGSILOG" or types == "2":
                        brand = LONGSILOG
                        __unit = "Longsilog"
                        # print(quantity)
                        i += 1 #for id iteration
                        meal = Meal(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(meal.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)
                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                        
                    elif types == "TAPSILOG" or types == "3":
                        brand = TAPSILOG
                        __unit = "Tapsilog"
                        # print(quantity)
                        i += 1 #for id iteration
                        meal = Meal(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(meal.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        print(brand_list)
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                    elif types == "TOSILOG" or types == "4":
                        brand = TOSILOG
                        __unit = "TOSILOG"
                        # print(quantity)
                        i += 1 #for id iteration
                        meal = Meal(i,food.get(unit),__unit,quantity,float(brand))
                        # adding list of drinks orderd
                        list.append(meal.to_string())
                        qtotal+=total_quantity(quantity)
                        if __unit not in brand_list:
                            brand_list.append(__unit + ":"+str(quantity))
                        price.append(brand*quantity)
                        total = subtotal(price)
                        c = '\n'.join(list)

                        print("\n----------------------------------------------")
                        print(c)
                        print("----------------------------------------------")
                        ans = input("Do you want to add your order? Y/N: ").upper()
                
                    if types != "HOTSILOG" and types != "1" and types != "LONGSILOG" and types != "2" and types != "TAPSILOG" and types != "3" and types != "TOSILOG" and types != "4" or quantity < 1:
                        os.system('cls')
                        print("------------Invalid input value-------------")
                    elif ans != "Y" and ans  != "N":
                        ans = "Y"      
                    if ans == "N":
                        all(total,food.get(unit),[meal],qtotal)
                        toCash(customer_cash,total,name,number,brand_list,qtotal)
                        main()

                if ans.upper() == "N":
                    print("Program Exit!")
                    main()  #return to main menu 
                
            elif unit == "QUIT":
            # terminate the program
                print("Thank you for coming") 
                # exit system
                sys.exit()
            else:
                print("----------Invalid selection-------------")
                
if __name__ == "__main__":
    main()
    
