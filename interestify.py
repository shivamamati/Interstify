def simple(a,b,c):
    print("The principal amount is :", a)
    print("The number of years for interest is:", b)
    print("The interest is:", c)
    simple_formula = (a * b * c)/100 
    print("The simple interest you will gain is: ", simple_formula)
    full_amount_simple = input("Would you like to see the full interest with principle: Enter Y for Yes and N for No!")
    if full_amount_simple == "Y":
        print(simple_formula + a)
    else:
        print("")

def compound(a,b,c,d):
    print("The principal amount is :", a)
    print("The number of years for interest is:", b)
    print("The interest is:", c)
    print("The number of times you would like to reinvest every year is:", d)
    compound_formula =  a * (1 + (c/100)/d)**(c*d)
    print("The Compound interest you will gain is: ", compound_formula)
    full_amount_compound= input("Would you like to see the full interest with principle: Enter Y for Yes and N for No!")
    if full_amount_compound == "Y":
        print(compound_formula + a)
    else:
        print("")
  
def ask_input():
    global principal, years, interest 
    principal = int(input("What is the principal Investment: "))
    print("")
    years = int(input("Number of years you would like to run the in investment: "))
    print("")
    interest = int(input("What is the number of interest you have been offered: "))
    print("")
  
print("*******************************************************")
print("*                      Interestify                    *")
print("*******************************************************")
print("")

print("Welcome to Interesify, where you could check to see if simple interest or compound interest would be better!")

first = int(input("Which one would you like to start off with! Type 1 for simple interest calculator and 2 for compound interest calculator: "))

if first == 1:
    print("")
    print("Simple Interest Calculator:")
    print("")
    ask_input()
    simple(principal,years,interest)
else:
    print("")
    print("Compound Interest Calculator:")
    print("")
    ask_input()
    per_year = int(input("How many times will ths compound yearly: "))
    compound(principal,years,interest, per_year)
