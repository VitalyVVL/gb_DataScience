
num = int(input("Enter a positive integer: "))
n = num
max_digit = n % 10
while n:
    a = n % 10
    if a>max_digit:
        max_digit = a
        if max_digit == 9: break

    n = n // 10

print(max_digit)
