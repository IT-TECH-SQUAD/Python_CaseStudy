from PIL import Image
from PIL import ImageDraw
from src.food import *
import main
import tabulate
import pywhatkit as kit
import os
from termcolor import colored
import datetime
import getpass as gp
from PIL import ImageFont
import phonenumbers as pn
import pywhatkit as kit
import pyqrcode


def qrcode(num):
    with open('output.txt', 'r') as f:
        s = f.read()
    qr = pyqrcode.create(s)
    qr.png('qr.png', scale=12)
    kit.sendwhats_image(num, 'qr.png')
def banner():
    str = '''

  888888 .d8888b. 888888888     88888888888                                8888888b.  .d88888b.  .d8888b.
    "88bd88P  Y88b888               888                                    888   Y88bd88P" "Y88bd8
     888888    888888               888                                    888    888888     888Y88b.
     888888    8888888888b.         888  .d88b.  8888b. 88888b.d88b.       888   d88P888     888 "Y888b.
     888888    888     "Y88b        888 d8P  Y8b    "88b888 "888 "88b      8888888P" 888     888   "Y88b.
     888888    888       888888888  888 88888888.d888888888  888  888888888888       888     888      "888
     88PY88b  d88PY88b  d88P        888 Y8b.    888  888888  888  888      888       Y88b. .d88PY88b  d88P
     888 "Y8888P"  "Y8888P"         888  "Y8888 "Y888888888  888  888      888        "Y88888P"  "Y8888P"
   .d88P
 .d88P"
888P"


    Developed by: Hemerson G. Ramiro Jr.
    Designed by: Geonelle and Joshua
    Video editor: Clarence
    Presentation maker: Aron Jay

    '''
    # print s with rainbow color
    print(colored(str, 'green'))


def subtotal(item):
    x = sum(item)
    return x

def date():
    now = datetime.datetime.now()
    x = now.strftime("%Y-%m-%d %H:%M:%S")
    return x
    
def rec(sentence):
    with open('output.txt', 'w') as f:
        f.write('{}\n'.format(sentence))

def customer(name, status):
    c = Customer(name, status)
    c.set_name(name)
    c.get_name()
    c.set_status(status)
    c.get_status()

    print(c.to_string())

# get total quantity


def total_quantity(quantity):
    return quantity


def toCash(customer_cash,total,name,number,list_items,list_quantity):

    items = ""
    while customer_cash < total:
        try:
            customer_cash = float(input("Please enter the amount of cash you have: "))
        except ValueError:
            print("Please enter a valid amount")
            continue
        if customer_cash < total:
            print("You do not have enough cash")
            if (input("Do you want to continue to pay? Y/N: ")).upper() == "N":
                main()

    change = customer_cash - total
    # print in tabulated format with dollar sign with date and add the quantity of Types and price
    #print all list_items
    items = all_items(list_items)
    
    print(items
          )
    quantity = list_quantity
    #print all items
    
    x = tabulate.tabulate([["Name: "+ str(name)],["Purchases: " + str(items)],["All of Quantity: "+str(quantity)],["Total Amount: " + str(f'${total:.2f}')],["Cash: " + str(f'${customer_cash:.2f}')],["Change: " + str(f'${change:.2f}')],["Date: "+ date()]],headers=["SALES INVOICE","Total Amount","Cash","Change","Date/Time"],tablefmt="psql")
    
    rec(x)
    print(x)
    to_send = (input("Do you want to send the invoice to your phone as qrcode? Y/N: ")).upper()
    if to_send == "Y":
        qrcode(number)
        
    elif to_send == "N":
        img_output(number)
    
    print(f'Thank you for shopping at the Food Court!')    
    # press enter to clear
    input("Press enter to continue")
    os.system('cls')
    return x

def product():
    # Drinks
    product.COKE =.20
    product.FANTA = .30
    product.SALAD = .60
    product.SPRITE = .10
    product.MILKTEA = .50
    # Junkfood
    product.BURGER = .80
    product.PIZZA = 1.00
    product.PASTA = 1.00
    product.NOODLES = .50

    # Meal
    product.HOTSILOG = .90
    product.LONGSILOG = 1.50
    product.TAPSILOG = 1.00
    product.TOSILOG = 1.00
    # Dessert
    product.EGGPIE = .50
    product.SALAD = .60
    product.UBE = .50

    product.var = {"JunkFoods":("Burger","Pizza","Pasta","Noodles")
    ,"Drinks":("Coke","Fanta","Sprite","MilkTea")
    ,"Meal":("Hotsilog","Longsilog","Tapsilog","Tosilog")
    ,"Dessert":("Eggpie","Salad","Ube")}
    product.headers = ["JunkFoods","Drinks","Meal","Dessert"]

    #display all products
    print(tabulate.tabulate([product.var["JunkFoods"],product.var["Drinks"],product.var["Meal"],product.var["Dessert"]],headers=product.headers,tablefmt="psql"))
def all(price,type,list_of_food,quantity):
    # print status verfied tabulated
    combo = Combo(price,type,list_of_food,quantity)
    print(combo.to_string())

def all_orders(x):
    seq = 1
    for i in x:
        # remove nextline
        print(f"{seq} {i}")
        seq += 1
        
def all_items(list_items):
    items = []
    #print all items in list
    for i in list_items:
        items.append(i)
    return items


#create a function to read outoput.txt
def img_output(num):
    with open('output.txt', 'r') as f:
        s = f.read()
    img = Image.open('bg.png')
 
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
 
    # Add Text to an image
    I1.text((28, 36),s, fill=(255, 0, 0))
    # Save the edited image
    img.save("b1.png")
    kit.sendwhats_image(num, 'b1.png')
          
                
def validate(number):

    try:
        pn.parse(number)
        print("Valid")
        return True
    
    except pn.NumberParseException:
        print("Invalid")
        return False

  

if __name__ == "__main__":
    pass