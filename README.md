# Python Fundamentals - Comprehensive Notes

## Getting Started

### Running Python Code
```bash
python script.py  # Run a Python script
```

### Indentation
- **Critical**: Python uses indentation (spaces/tabs) to define code blocks
- Standard: 4 spaces per indentation level
- Consistent indentation is mandatory - mixing tabs and spaces causes errors

### Libraries
- Collections of pre-written functions and classes
- Import with `import library_name` or `from library import function`
- Examples: `math`, `random`, `datetime`, `os`

### F-Strings (Formatted String Literals)
```python
name = "Alice"
age = 25
print(f"Hello, {name}! You are {age} years old.")
# Output: Hello, Alice! You are 25 years old.

# With expressions
print(f"Next year you'll be {age + 1}")
```

---

## Variables
Identifier - names given to variables

### Identifier Rules
- Start with letter or underscore (not number)
- Can contain letters, numbers, underscores
- Case-sensitive (`name` ≠ `Name`)
- Use snake_case convention: `first_name`, `total_count`
- Avoid Python keywords: `def`, `class`, `if`, etc.

### Assignment
```python
x = 10          # Integer
name = "John"   # String
is_active = True # Boolean
```

---

## Expressions and Statements

### Expression
- Evaluates to a value
- Examples: `1 + 1`, `x * 2`, `"Hello" + " World"`

### Statement
- An instruction that performs an action
- Examples: `x = 5`, `print("Hello")`, `if x > 0:`

---

## Comments
```python
# Single line comment
x = 5  # Inline comment

"""
Multi-line comment
or docstring
"""
```

---

## Data Types

### Primitive Types
- **int**: Whole numbers (`42`, `-17`)
- **float**: Decimal numbers (`3.14`, `-2.5`)
- **str**: Text (`"Hello"`, `'Python'`)
- **bool**: True/False values

### Non-Primitive Types
- **list**: Ordered, mutable collection `[1, 2, 3]`
- **tuple**: Ordered, immutable collection `(1, 2, 3)`
- **dict**: Key-value pairs `{"name": "John", "age": 30}`
- **set**: Unordered collection of unique items `{1, 2, 3}`

### Type Checking with isinstance()
```python
isinstance(object, classinfo)

# Examples
isinstance(42, int)        # True
isinstance("hello", str)   # True
isinstance([1, 2], list)   # True
isinstance(3.14, (int, float))  # True (tuple of types)
```

### Type Casting
```python
# String to number
int("123")      # 123
float("3.14")   # 3.14

# Number to string
str(42)         # "42"
str(3.14)       # "3.14"

# To boolean
bool(1)         # True
bool(0)         # False
bool("")        # False
bool("hello")   # True

# List/tuple conversion
list((1, 2, 3)) # [1, 2, 3]
tuple([1, 2, 3]) # (1, 2, 3)
```

---

## Operators

### Assignment Operators
```python
x = 5       # Basic assignment
x += 3      # x = x + 3
x -= 2      # x = x - 2
x *= 4      # x = x * 4
x /= 2      # x = x / 2
x //= 3     # x = x // 3 (floor division)
x %= 2      # x = x % 2 (modulo)
x **= 2     # x = x ** 2 (exponentiation)
```

### Arithmetic Operators
```python
+    # Addition
-    # Subtraction
*    # Multiplication
/    # Division (returns float)
//   # Floor division (returns integer)
%    # Modulo (remainder)
**   # Exponentiation

# Examples
10 / 3   # 3.3333...
10 // 3  # 3 (floor division)
10 % 3   # 1 (remainder)
2 ** 3   # 8 (2 to the power of 3)
```

### Comparison Operators
```python
==   # Equal to
!=   # Not equal to
<    # Less than
>    # Greater than
<=   # Less than or equal to
>=   # Greater than or equal to

# All return boolean values (True/False)
```

