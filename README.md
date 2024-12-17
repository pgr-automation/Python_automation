# Python_automation

## Python Fundamentals
- Variables and Data Types:
```python
name = "Alice"
age = 25
is_active = True
```
- Input/Output:
```python
user_input = input("Enter your name: ")
print(f"Hello, {user_input}")
```
- Control Flow:
```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```
- Loops:
```python
for i in range(5):
    print(i)

while age > 0:
    age -= 1
```
---
## Data Structures
- Lists:
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])
```

- Dictionaries:
```python
person = {"name": "Alice", "age": 25}
print(person["name"])
```

- Tuples:
```python
coordinates = (10, 20)
```
- Sets:
```python
unique_items = {1, 2, 3, 3}
```

---

## Functions
- Define and call functions:
```python
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

- Lambda functions:
```python
add = lambda x, y: x + y
print(add(2, 3))
```
---
## File Handling
- Read/Write files:
```python
with open("test.txt", "w") as file:
    file.write("Hello, File!")

with open("test.txt", "r") as file:
    print(file.read())
```
---
## Object-Oriented Programming (OOP)

- Classes and Objects:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}!"

p = Person("Alice", 25)
print(p.greet())
```
---
- Inheritance:
```python
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

```

---
##  Modules and Packages
- Importing modules:
```python
import math
print(math.sqrt(16))
```
- Create your own module:
```python
mkdir mypackage
echo "def say_hello(): print('Hello!')" > mypackage/my_module.py
```
- Use it:
```python
from mypackage.my_module import say_hello
say_hello()
```

---
## Error Handling
- Try-Except:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
```
---