def calculator ():
    num_1= float (input("Enter the first number: "))
    num_2= float (input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
  
    if(operator=="+"):
        answer=num_1+num_2
    elif(operator=="-"):
        answer=num_1-num_2
    elif(operator=="*"):
        answer=num_1*num_2
    elif(operator=="/" and num_2!=0):
        answer=num_1/num_2
    elif(operator=="/" and num_2==0):
        answer = "Error! Division by zero is not allowed."
    else:
        answer ="Invalid operator. Please enter a valid operator (+, -, *, /)."
    
    result = print(f"{num_1}{operator}{num_2}={answer}")

  
    
print("Hello! Welcome to the calculator program.")
print(calculator())

 