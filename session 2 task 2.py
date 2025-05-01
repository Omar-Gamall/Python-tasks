# Filter and transofmr a list 

numbers = list(range(1, 21))
divisible_by_3 = []

for number in numbers:
    if number % 3 == 0:
        divisible_by_3.append(number)

# Print the numbers divisible by 3
print("Numbers divisible by 3 are as follows:")
for num in divisible_by_3:
    print(num)
