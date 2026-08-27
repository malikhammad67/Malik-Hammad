# 🔄 Python While Loops

A `while` loop is used to repeat a block of code as long as a condition is `True`.

It is useful when you don't know exactly how many times a loop should run.

> Syntax: `while condition:`

---

## 📌 Table of Contents

- What is a While Loop?
- Basic Syntax
- Simple Example
- How While Loop Works
- While Loop with Counter
- Counting Backwards
- Using User Input
- Infinite While Loop
- break Statement
- continue Statement
- else with While Loop
- Nested While Loops
- While Loop with Lists
- While Loop with Strings
- While Loop for Validation
- Multiple Conditions
- Real-World Examples
- Common Mistakes
- While vs For Loop
- Quick Reference
- Key Takeaways

---

# 🔹 What is a While Loop?

A `while` loop repeatedly executes a block of code while a given condition remains `True`.

Example:

    count = 1

    while count <= 5:
        print(count)
        count += 1

Output:

    1
    2
    3
    4
    5

The loop stops when `count <= 5` becomes `False`.

---

# 🔹 Basic Syntax

    while condition:
        # code to execute

Example:

    number = 1

    while number <= 5:
        print(number)
        number += 1

The condition is checked before every iteration.

---

# 🔹 Simple Example

    count = 1

    while count <= 3:
        print("Hello")
        count += 1

Output:

    Hello
    Hello
    Hello

The loop runs three times because the condition is `True` for `1`, `2`, and `3`.

---

# 🔹 How While Loop Works

Consider this example:

    count = 1

    while count <= 3:
        print(count)
        count += 1

### Step 1

`count = 1`

Check:

    1 <= 3

Result:

    True

Print:

    1

Then:

    count = 2

### Step 2

Check:

    2 <= 3

Result:

    True

Print:

    2

Then:

    count = 3

### Step 3

Check:

    3 <= 3

Result:

    True

Print:

    3

Then:

    count = 4

### Step 4

Check:

    4 <= 3

Result:

    False

The loop stops.

Output:

    1
    2
    3

---

# 🔹 While Loop with Counter

A counter is commonly used with a `while` loop.

    count = 1

    while count <= 5:
        print(f"Count: {count}")
        count += 1

Output:

    Count: 1
    Count: 2
    Count: 3
    Count: 4
    Count: 5

### Important

Always make sure the counter eventually changes.

    count += 1

Without changing the counter, the loop may become infinite.

---

# 🔹 Counting Backwards

You can also decrease the counter.

    count = 5

    while count >= 1:
        print(count)
        count -= 1

Output:

    5
    4
    3
    2
    1

This is useful for countdowns.

---

# 🔹 Using User Input

A `while` loop can continue running until the user enters a specific value.

    password = ""

    while password != "python123":
        password = input("Enter password: ")

    print("Access granted!")

The loop continues until the correct password is entered.

---

# 🔹 Infinite While Loop

An infinite loop continues forever unless something stops it.

Example:

    while True:
        print("This keeps running")

Since `True` is always true, the loop never naturally ends.

Usually, an infinite loop is stopped using `break`.

    while True:
        command = input("Enter command: ")

        if command == "exit":
            break

        print(f"You entered: {command}")

The loop stops when the user enters `"exit"`.

---

# 🔹 `break` Statement

The `break` statement immediately stops the loop.

    number = 1

    while number <= 10:
        print(number)

        if number == 5:
            break

        number += 1

Output:

    1
    2
    3
    4
    5

When `number == 5`, `break` terminates the loop.

---

# 🔹 `continue` Statement

The `continue` statement skips the current iteration and moves to the next iteration.

Example:

    number = 0

    while number < 5:
        number += 1

        if number == 3:
            continue

        print(number)

Output:

    1
    2
    4
    5

When `number` becomes `3`, `continue` skips the `print()` statement.

---

# 🔹 `else` with While Loop

A `while` loop can have an `else` block.

The `else` block runs when the loop finishes normally.

    count = 1

    while count <= 3:
        print(count)
        count += 1
    else:
        print("Loop completed")

Output:

    1
    2
    3
    Loop completed

### Important

If the loop is terminated using `break`, the `else` block does not run.

    count = 1

    while count <= 5:
        print(count)

        if count == 3:
            break

        count += 1
    else:
        print("Loop completed")

Output:

    1
    2
    3

The `else` block is skipped because `break` stopped the loop.

---

# 🔹 Nested While Loops

A `while` loop can contain another `while` loop.

This is called a nested loop.

    outer = 1

    while outer <= 3:
        inner = 1

        while inner <= 2:
            print(f"Outer: {outer}, Inner: {inner}")
            inner += 1

        outer += 1

Output:

    Outer: 1, Inner: 1
    Outer: 1, Inner: 2
    Outer: 2, Inner: 1
    Outer: 2, Inner: 2
    Outer: 3, Inner: 1
    Outer: 3, Inner: 2

The inner loop completes all its iterations for each iteration of the outer loop.

---

# 🔹 While Loop with Lists

You can use a `while` loop to iterate through a list.

    fruits = ["Apple", "Banana", "Mango"]

    index = 0

    while index < len(fruits):
        print(fruits[index])
        index += 1

Output:

    Apple
    Banana
    Mango

Here, `index` is used to access each list element.

---

# 🔹 While Loop with Strings

You can also use a `while` loop to process characters in a string.

    word = "Python"

    index = 0

    while index < len(word):
        print(word[index])
        index += 1

