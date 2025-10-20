# 🐍 Python Fundamentals – Explained with Examples

A clean, beginner-friendly guide covering Python basics: variables, data types, type casting, operators, and strings.

---

## 📚 Table of Contents

- [📦 Data Types and Printing](#data-types-and-printing)
- [➕ Operators in Python](#operators-in-python)
- [💬 Working with Strings](#working-with-strings)
- [🔄 Type Casting (Conversions)](#type-casting-(conversions))
- [🧠 Variables and Input Handling](#variables-and-input-handling)

---

## 📦 Data Types and Printing

Python supports several built-in data types like `int`, `float`, `bool`, and `str`. You can inspect them using the `type()` function.

### 🔹 Example Code:

```python
# int
# float
# string 
# bool

print(type(10))       #=> Integer
print(type(True))     #=> Boolean


print('ba',end = '#')
print("hello")
print('b','t',sep='$')
```

### ⚙️ Output:

```
<class 'int'>

<class 'bool'>

ba#hello

b$t
```

### 💬 Explanation:

- Prints examples of core data types.
- Use `type()` to check variable types at runtime.

> 💡 **Tip:** Use `isinstance(var, type)` for better type checking.

---

## ➕ Operators in Python

Operators let you perform mathematical and logical operations. They are the backbone of any computation.

### 🔹 Example Code:

```python
#Arithmatic operator


#ADDITION
print("ADDITION")
print(2+3)
print(2+3.4)
print(True+False)
print("Shivam "+"Varshney")
print("---------\n")

#Substraction
print("Substraction")
print(2-3)
print(2-3.4)
print(True-False)
# print("Shivam "-"Varshney")           #error
print("---------\n")

#Multiplication
print("Multiplication")
print(2*3)
print(2*3.4)
print(True*False)
# print("Shivam "*"Varshney")           #error
print("hello "*3)
print("---------\n")


#Division
print("Division")
print(3/2)
print(2.5/5.0)
print(1/3)
print("---------\n")


#Floor division
print("Floor division")
print(3//2)
print("---------\n")



#Remainder
print("Remainder")
print(3%2)
print(2.5%5.0)
print(1%3)
print("---------\n")


#Exponentiation
print("Exponentiation")
print(3**2)
print(2.5**5.0)
print(2.5**1)
print("---------\n")


#abs
print("abs")
print(abs(-35))
print("---------\n")



#round
print("round")
print(round(1.2383434,2))
print("---------\n")


#Comparision operator <, >, <=, >=, ==, !=


#Logical operator and, or , not
```

### ⚙️ Output:

```
ADDITION

5

5.4

1

Shivam Varshney

---------



Substraction

-1

-1.4

1

---------



Multiplication

6

6.8

0

hello hello hello 

---------



Division

1.5

0.5

0.3333333333333333

---------



Floor division

1

---------



Remainder

1

2.5

1

---------



Exponentiation

9

97.65625

2.5

---------



abs

35

---------



round

1.24

---------
```

### 💬 Explanation:

- Demonstrates arithmetic and logical operations.
- `//` gives floor division, `**` gives exponentiation.
- `/` performs true division returning float.

> 💡 **Tip:** Use parentheses to make complex expressions clearer.

---

## 💬 Working with Strings

Strings are sequences of characters. You can manipulate them easily using built-in string methods.

### 🔹 Example Code:

```python
#string

#concatenation
print("\n==concatenation=============")
print("a"+"b")

#string replication 
print("\n==string replication========")
print("abc"*20)

#string length
print("\n==length====================")
print(len("abc"))

#string slicing
print("\n==string slicing============")
arr = "shivam varshney"
print(arr[0:6:2])#start:end:steps 
print(arr[-6:-1])

#string case conversion
print("\nstring case conversion======")
print("Shivam".lower())
print("shivam".upper())

#string stripping
print("\nstring stripping============")
print("    shivam  varshney        ".strip())

#string replacing
print("\nstring replacing============")
print('shivam'.replace('h','v'))

#string count
print("\nstring count================")
print("shivam".count('s'))

#string find
print("\nstring find=================")
print("shivam".find("iv"))

#string check
print("\nstring check================")
print("shivam".islower())
print("ABC".isupper())
print("12a".isdigit())
print("hsdkShhsHSu)".isalpha())


#string capitalization
print("\nstring capitalization=======")
print("shivam varshney".capitalize())
print("shivam varshney".title())


#check for start end end
print("\nstart and end===============")
print("Shivam".startswith("Shi"))
print("Varshney".endswith("ney"))

#allignment
print("\nallignment==================")
print("Shivam".center(20,"?"))
print("Shivam".ljust(20,'?'))
print("Shivam".rjust(20,'?'))

#joining strings
print("\njoining strings=============")
s = "==>"
k = s.join(['a','b','c'])
print(k)
```

### ⚙️ Output:

```


==concatenation=============

ab



==string replication========

abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc



==length====================

3



==string slicing============

sia

rshne



string case conversion======

shivam

SHIVAM



string stripping============

shivam  varshney



string replacing============

svivam



string count================

1



string find=================

2



string check================

True

True

False

False



string capitalization=======

Shivam varshney

Shivam Varshney



start and end===============

True

True



allignment==================

???????Shivam???????

Shivam??????????????

??????????????Shivam



joining strings=============

a==>b==>c
```

### 💬 Explanation:

- Shows how to modify and format strings.
- Common methods: `.lower()`, `.upper()`, `.title()`, `.split()`, `.join()`.
- Strings are immutable, so methods return new strings.

> 💡 **Tip:** Use f-strings for efficient string formatting.

---

## 🔄 Type Casting (Conversions)

Type casting means converting one data type to another. For example, changing a string `'5'` into an integer `5`.

### 🔹 Example Code:

```python
#int
print("\nint --------------------------")
print(int(2.14))
print(int('199'))

#float
print("\nfloat ------------------------")
print(float('12.22'))

#bool
print("\nbool -------------------------")
print(bool(199))
print(bool(0))
print(bool(-100203))
print(bool([]))

#string
print("\nstring -----------------------")
print(str(123))
print(str(10.2))
print(str(True))


#Execptions
print("\n------------------------------")
# print(int('2.34'))              #wrong way 
print(int(float('2.34')))         #correct way
```

### ⚙️ Output:

```


int --------------------------

2

199



float ------------------------

12.22



bool -------------------------

True

False

True

False



string -----------------------

123

10.2

True



------------------------------

2
```

### 💬 Explanation:

- Demonstrates converting between types using `int()`, `float()`, `str()`, and `bool()`.
- Be cautious: invalid conversions (e.g., `int('abc')`) cause errors.

> 💡 **Tip:** Always check input type before casting to avoid `ValueError`.

---

## 🧠 Variables and Input Handling

Variables are names that store values. In Python, you don’t need to declare the type — it’s inferred automatically.

### 🔹 Example Code:

```python
a = 1
b = 2
print(a*b)

x = y = z = 0
print(x,y,z,sep=" | ")
m,n,o = 1,2,3
print(m,n,o,sep='/')


#taking input from user
n = int(input("n = "))
print("n = ",n,sep="")
n += 100 # same for *=,-=,/=,//=
print("n = ",n,sep="")
```

### ⚙️ Output:

```
[Skipped: this example requires user input()]
```
---