### Boolean Operators
```python
and  # Both conditions must be True
or   # At least one condition must be True
not  # Inverts the boolean value

# Examples
True and False  # False
True or False   # True
not True       # False

# Short-circuit evaluation
x = 5
result = x > 0 and x < 10  # True (both conditions checked)
result = x < 0 or x > 10   # False (second condition not checked if first is True)
```

### Falsy Values in Python
```python
# These evaluate to False in boolean context:
False, 0, 0.0, "", [], {}, (), None

# Everything else is truthy
bool(0)      # False
bool("")     # False
bool([])     # False
bool("hi")   # True
bool([1])    # True
```

### Bitwise Operators
```python
&    # AND
|    # OR
^    # XOR
~    # NOT (complement)
<<   # Left shift
>>   # Right shift

# Example
5 & 3   # 1 (101 & 011 = 001)
5 | 3   # 7 (101 | 011 = 111)
```

### Identity and Membership Operators
```python
# 'is' - checks if two variables refer to the same object
x = [1, 2, 3]
y = x
print(x is y)  # True

# 'in' - checks if value exists in sequence
print(2 in [1, 2, 3])      # True
print("lo" in "hello")     # True
```

### Ternary Operator
```python
# Syntax: value_if_true if condition else value_if_false
age = 18
status = "adult" if age >= 18 else "minor"
print(status)  # "adult"

# Can be nested (but avoid for readability)
result = "positive" if x > 0 else "zero" if x == 0 else "negative"
```

---

## Strings

### String Creation
```python
single = 'Hello'
double = "World"
multiline = """This is a
multi-line
string"""

# All are equivalent for single-line strings
```

### String Concatenation
```python
first = "Hello"
second = "World"
result = first + " " + second  # "Hello World"

# Better approach with f-strings
result = f"{first} {second}"
```

### String Methods
```python
text = "hello world"

# Case methods
text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.title()        # "Hello World"
text.capitalize()   # "Hello world"
text.swapcase()     # "HELLO WORLD"

# Check case
text.isupper()      # False
text.islower()      # True
text.istitle()      # False

# Character type checks
text.isalpha()      # False (contains space)
text.isalnum()      # False (contains space)
text.isdigit()      # False
text.isspace()      # False

# Other useful methods
text.strip()        # Remove whitespace from ends
text.replace("world", "Python")  # "hello Python"
text.split(" ")     # ["hello", "world"]
text.startswith("hello")  # True
text.endswith("world")    # True
text.find("world")  # 6 (index of substring)
text.count("l")     # 3 (occurrences)
```

### Common Global Functions for Strings
```python
len("hello")        # 5 (length)
str(123)           # "123" (convert to string)
repr("hello")      # "'hello'" (string representation)
ord('A')           # 65 (ASCII value)
chr(65)            # 'A' (character from ASCII)
```

### Using 'in' Operator with Strings
```python
print("world" in "hello world")  # True
print("xyz" in "hello world")    # False
```

### Escape Characters
```python
# Use backslash (\) to escape special characters
print("She said \"Hello\"")     # She said "Hello"
print('It\'s a beautiful day')   # It's a beautiful day
print("Line 1\nLine 2")         # Line 1 (newline) Line 2
print("Tab\tSeparated")         # Tab    Separated
print("Path: C:\\Users\\Name")   # Path: C:\Users\Name

# Raw strings (ignore escape characters)
print(r"C:\Users\Name")         # C:\Users\Name
```

### String Indexing and Slicing
```python
text = "Python"

# Indexing (0-based)
text[0]     # 'P' (first character)
text[-1]    # 'n' (last character)
text[-2]    # 'o' (second to last)

# Slicing [start:end:step]
text[0:3]   # 'Pyt' (characters 0, 1, 2)
text[2:]    # 'thon' (from index 2 to end)
text[:4]    # 'Pyth' (from start to index 3)
text[::2]   # 'Pto' (every 2nd character)
text[::-1]  # 'nohtyP' (reverse string)

# Range function often used with strings
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")
```

---

## Booleans

### Boolean Type
```python
is_active = True
is_complete = False

# Type checking
isinstance(True, bool)  # True
type(True)             # <class 'bool'>
```

