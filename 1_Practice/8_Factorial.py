num = int(input("Enter a number: "))

def fact(n):
    if n > 0:
        s = 1
        for i in range(1, n + 1):
            s = s * i
        return s
    else:
        return "Enter a valid number."

result = fact(num)
print(f"Factorial of {num} is: {result}")
