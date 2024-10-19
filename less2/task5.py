num1 = int(input())
num2 = int(input())
if num2 == 0:
    print("нельзя делить на ноль")
else:
    quotient = num1 //num2
    remainder = num1 % num2
    print(f"частное:{quotient}")
    print(f"Остаток:{remainder}")