### Truthiness Rules
```python
# Numbers: 0 is False, everything else is True
bool(0)      # False
bool(1)      # True
bool(-5)     # True

# Strings: empty string is False, everything else is True
bool("")     # False
bool("hi")   # True

# Collections: empty is False, non-empty is True
bool([])     # False (empty list)
bool([1])    # True (non-empty list)
bool({})     # False (empty dict)
bool({"a": 1}) # True (non-empty dict)
bool(())     # False (empty tuple)
bool(set())  # False (empty set)
```

### Global Functions with Booleans
```python
# any() - returns True if ANY element is True
any([False, False, True])   # True
any([False, False, False])  # False
any([])                     # False (empty iterable)

# all() - returns True if ALL elements are True
all([True, True, True])     # True
all([True, False, True])    # False
all([])                     # True (empty iterable)

# Examples with conditions
numbers = [1, 2, 3, 4, 5]
any(x > 3 for x in numbers)  # True (4 and 5 are > 3)
all(x > 0 for x in numbers)  # True (all are positive)
```

---

## Complex Numbers

### Complex Number Basics
```python
# Complex numbers: real + imaginary part
# Imaginary unit: j (not i like in math)

# Creation methods
complex1 = 2 + 3j          # Direct notation
complex2 = complex(2, 3)   # Using complex() function

print(complex1)  # (2+3j)
print(complex2)  # (2+3j)
```

### Accessing Parts
```python
num = 2 + 3j

# Get real and imaginary parts (returns floats)
real_part = num.real       # 2.0
imag_part = num.imag       # 3.0

print(type(real_part))     # <class 'float'>
print(type(imag_part))     # <class 'float'>
```

### Complex Number Operations
```python
a = 2 + 3j
b = 1 + 4j

# Basic operations
print(a + b)      # (3+7j)
print(a - b)      # (1-1j)
print(a * b)      # (-10+11j)
print(a / b)      # (0.8235294117647058-0.29411764705882354j)

# Other operations
print(abs(a))     # 3.605551275463989 (magnitude)
print(a.conjugate()) # (2-3j) (complex conjugate)
```
# Python Data Structures & Built-ins - Comprehensive Notes

## Built-in Functions for Numbers

### Mathematical Functions
```python
# Absolute value
abs(-5)         # 5
abs(3.14)       # 3.14
abs(-2.7)       # 2.7

# Rounding
round(5.49)     # 5 (rounds to nearest integer)
round(5.5)      # 6 (rounds to nearest even number)
round(5.49, 1)  # 5.5 (1 decimal place)
round(123.456, 2)  # 123.46 (2 decimal places)

# Min and Max
min(1, 5, 3)    # 1
max([1, 5, 3])  # 5
min("hello")    # 'e' (alphabetically first)

# Sum
sum([1, 2, 3, 4])  # 10
sum([1, 2, 3], 10) # 16 (with start value)

# Power
pow(2, 3)       # 8 (2 to the power of 3)
pow(2, 3, 5)    # 3 (2**3 % 5)

# Divmod (quotient and remainder)
divmod(17, 5)   # (3, 2) - 17//5=3, 17%5=2

# Other useful functions
bin(10)         # '0b1010' (binary representation)
hex(255)        # '0xff' (hexadecimal)
oct(8)          # '0o10' (octal)
```

---

## Enums (Enumerations)

### What are Enums?
- Enums create a set of symbolic names (constants) bound to unique values
- Useful for creating named constants that are more readable than raw values
- Prevent invalid values and provide better code documentation
- Immutable and iterable

### Basic Enum Usage
```python
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    PENDING = 2

# Accessing enum values
print(State.ACTIVE)         # State.ACTIVE
print(State.ACTIVE.name)    # 'ACTIVE'
print(State.ACTIVE.value)   # 1

# Comparison
current_state = State.ACTIVE
if current_state == State.ACTIVE:
    print("System is active")

# Iteration
for state in State:
    print(f"{state.name}: {state.value}")
```

