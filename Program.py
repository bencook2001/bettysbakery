import sys

small = {"flour" : 250,
          "sugar" : 200,
          "butter" : 125,
          "egg" : 6}

medium = {"flour" : 500,
          "sugar" : 400,
          "butter" : 250,
          "egg" : 10}

large = {"flour" : 750,
         "sugar" : 600,
         "butter" : 500,
         "egg" : 12}

recipe = {"flour" : 12,
          "sugar" : 14,
          "butter" : 4,
          "egg" : 0.1}

def start():
    print("10 Chocolate Cupcakes")
    print()
    print("120g plain flour")
    print("140g sugar")
    print("1 teaspoon baking powder")
    print("40g unsalted butter")
    print("50g dark chocolate")
    print("1 free-range egg")
    print("125ml milk")
    print("1 orange juice only")
    print()
    print()
    print("1 Lemon Drizzle Cake")
    print("4 1/2 free range eggs")
    print("300g sugar")
    print("140ml double cream")
    print("3 lemons, zest only")
    print("1 pinch salt")
    print("80g unsalted butter")
    print("240g plain flour")
    print("1/2 teaspoon baking powder")
    print()
    print()
    print("Do you want to make Chocolate Cupcakes or a Lemon Drizzle Cake?")
    cake = input("Enter 'Chocolate' or 'Lemon': ")

    if cake == "chocolate".lower():
        chocolate()

    elif cake == "lemon".lower():
        lemon()

    else:
        print("Answer not recognised.")
        sys.exit()
        
def chocolate():
    choc_amount = int(input("How many Chocolate cupcakes do you want to make?: "))
    choc_flour = recipe["flour"] * choc_amount
    choc_sugar = recipe["sugar"] * choc_amount
    choc_butter = recipe["butter"] * choc_amount
    choc_egg = recipe["egg"] * choc_amount

    print()
    print("Here are your ingredients:")
    print(choc_flour,"flour")
    print(choc_sugar,"sugar")
    print(choc_butter,"butter")
    print(choc_egg,"egg")
    
def lemon():
    lemon_amount = int(input("How many Lemon Drizzle cakes do you want to make?"))
    
start()
