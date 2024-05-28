import random

def randNumber():
    return random.randint(1000,9999)

def correctDigits(num1,num2):
    result=""
    for i in range(4):
        if(num1[i]==num2[i]):
            result+="0"
        else:
            result+="X"
    return result
        
number=str(randNumber())
print("Please enter a 4-digit number!")
for i in range(10):
    result=correctDigits(number,input())
    print("The result is:",end="")
    print(result)
    if(result=="0000"):
        print("Well Done!")
        break
    
    