### Advanced Enum Features
```python
from enum import Enum, auto, IntEnum, Flag, IntFlag

# Auto-generated values
class Color(Enum):
    RED = auto()      # 1
    GREEN = auto()    # 2
    BLUE = auto()     # 3

# String Enums
class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

# IntEnum - can be compared with integers
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.LOW == 1)  # True

# Flag Enum - for bitwise operations
class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

# Combine flags
full_access = Permission.READ | Permission.WRITE | Permission.EXECUTE
```

### Enum Best Practices
```python
# Functional API
Animal = Enum('Animal', 'CAT DOG BIRD')
# Equivalent to:
# class Animal(Enum):
#     CAT = 1
#     DOG = 2
#     BIRD = 3

# Unique decorator - ensures no duplicate values
from enum import unique

@unique
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    # DENIED = 3  # This would raise ValueError due to @unique
```

---

## User Input

### Getting User Input
```python
# input() always returns a string
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Converting input to other types
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Handling invalid input
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number")
    age = 0
```

---

## Control Statements

### Conditional Statements
```python
# Basic if statement
if condition:
    # execute if True
    pass

# if-else
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Multiple conditions
if age >= 18 and has_license:
    print("Can drive")

# Nested conditions
if weather == "sunny":
    if temperature > 25:
        print("Perfect beach day!")
    else:
        print("Nice day for a walk")
```

---

## Lists

### Theory and Characteristics
- **Ordered**: Items have a defined order that won't change
- **Mutable**: Can be changed after creation (add, remove, modify items)
- **Allow duplicates**: Same value can appear multiple times
- **Dynamic size**: Can grow or shrink during runtime
- **Indexed**: Access items using numeric indices (0-based)

### List Creation and Basic Operations
```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
nested = [[1, 2], [3, 4], [5, 6]]

# List constructor
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o']
range_list = list(range(5))  # [0, 1, 2, 3, 4]
```

### Accessing and Indexing
```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (0-based)
print(fruits[0])    # "apple"
print(fruits[1])    # "banana"

# Negative indexing
print(fruits[-1])   # "date" (last item)
print(fruits[-2])   # "cherry" (second to last)

# Slicing [start:end:step]
print(fruits[1:3])  # ["banana", "cherry"] (inclusive:exclusive)
print(fruits[:2])   # ["apple", "banana"] (from start)
print(fruits[2:])   # ["cherry", "date"] (to end)
print(fruits[::2])  # ["apple", "cherry"] (every 2nd item)
print(fruits[::-1]) # ["date", "cherry", "banana", "apple"] (reverse)
```

### List Methods and Operations
```python
numbers = [1, 2, 3]

# Check membership
print(2 in numbers)     # True
print(5 in numbers)     # False

# Length
print(len(numbers))     # 3

# Truthiness
print(bool([]))         # False (empty list)
print(bool([1]))        # True (non-empty list)

# Adding elements
numbers.append(4)       # [1, 2, 3, 4] - adds single item to end
numbers.extend([5, 6])  # [1, 2, 3, 4, 5, 6] - adds multiple items
numbers += [7, 8]       # [1, 2, 3, 4, 5, 6, 7, 8] - same as extend
numbers.insert(0, 0)    # [0, 1, 2, 3, 4, 5, 6, 7, 8] - insert at index

# Common mistake with extend
numbers = [1, 2, 3]
numbers.extend("45")    # [1, 2, 3, '4', '5'] - adds each character
numbers.extend([4, 5])  # [1, 2, 3, 4, 5] - correct way

# Removing elements
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)       # [1, 3, 2, 4] - removes first occurrence
popped = numbers.pop()  # [1, 3, 2] - removes and returns last item (4)
popped = numbers.pop(1) # [1, 2] - removes and returns item at index 1 (3)
del numbers[0]          # [2] - removes item at index

# Updating elements
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry" # ["apple", "blueberry", "cherry"]

# Adding multiple items in middle using slices
fruits[1:1] = ["kiwi", "mango"]  # Insert at index 1
# Result: ["apple", "kiwi", "mango", "blueberry", "cherry"]
```

