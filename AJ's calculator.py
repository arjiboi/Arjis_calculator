print("Welcome to Arjun's calculator")
print("Type which type of calculation you would like to perform:")
print("Addition, subtraction, multiplication, division, exponents, roots, or percentage.")
calc_type=input()
if calc_type=="addition" or calc_type=="Addition":
    print("Which numbers would you like to add, starting with the first one?")
    n1=float(input())
    print("Now for the second one...")
    n2=float(input())
    answer=(n1+n2)
elif calc_type=="subtraction" or calc_type=="Subtraction":
    print("Which numbers would you like to subtract from?")
    n1=float(input())
    print("Now for the one you're subtracting...")
    n2=float(input())
    answer=n1-n2
elif calc_type=="multiplication" or calc_type=="Multiplication":
    print("Which numbers would you like to multiply, starting with the first one?")
    n1=float(input())
    print("Now for the second one...")
    n2=float(input())
    answer=n1*n2
elif calc_type=="division" or calc_type=="Division":
    print("What is the dividend (number you're dividing)")
    n1=float(input())
    print("What is the divisor (number you're dividing by)")
    n2=float(input())
    answer=n1/n2
elif calc_type=="exponents" or calc_type=="Exponents" or calc_type=="exponent" or calc_type=="Power" or calc_type=="power":
    print("What is the base (number you're raising to a power)?")
    n1=float(input())
    print("What is the exponent (power you're raising the base to)?")
    n2=float(input())
    answer=pow(n1, n2)
elif calc_type=="roots" or calc_type=="root" or calc_type=="Root" or calc_type=="Roots":
    print("What is the number inside the root?")
    n1=float(input())
    print("What is the level of the root (ex: 4th root)?")
    n2=float(input())
    answer=pow(n1,(1/n2))
elif calc_type=="percentages" or calc_type=="percent" or calc_type=="Percentages" or calc_type=="Percent" or calc_type=="percentages" or calc_type=="Percentages":
    print("What is the percent you want to take (ex:5)? Make sure not to include the percent sign.")
    n1=float(input())
    print("What is the number you're taking a percent of?")
    n2=float(input())
    answer=(n1/100)*n2
else :
    print("That is not an option")
    answer="undefined"
if answer != "undefined":
    print("The answer is" + str(answer) + "!")
print("Reload to try again")