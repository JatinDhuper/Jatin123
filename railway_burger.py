#1. Railway Ticket Booking System:-
print("Welcome to the Code Rail")
print("We are here to provide best railway ticket booking facility to our users")
name = input("Enter your Name:")
age = int(input("Enter your Age:"))

print("""
First Class: Rs.1500
Second Class: Rs.1000
Third Class: Rs.500
""")

travel_class = input("Enter the desired Travel Class:")
ticket_price = 0
print("You have following options available:")

if travel_class == "First Class":
    ticket_price = 1500
elif travel_class == "Second Class":
    ticket_price = 1000
elif travel_class == "Third Class":
    ticket_price = 500

meal = input("Do you want to include meal:")
meal1  = 0
if meal == "Yes":
    print("Since, you have added meal")
    print("You have to pay Rs.200 extra for your total railway cost")
    meal1 = meal1 + 200
elif meal == "No":
    print("No, extra price will be added to your ticket")
    meal1 = 0
total_cost = 0


if age<5:
    print("Since, you are 5 years old, your ticket price is free")
    print("Essential details for Railway Ticket Booking:")
    print("Name:", name)
    print("Age:", age)
    print("Travel Class:", travel_class)
    print("Meal Price:", meal1)
    total_cost = ticket_price + meal1
    print("Total Estimated cost of your trip", name, "is:", total_cost)

elif age>60:
    print("Since, you are a Senior Citizen, you have 20 percent discount on your total cost")
    print("Essential details for Railway Ticket Booking:")
    print("Name:", name)
    print("Age:", age)
    print("Travel Class:", travel_class)
    print("Meal Price:", meal1)
    total_cost = ticket_price + meal1
    print("Total Estimated cost of your trip", name, "is:", total_cost)

elif 5<age<60:
    print("You will be charged for your ticket for regular basis")
    print("Essential details for Railway Ticket Booking:")
    print("Name:", name)
    print("Age:", age)
    print("Travel Class:", travel_class)
    print("Meal Price:", meal1)
    total_cost = ticket_price + meal1
    print("Total Estimated cost of your trip", name, "is:", total_cost)



#2. Burger King:
print("Welcome to Burger King")
print("Menu for Items available in Burger King:")
print("""
    Item            Price(Rs)
    Whopper Burger: Rs.150
    Crispy Veg:     Rs.100
    Chicken Wings:  Rs.120
""")
item = int(input("Enter the item number:"))
cost = 0
if item == 1:
    print("You have ordered for Whopper Burger whose cost is Rs.150")
    quantity = int(input("Enter the quantity:"))
    cost = 150 * quantity
elif item == 2:
    print("You have ordered for Crispy Veg whose cost is Rs.100")
    quantity = int(input("Enter the quantity:"))
    cost = 100 * quantity
elif item == 3:
    print("You have ordered for Chicken Wings whose cost is Rs.120")
    quantity = int(input("Enter the quantity:"))
    cost = 120 * quantity

coupon = input("Do you have a coupon code:")
if coupon == "Yes":
    print("Enter the coupon, and you will get discount based on the coupon")
    code = input("Enter your coupon code:")
    if code == "KING50":
        print("You will get 50 perecent discount")
        total_cost = cost - (cost/2)
        print("Your Total Bill:",total_cost)
    elif code == "BK20":
        print("You will get 20 perecent dicount")
        total_cost = cost - (cost/5)
        print("Your Total Bill:",total_cost)
    else:
        print("You have entered invalid code")

elif coupon == "No":
    print("You will be charged regularly")
    print("Your total bill:", cost)


