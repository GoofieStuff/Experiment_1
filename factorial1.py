n = int(input("Enter a number: "))
ans = 1

for i in range(1, n + 1):
    ans *= i

print(f"The factorial of {n} is {ans}")

print("This is changed code.")