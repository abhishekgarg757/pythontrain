def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

calc_dict={}
calc_dict["+"]=add
calc_dict["-"]=sub
calc_dict["*"]=multiply
calc_dict["/"]=divide
num1 = int(input("whats your first number"))
operation = input("pick and operation from +,-,*,/")
num2 = int(input("whats your second number"))
def work():
    return calc_dict[operation](num1,num2)
output = work()
print(f"your answer is {output}")

next_action = input(f"type y to continue your calculation with {output} or type n to start new calculation")
while next_action == "y" or next_action == "n":
    if next_action == "y":
        num1 = output
        operation = input("pick and operation from +,-,*,/")
        num2 = int(input("whats your second number"))
        output = work()
        print(f"your answer is {output}")
        next_action = input(f"type y to continue your calculation with {output} or type n to start new calculation")
    if next_action == "n":
        num1 = int(input("whats your first number"))
        operation = input("pick and operation from +,-,*,/")
        num2 = int(input("whats your second number"))
        def work():
            return calc_dict[operation](num1,num2)
        output = work()
        print(f"your answer is {output}")
        
        next_action = input(f"type y to continue your calculation with {output} or type n to start new calculation")
        
    
    
        
    
