# Incorrect:"result:", result
x = 10
y = 0
result = x / y
print("Result:", result)


# Incorrect:(nubers[i+1])
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i]) # off by one error, delete +1


# Incorrect: # missing colon
def calculate_area(radius)
   area = 3.14 * radius ** 2
   return area 


# Incorrect: if number # missing colons
def is_even(number):
   if number % 2 == 0
       return True
   else
       return False
#
# Incorrect: # missing colons
for i in range(5)
   print(i)

# Incorrect:
def greet(name):
   return "Hello, " + name # missing + sign, not adding them togethere


# Incorrect: # infinite recursion, 
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
sum += number
print("Sum of numbers:", sum)

# Incorrect: infinite recursion , change to 
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n+1)

# Incorrect:  #always evluated to true, need 
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# Incorrect:
def divide_numbers(x, y):
   result = x / y
   return result
 if y == 0:
num1 = 10
num2 = 2 #zero divison error 
print(divide_numbers(num1, num2))
