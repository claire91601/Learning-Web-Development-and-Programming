firstNumber = int(input("Please enter your first number here:  "))
secondNumber = int(input("Please enter your second number here:  "))
thirdNumber = int(input("Please enter your third number here:  "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    largest = firstNumber
elif firstNumber < secondNumber and firstNumber < thirdNumber:
    smallest = firstNumber
if secondNumber > firstNumber and secondNumber > thirdNumber:
    largest = secondNumber
elif secondNumber < firstNumber and secondNumber < thirdNumber:
    smallest = secondNumber
if thirdNumber > firstNumber and thirdNumber > secondNumber:
    largest = thirdNumber
elif thirdNumber < firstNumber and thirdNumber < secondNumber:
    smallest = thirdNumber

print(f"The largest value is {largest}")
print(f"The smallest value is {smallest}")