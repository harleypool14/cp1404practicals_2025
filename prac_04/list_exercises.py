numbers = []
for i in range(5):
    num = input(input(f"Number {1 + i}:"))
    numbers.append(num)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The Largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