### Sorting Lists

```python
# Sort modifies original list
items = ["Rogers", "bob", "Beau", "Quincy"]

# Basic sorting (case-sensitive: uppercase first)
items.sort()  # ['Beau', 'Quincy', 'Rogers', 'bob']

# Case-insensitive sorting
items = ["Rogers", "bob", "Beau", "Quincy"]
items.sort(key=str.lower)  # ['Beau', 'bob', 'Quincy', 'Rogers']
# key=str.lower applies str.lower() to each element for comparison only

# Reverse sorting
items.sort(reverse=True)
items.sort(key=str.lower, reverse=True)

# Creating a copy before sorting
items = ["Rogers", "bob", "Beau", "Quincy"]
items_copy = items[:]  # or items.copy() or list(items)
items.sort(key=str.lower)
print(items)        # Sorted
print(items_copy)   # Original order

# Sorting without modifying original (returns new list)
items = ["Rogers", "bob", "Beau", "Quincy"]
sorted_items = sorted(items, key=str.lower)
print(items)        # Original unchanged
print(sorted_items) # New sorted list

# Sorting numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()      # [1, 1, 2, 3, 4, 5, 6, 9]

# Custom sorting
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
people.sort(key=lambda x: x[1])  # Sort by age: [("Charlie", 20), ("Alice", 25), ("Bob", 30)]
```

---

## Tuples

### Theory and Characteristics
- **Immutable**: Cannot be changed after creation
- **Ordered**: Items have a defined order
- **Allow duplicates**: Same value can appear multiple times
- **Indexed**: Access items using numeric indices
- **Hashable**: Can be used as dictionary keys (if all elements are hashable)

### Tuple Operations
```python
# Creating tuples
coordinates = (3, 5)
colors = ("red", "green", "blue")
single = (42,)  # Note the comma for single-item tuple
empty = ()

# Tuple constructor
numbers = tuple([1, 2, 3])  # (1, 2, 3)
letters = tuple("hello")    # ('h', 'e', 'l', 'l', 'o')

# Accessing elements (same as lists)
print(colors[0])     # "red"
print(colors[-1])    # "blue"
print(colors[1:3])   # ("green", "blue")

# Tuple methods
fruits = ("apple", "banana", "cherry", "banana")
print(fruits.index("banana"))  # 1 (first occurrence)
print(fruits.count("banana"))  # 2

# Common operations
print(len(fruits))       # 4
print("apple" in fruits) # True

# Sorting (creates new tuple)
numbers = (3, 1, 4, 1, 5)
sorted_tuple = tuple(sorted(numbers))  # (1, 1, 3, 4, 5)

# Concatenation (creates new tuple)
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)

# Tuple unpacking
point = (10, 20)
x, y = point  # x=10, y=20

# Multiple assignment
a, b, c = (1, 2, 3)
```

---

## Dictionaries

### Theory and Characteristics
- **Key-Value pairs**: Data stored as associations
- **Unordered**: No guaranteed order (Python 3.7+ maintains insertion order)
- **Mutable**: Can be changed after creation
- **Keys must be immutable**: strings, numbers, tuples (but not lists)
- **Values can be anything**: any data type
- **No duplicate keys**: Each key is unique

