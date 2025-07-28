print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Small pizza (S) - $15
# Medium pizza (M) - $20
# Large pizza (L) - $25
# Add pepperoni for small pizza +$2
# Add pepperoni for medium or large pizza +$3
# Add extra cheese any size pizza +$1

bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill = bill + 2
if size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = bill + 3
if size == "L":
    bill = 25
    if pepperoni == "Y":
        bill = bill + 3
if extra_cheese == "Y":
    bill = bill +1
print(f"Your final bill is: ${bill}")
