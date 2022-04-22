

a = int(input("Enter how much the athlete ran on the first day: "))
b = int(input("Enter how much you need to run: "))

temp_a = a
num_day =0
while temp_a<=b:
    temp_a*=1.1
    num_day +=1
print(f"Day: {num_day} = {temp_a:.2f}")


