num = int(input('1つの自然数を入れてください:'))

if num % 3 == 0:
    output = "Fizz"
elif num % 5 == 0:
    output = "Buzz"
else:
    output = str(num)

print(output)
