#exercise 2 : faulty calculator
# taking input of operator and two numbers from user creat a calculator which will solve calculations correctly except follwing calculations :
#--->45*3 = 55 
#--->56+9 = 77 
#--->56/6 = 3 

# taking input operator for operation
inp1 = input("operator")
# enter 1st number from user
inp2 = input("enter first number")
# enter 2nd number from user
inp3 = input("enter second number")

new_input = inp2 + inp1 + inp3

if new_input == "45*3":
    print(55)
elif new_input == "56+9":
    print(77)
elif new_input == "56/6":
    print(3)
elif inp1 == "*":
    print(int(inp2) * int(inp3))
elif inp1 == "+":
    print(int(inp2) + int(inp3))
elif inp1 == "-":
    print(int(inp2) - int(inp3))
elif inp1 == "/":
    print(int(inp2) / int(inp3))