### Dictionary Operations
```python
# Creating dictionaries
person = {"name": "John", "age": 30, "city": "New York"}
empty_dict = {}
grades = dict(math=85, science=92, english=78)

# Accessing elements
print(person["name"])        # "John"
print(person.get("age"))     # 30
print(person.get("height", "Unknown"))  # "Unknown" (default value)

# Adding/updating key-value pairs
person["email"] = "john@email.com"  # Add new key
person["age"] = 31                  # Update existing key
person.update({"phone": "123-456", "age": 32})  # Update multiple

# Removing items
person.pop("email")          # Remove and return value
person.pop("height", None)   # Remove with default if key doesn't exist
del person["phone"]          # Remove key-value pair
person.popitem()             # Remove and return last inserted item

# Dictionary methods
person = {"name": "John", "age": 30, "city": "New York"}

# Check if key exists
print("name" in person)      # True
print("height" in person)    # False

# Get all keys, values, or items
keys = person.keys()         # dict_keys(['name', 'age', 'city'])
values = person.values()     # dict_values(['John', 30, 'New York'])
items = person.items()       # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Convert to lists
key_list = list(person.keys())
value_list = list(person.values())
item_list = list(person.items())

# Length
print(len(person))           # 3

# Copying dictionaries
person_copy = person.copy()         # Shallow copy
person_copy2 = dict(person)         # Another way to copy
person_copy3 = {**person}           # Using dictionary unpacking

# Clear all items
person.clear()               # {}
```

### Advanced Dictionary Operations
```python
# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Nested dictionaries
students = {
    "john": {"math": 85, "science": 92},
    "jane": {"math": 78, "science": 88}
}

# Accessing nested values
print(students["john"]["math"])  # 85

# Default dictionaries
from collections import defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")  # Automatically creates list if key doesn't exist
```

---

## Sets

### Theory and Characteristics
- **Unordered**: No defined order of elements
- **Mutable**: Can add/remove elements (regular sets)
- **No duplicates**: Each element appears only once
- **Elements must be immutable**: strings, numbers, tuples
- **Fast membership testing**: Very efficient for checking if item exists

### Set Operations
```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3} - duplicates removed
empty_set = set()  # Note: {} creates an empty dict, not set

# Set from string
letters = set("hello")  # {'h', 'e', 'l', 'o'} - duplicates removed

# Basic operations
fruits.add("orange")           # Add single item
fruits.update(["kiwi", "mango"])  # Add multiple items
fruits.remove("banana")        # Remove item (KeyError if not found)
fruits.discard("grape")        # Remove item (no error if not found)
popped = fruits.pop()          # Remove and return arbitrary item

# Membership and length
print("apple" in fruits)       # True
print(len(fruits))             # Number of items

# Convert to list
fruit_list = list(fruits)      # Convert set to list
```

### Set Mathematical Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all unique elements from both sets)
union = set1 | set2              # {1, 2, 3, 4, 5, 6}
union = set1.union(set2)         # Same result

# Intersection (common elements)
intersection = set1 & set2       # {3, 4}
intersection = set1.intersection(set2)  # Same result

# Difference (elements in set1 but not in set2)
difference = set1 - set2         # {1, 2}
difference = set1.difference(set2)  # Same result

# Symmetric difference (elements in either set, but not both)
sym_diff = set1 ^ set2           # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)  # Same result

# Subset and superset relationships
set_a = {1, 2}
set_b = {1, 2, 3, 4}

print(set_a < set_b)             # True (set_a is proper subset of set_b)
print(set_a <= set_b)            # True (set_a is subset of set_b)
print(set_b > set_a)             # True (set_b is proper superset of set_a)
print(set_b >= set_a)            # True (set_b is superset of set_a)

# Check if sets are disjoint (no common elements)
set_c = {7, 8, 9}
print(set_a.isdisjoint(set_c))   # True
```

### Frozen Sets (Immutable Sets)
```python
# Frozen sets are immutable versions of sets
frozen = frozenset([1, 2, 3, 4])
frozen2 = frozenset("hello")     # frozenset({'h', 'e', 'l', 'o'})

# Can be used as dictionary keys (since they're hashable)
set_counts = {
    frozenset([1, 2]): "small",
    frozenset([1, 2, 3, 4]): "large"
}

# All set operations work, but no modification methods
print(len(frozen))               # 4
print(2 in frozen)               # True
# frozen.add(5)                  # AttributeError - not supported
```

### Set Comprehensions
```python
# Set comprehension
squares = {x**2 for x in range(1, 6)}  # {1, 4, 9, 16, 25}

# Conditional set comprehension
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}  # {4, 16, 36, 64, 100}
```

