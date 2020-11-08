# Exercise 1

num = int(input("Enter a num: "))
count = int(input("Enter the count: "))
n = num

while count > 0:
    if n % num == 0:
        print(n, end=' ')
        count -= 1
    n += 1

print( )
print( )

# Exercise 2

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
string = input("Enter a string: ")
vowels_amount = 0

for c in string:
    if c in vowels:
        vowels_amount += 1

print(vowels_amount)

print( )

# Exercise 3

list1 = ["my", 1, "turtle", "explain", 3.14]
x = 0

for x in list1:
    if isinstance(x, int) or isinstance(x, float):
        list1.remove(x)
print(list1)
print( )

# Exercise 4

number = input("Enter a number: ")

if number == number[::-1]:
    print(number, "is symetrical")
else:
    print(number, "isn't symetrical")
