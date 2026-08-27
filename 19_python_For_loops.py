# 🔁 Python For Loops

A `for` loop is used to **iterate over a sequence or iterable**, such as a list, tuple, string, dictionary, set, or range.

It is one of the most commonly used loops in Python.

> **Syntax:** `for variable in iterable:`

---

## 📌 Table of Contents

- [What is a For Loop?](#-what-is-a-for-loop)
- [Basic Syntax](#-basic-syntax)
- [Simple Example](#-simple-example)
- [How For Loop Works](#-how-for-loop-works)
- [Looping Through a List](#-looping-through-a-list)
- [Looping Through a Tuple](#-looping-through-a-tuple)
- [Looping Through a String](#-looping-through-a-string)
- [Using `range()`](#-using-range)
- [Range with Start and Stop](#-range-with-start-and-stop)
- [Range with Step](#-range-with-step)
- [Reverse Loop](#-reverse-loop)
- [Using `break`](#-using-break)
- [Using `continue`](#-using-continue)
- [Using `else`](#-using-else)
- [Nested For Loops](#-nested-for-loops)
- [For Loop with Dictionaries](#-for-loop-with-dictionaries)
- [For Loop with Sets](#-for-loop-with-sets)
- [Using `enumerate()`](#-using-enumerate)
- [Using `zip()`](#-using-zip)
- [List Comprehension](#-list-comprehension)
- [Real-World Examples](#-real-world-examples)
- [Common Mistakes](#-common-mistakes)
- [For vs While Loop](#-for-vs-while-loop)
- [Quick Reference](#-quick-reference)
- [Key Takeaways](#-key-takeaways)

---

# 🔹 What is a For Loop?

A `for` loop repeats a block of code for every item in an iterable.

An iterable can be:

- List
- Tuple
- String
- Dictionary
- Set
- Range
- Other iterable objects

Example:

    fruits = ["Apple", "Banana", "Mango"]

    for fruit in fruits:
        print(fruit)

Output:

    Apple
    Banana
    Mango

The loop automatically moves from one item to the next.

---

# 🔹 Basic Syntax

    for variable in iterable:
        # code to execute

Example:

    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        print(number)

Output:

    1
    2
    3
    4
    5

Here:

    number → loop variable
    numbers → iterable

---

# 🔹 Simple Example

    for i in range(5):
        print(i)

Output:

    0
    1
    2
    3
    4

By default, `range(5)` starts from `0` and stops before `5`.

---

# 🔹 How For Loop Works

Consider:

    fruits = ["Apple", "Banana", "Mango"]

    for fruit in fruits:
        print(fruit)

Python performs the following:

    First iteration → fruit = "Apple"
    Second iteration → fruit = "Banana"
    Third iteration → fruit = "Mango"

Output:

    Apple
    Banana
    Mango

After all items are processed, the loop ends automatically.

---

# 🔹 Looping Through a List

You can directly iterate through a list.

    numbers = [10, 20, 30, 40]

    for number in numbers:
        print(number)

Output:

    10
    20
    30
    40

This is cleaner than manually accessing indexes.

---

# 🔹 Looping Through a Tuple

A `for` loop can iterate through tuple elements.

    colors = ("Red", "Green", "Blue")

    for color in colors:
        print(color)

Output:

    Red
    Green
    Blue

---

# 🔹 Looping Through a String

Strings are iterable, so you can loop through each character.

    word = "Python"

    for character in word:
        print(character)

Output:

    P
    y
    t
    h
    o
    n

---

# 🔹 Using `range()`

`range()` is commonly used with `for` loops.

    for number in range(5):
        print(number)

Output:

    0
    1
    2
    3
    4

### Important

`range(5)` generates numbers from `0` up to, but not including, `5`.

---

# 🔹 Range with Start and Stop

You can specify where the range starts and stops.

    for number in range(1, 6):
        print(number)

Output:

    1
    2
    3
    4
    5

Syntax:

    range(start, stop)

The `stop` value is not included.

---

# 🔹 Range with Step

You can specify how much the number should increase each time.

    for number in range(0, 11, 2):
        print(number)

Output:

    0
    2
    4
    6
    8
    10

Syntax:

    range(start, stop, step)

Here:

    start = 0
    stop = 11
    step = 2

---

# 🔹 Reverse Loop

You can use a negative step to count backwards.

    for number in range(5, 0, -1):
        print(number)

Output:

    5
    4
    3
    2
    1

This is useful for countdowns.

---

# 🔹 `break` Statement

The `break` statement immediately stops the loop.

    for number in range(1, 11):
        print(number)

        if number == 5:
            break

Output:

    1
    2
    3
    4
    5

When `number` becomes `5`, the loop terminates.

---

# 🔹 `continue` Statement

The `continue` statement skips the current iteration and moves to the next one.

    for number in range(1, 6):

        if number == 3:
            continue

        print(number)

Output:

    1
    2
    4
    5

When `number` is `3`, Python skips that iteration.

---

# 🔹 `else` with For Loop

A `for` loop can have an `else` block.

The `else` block runs when the loop finishes normally.

    for number in range(3):
        print(number)
    else:
        print("Loop completed")

Output:

    0
    1
    2
    Loop completed

### Important

If the loop is stopped using `break`, the `else` block does not execute.

    for number in range(5):
        print(number)

        if number == 2:
            break
    else:
        print("Loop completed")

Output:

    0
    1
    2

The `else` block is skipped because `break` stopped the loop.

---

# 🔹 Nested For Loops

A `for` loop can contain another `for` loop.

This is called a **nested loop**.

    for i in range(1, 4):
        for j in range(1, 3):
            print(f"i={i}, j={j}")

Output:

    i=1, j=1
    i=1, j=2
    i=2, j=1
    i=2, j=2
    i=3, j=1
    i=3, j=2

The inner loop completes all its iterations for every iteration of the outer loop.

---

# 🔹 For Loop with Dictionaries

You can loop through dictionary keys.

    user = {
        "name": "Hadi",
        "age": 20,
        "city": "Islamabad"
    }

    for key in user:
        print(key)

Output:

    name
    age
    city

---

## 🔸 Loop Through Dictionary Values

Use `.values()` to get values.

    user = {
        "name": "Hadi",
        "age": 20,
        "city": "Islamabad"
    }

    for value in user.values():
        print(value)

Output:

    Hadi
    20
    Islamabad

---

## 🔸 Loop Through Keys and Values

Use `.items()` to get both keys and values.

    user = {
        "name": "Hadi",
        "age": 20
    }

    for key, value in user.items():
        print(key, value)

Output:

    name Hadi
    age 20

---

# 🔹 For Loop with Sets

Sets are also iterable.

    fruits = {"Apple", "Banana", "Mango"}

    for fruit in fruits:
        print(fruit)

Output:

    Apple
    Banana
    Mango

> ⚠️ Sets are unordered, so the output order may be different.

---

# 🔹 Using `enumerate()`

`enumerate()` allows you to get both the index and the value while looping.

    fruits = ["Apple", "Banana", "Mango"]

    for index, fruit in enumerate(fruits):
        print(index, fruit)

Output:

    0 Apple
    1 Banana
    2 Mango

You can also start the index from another number.

    fruits = ["Apple", "Banana", "Mango"]

    for index, fruit in enumerate(fruits, start=1):
        print(index, fruit)

Output:

    1 Apple
    2 Banana
    3 Mango

---

# 🔹 Using `zip()`

`zip()` allows you to iterate over multiple sequences at the same time.

    names = ["Hadi", "Ali", "Ahmed"]
    ages = [20, 21, 22]

    for name, age in zip(names, ages):
        print(name, age)

Output:

    Hadi 20
    Ali 21
    Ahmed 22

`zip()` pairs the corresponding elements.

---

# 🔹 List Comprehension

List comprehension provides a short way to create a list using a `for` loop.

Traditional approach:

    numbers = [1, 2, 3, 4, 5]
    squares = []

    for number in numbers:
        squares.append(number ** 2)

    print(squares)

Output:

    [1, 4, 9, 16, 25]

Using list comprehension:

    numbers = [1, 2, 3, 4, 5]

    squares = [number ** 2 for number in numbers]

    print(squares)

Output:

    [1, 4, 9, 16, 25]

---

# 🔹 For Loop with Conditions

You can use `if` inside a `for` loop.

    numbers = [1, 2, 3, 4, 5, 6]

    for number in numbers:
        if number % 2 == 0:
            print(number)

Output:

    2
    4
    6

This example prints only even numbers.

---

# 🔹 For Loop with `if-else`

You can also use `if-else` inside a loop.

    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        if number % 2 == 0:
            print(number, "Even")
        else:
            print(number, "Odd")

Output:

    1 Odd
    2 Even
    3 Odd
    4 Even
    5 Odd

---

# 🔥 Real-World Example: Shopping Cart

    cart = ["Laptop", "Mouse", "Keyboard"]

    for item in cart:
        print(f"Added to cart: {item}")

Output:

    Added to cart: Laptop
    Added to cart: Mouse
    Added to cart: Keyboard

---

# 🔥 Real-World Example: Calculate Total

    prices = [100, 250, 50, 300]

    total = 0

    for price in prices:
        total += price

    print(f"Total: ${total}")

Output:

    Total: $700

---

# 🔥 Real-World Example: Find Maximum Number

    numbers = [10, 45, 23, 89, 12]

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print("Maximum:", maximum)

Output:

    Maximum: 89

---

# 🔥 Real-World Example: Count Vowels

    word = "programming"

    vowels = "aeiou"
    count = 0

    for character in word:
        if character in vowels:
            count += 1

    print("Vowels:", count)

Output:

    Vowels: 3

---

# 🔥 Real-World Example: Password Validation

    password = "Python123"

    has_digit = False

    for character in password:
        if character.isdigit():
            has_digit = True
            break

    if has_digit:
        print("Password contains a number")
    else:
        print("Password must contain a number")

Output:

    Password contains a number

---

# ⚠️ Common Mistakes

## 1. Incorrect Indentation

❌ Wrong:

    for number in range(5):
    print(number)

✅ Correct:

    for number in range(5):
        print(number)

Python uses indentation to define the loop body.

---

## 2. Forgetting That `range()` Excludes the Stop Value

    for number in range(1, 5):
        print(number)

Output:

    1
    2
    3
    4

`5` is not included.

---

## 3. Modifying a List While Iterating

Avoid changing the size of a list while directly looping through it.

Instead, create a separate list or use another approach.

Example:

    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        print(number)

---

## 4. Using the Wrong Variable

Make sure the loop variable is used correctly.

    fruits = ["Apple", "Banana", "Mango"]

    for fruit in fruits:
        print(fruit)

Here, `fruit` represents the current item.

---

# 🔹 For vs While Loop

Both loops are used for repetition, but they work differently.

| Feature | `for` | `while` |
|---|---|---|
| Iterate over sequences | ✅ Excellent | ✅ Possible |
| Known number of iterations | ✅ Excellent | ✅ Possible |
| Unknown number of iterations | ⚠️ Less common | ✅ Excellent |
| Lists / tuples / strings | ✅ Excellent | ✅ Possible |
| User input loops | ⚠️ Possible | ✅ Excellent |
| Infinite loop | ⚠️ Less common | ✅ Easy |
| Automatic iteration | ✅ Yes | ❌ Manual |

### Use `for` when:

You want to iterate over a sequence or a known range.

    for number in range(5):
        print(number)

### Use `while` when:

You want to continue until a condition changes.

    while password != "python123":
        password = input("Enter password: ")

---

# 📚 Quick Reference

| Syntax | Purpose |
|---|---|
| `for x in iterable:` | Iterate over an iterable |
| `range(5)` | Numbers from `0` to `4` |
| `range(1, 6)` | Numbers from `1` to `5` |
| `range(0, 10, 2)` | Numbers with step `2` |
| `break` | Stop the loop |
| `continue` | Skip current iteration |
| `else` | Run after normal loop completion |
| `enumerate()` | Get index and value |
| `zip()` | Iterate over multiple sequences |
| `.keys()` | Iterate over dictionary keys |
| `.values()` | Iterate over dictionary values |
| `.items()` | Iterate over dictionary keys and values |

---

# 🧠 Key Takeaways

- A `for` loop is used to iterate over an iterable.
- It can work with lists, tuples, strings, sets, dictionaries, and ranges.
- The loop variable represents the current item.
- `range()` is commonly used for generating numbers.
- `break` stops the loop immediately.
- `continue` skips the current iteration.
- `else` runs when the loop finishes normally.
- Nested `for` loops are possible.
- `enumerate()` provides both index and value.
- `zip()` allows you to loop through multiple sequences together.
- List comprehensions provide a shorter way to create lists.
- `for` loops are usually preferred when iterating over a known sequence.
- `while` loops are better when repetition depends mainly on a condition.

---

# ⭐ Remember

### `for` loop

Use when you want to iterate over a sequence or a known range.

    for item in iterable:
        # code

### `while` loop

Use when you want to repeat something until a condition changes.

    while condition:
        # code

---

# 🚀 Final Example

    students = ["Hadi", "Ali", "Ahmed"]

    for student in students:
        print(f"Welcome, {student}!")

Output:

    Welcome, Hadi!
    Welcome, Ali!
    Welcome, Ahmed!

> 💡 **Tip:** Use `for` loops when you know what you want to iterate over. Python's `for` loop automatically handles moving from one item to the next, making it cleaner and safer than manually managing an index.