Output:

    P
    y
    t
    h
    o
    n

---

# 🔹 While Loop for Validation

A common use of `while` loops is validating user input.

    age = int(input("Enter your age: "))

    while age < 0:
        print("Age cannot be negative.")
        age = int(input("Enter your age: "))

    print(f"Your age is {age}")

The loop keeps asking for input until a valid value is provided.

---

# 🔹 Multiple Conditions

You can use logical operators with a `while` loop.

    number = 1

    while number <= 10 and number != 5:
        print(number)
        number += 1

Output:

    1
    2
    3
    4

The loop stops when either condition becomes `False`.

---

# 🔹 Using `not`

You can also use the `not` operator.

    logged_in = False

    while not logged_in:
        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "1234":
            logged_in = True

    print("Login successful!")

The loop continues while `logged_in` is `False`.

---

# 🔥 Real-World Example: Login System

    correct_password = "python123"
    attempts = 0

    while attempts < 3:
        password = input("Enter password: ")

        if password == correct_password:
            print("Login successful!")
            break

        attempts += 1
        print("Incorrect password.")

    if attempts == 3:
        print("Too many attempts.")

This limits the user to three attempts.

---

# 🔥 Real-World Example: ATM Menu

    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Balance: $1000")

        elif choice == "2":
            print("Withdrawal selected")

        elif choice == "3":
            print("Deposit selected")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

The loop keeps showing the menu until the user chooses `"4"`.

---

# 🔥 Real-World Example: Number Guessing Game

    secret_number = 7

    while True:
        guess = int(input("Guess the number: "))

        if guess == secret_number:
            print("Correct!")
            break

        elif guess < secret_number:
            print("Too low!")

        else:
            print("Too high!")

The loop continues until the user guesses the correct number.

---

# 🔥 Real-World Example: Sum Until Zero

You can use a `while` loop to keep accepting numbers until the user enters `0`.

    total = 0

    while True:
        number = int(input("Enter a number (0 to stop): "))

        if number == 0:
            break

        total += number

    print(f"Total: {total}")

Example:

    Enter a number: 10
    Enter a number: 20
    Enter a number: 30
    Enter a number: 0

Output:

    Total: 60

---

# ⚠️ Common Mistakes

## 1. Forgetting to Update the Variable

Wrong:

    count = 1

    while count <= 5:
        print(count)

This creates an infinite loop because `count` never changes.

Correct:

    count = 1

    while count <= 5:
        print(count)
        count += 1

---

## 2. Incorrect Condition

Make sure your condition eventually becomes `False`.

Example:

    count = 1

    while count <= 5:
        print(count)
        count += 1

The loop eventually stops when:

    count = 6

---

## 3. Accidentally Creating an Infinite Loop

Be careful with conditions like:

    while True:
        print("Hello")

This will continue forever unless you use `break`.

---

## 4. Forgetting `break`

When using `while True`, make sure there is a condition that can stop the loop.

    while True:
        command = input("Enter command: ")

        if command == "exit":
            break

---

# 🔹 While vs For Loop

Both `while` and `for` loops are used for repetition, but they are useful in different situations.

| Feature | `while` | `for` |
|---|---|---|
| Condition-based repetition | ✅ Excellent | ⚠️ Less common |
| Known number of iterations | ⚠️ Possible | ✅ Excellent |
| Unknown number of iterations | ✅ Excellent | ⚠️ Less convenient |
| Iterating over lists | ✅ Possible | ✅ Excellent |
| Infinite loop | ✅ Easy | ⚠️ Less common |
| User input loops | ✅ Excellent | ⚠️ Less convenient |

### Use `for` when:

You know what you want to iterate over.

    for fruit in fruits:
        print(fruit)

### Use `while` when:

You want to continue until a condition changes.

    while password != "python123":
        password = input("Enter password: ")

---

# 📚 Quick Reference

| Syntax | Purpose |
|---|---|
| `while condition:` | Repeat while condition is `True` |
| `break` | Stop the loop immediately |
| `continue` | Skip current iteration |
| `while True:` | Create an intentional infinite loop |
| `while ... else:` | Run `else` after normal completion |
| `+= 1` | Increase counter |
| `-= 1` | Decrease counter |
| `len()` | Get length of sequence |
| `and` | Require multiple conditions |
| `or` | Allow either condition |
| `not` | Reverse a condition |

---

# 🧠 Key Takeaways

- A `while` loop repeats code while a condition is `True`.
- The condition is checked before every iteration.
- The loop stops when the condition becomes `False`.
- Always make sure the condition can eventually become `False`.
- `break` immediately terminates the loop.
- `continue` skips the current iteration.
- `while True` creates an infinite loop.
- Use `break` to exit an intentional infinite loop.
- A `while` loop can have an `else` block.
- The `else` block runs when the loop finishes normally.
- Nested `while` loops are possible.
- `while` loops are useful for user input and validation.
- Use `for` loops when iterating over a known sequence.
- Use `while` loops when repetition depends mainly on a condition.

---

# ⭐ Remember

### `for` loop

Use when you know what you want to iterate over.

### `while` loop

Use when you want to repeat something until a condition changes.

Basic structure:

    while condition:
        # code

Example:

    count = 1

    while count <= 5:
        print(count)
        count += 1

Output:

    1
    2
    3
    4
    5

> 💡 Tip: The most important thing to remember with `while` loops is to make sure something inside the loop changes the condition. Otherwise, you may accidentally create an infinite loop.