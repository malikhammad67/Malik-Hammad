# 🐍 Python If-Else

**Conditional statements** allow a Python program to make decisions based on whether a condition is `True` or `False`.

For example:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

The `if` statement checks the condition. If the condition is `True`, the indented code runs.

---

## 📌 Table of Contents

* [What Are Conditional Statements?](#-what-are-conditional-statements)
* [if Statement](#-if-statement)
* [if Syntax](#-if-syntax)
* [Comparison Operators](#-comparison-operators)
* [if-else Statement](#-if-else-statement)
* [if-elif-else](#-if-elif-else)
* [Multiple Conditions](#-multiple-conditions)
* [Logical Operators](#-logical-operators)
* [Nested if Statements](#-nested-if-statements)
* [if With Strings](#-if-with-strings)
* [if With Lists](#-if-with-lists)
* [if With Sets](#-if-with-sets)
* [if With Dictionaries](#-if-with-dictionaries)
* [Membership Operators](#-membership-operators)
* [Identity Operators](#-identity-operators)
* [Truthy and Falsy Values](#-truthy-and-falsy-values)
* [Ternary Operator](#-ternary-operator)
* [Conditional Expressions](#-conditional-expressions)
* [Using pass](#-using-pass)
* [Common Mistakes](#-common-mistakes)
* [Real-World Example](#-real-world-example)
* [Quick Reference](#-quick-reference)
* [Key Takeaways](#-key-takeaways)

---

# 🔹 What Are Conditional Statements?

Conditional statements allow your program to execute different code depending on a condition.

Python provides:

```text
if
elif
else
```

Basic structure:

```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```

---

# 🔹 if Statement

The `if` statement executes code only when its condition is `True`.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Output:

```text
You are an adult
```

If the condition is `False`, nothing happens:

```python
age = 15

if age >= 18:
    print("You are an adult")
```

There is no output.

---

# 🔹 if Syntax

The basic syntax is:

```python
if condition:
    statement
```

Example:

```python
temperature = 30

if temperature > 25:
    print("It is hot")
```

### ⚠️ Important

Python uses **indentation** to define the code block.

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
# if age >= 18:
# print("Adult")
```

Usually, use **4 spaces** for indentation.

---

# 🔹 Comparison Operators

Comparison operators are commonly used with `if`.

| Operator | Meaning               | Example   |
| -------- | --------------------- | --------- |
| `==`     | Equal to              | `x == 10` |
| `!=`     | Not equal to          | `x != 10` |
| `>`      | Greater than          | `x > 10`  |
| `<`      | Less than             | `x < 10`  |
| `>=`     | Greater than or equal | `x >= 10` |
| `<=`     | Less than or equal    | `x <= 10` |

---

## 🔸 Equal To `==`

```python
age = 20

if age == 20:
    print("Age is 20")
```

Output:

```text
Age is 20
```

⚠️ `==` checks equality.

`=` is assignment.

```python
age = 20       # Assignment
age == 20      # Comparison
```

---

## 🔸 Not Equal `!=`

```python
age = 20

if age != 18:
    print("Age is not 18")
```

---

## 🔸 Greater Than `>`

```python
score = 90

if score > 80:
    print("Excellent")
```

---

## 🔸 Less Than `<`

```python
temperature = 15

if temperature < 20:
    print("Cold")
```

---

## 🔸 Greater Than or Equal `>=`

```python
age = 18

if age >= 18:
    print("Eligible")
```

---

## 🔸 Less Than or Equal `<=`

```python
age = 16

if age <= 18:
    print("Age is 18 or below")
```

---

# 🔹 if-else Statement

`else` executes when the `if` condition is `False`.

```python
age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

Output:

```text
You cannot vote
```

### Structure

```python
if condition:
    # True
else:
    # False
```

---

# 🔹 if-elif-else

Use `elif` when you need to check multiple conditions.

```python
marks = 75

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Needs improvement")
```

Output:

```text
B
```

Python checks conditions from **top to bottom**.

Once one condition is `True`, the remaining conditions are skipped.

---

# 🔹 Multiple elif Statements

You can use multiple `elif` blocks.

```python
marks = 62

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(grade)
```

Output:

```text
C
```

---

# 🔹 Multiple Conditions

You can combine conditions using logical operators.

Python provides:

```text
and
or
not
```

---

# 🔹 Logical Operator: and

`and` requires **both conditions** to be `True`.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

Both conditions are true, so the output is:

```text
Access granted
```

If either condition is false:

```python
age = 16
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

Nothing is printed.

---

# 🔹 Logical Operator: or

`or` requires **at least one condition** to be `True`.

```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")
```

Output:

```text
Access granted
```

---

# 🔹 Logical Operator: not

`not` reverses a Boolean value.

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

Output:

```text
Please log in
```

---

# 🔹 Logical Operators Summary

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | All conditions must be true         |
| `or`     | At least one condition must be true |
| `not`    | Reverses the result                 |

Example:

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
```

---

# 🔹 Nested if Statements

An `if` statement inside another `if` statement is called a **nested if**.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

Output:

```text
Access granted
```

You can also use `else`:

```python
age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Too young")
```

---

# 🔹 if With Strings

You can compare strings using `==`.

```python
username = "Hadi"

if username == "Hadi":
    print("Welcome Hadi")
```

You can also use `!=`:

```python
username = "Ali"

if username != "Hadi":
    print("Different user")
```

---

## 🔸 Case-Sensitive Comparison

String comparisons are case-sensitive.

```python
name = "Hadi"

if name == "hadi":
    print("Match")
else:
    print("No match")
```

Output:

```text
No match
```

To ignore case:

```python
name = "Hadi"

if name.lower() == "hadi":
    print("Match")
```

---

# 🔹 if With Lists

You can check whether an item exists in a list.

```python
fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("Apple is available")
```

Output:

```text
Apple is available
```

You can also check whether the list is empty:

```python
fruits = []

if not fruits:
    print("No fruits available")
```

---

# 🔹 if With Sets

Sets are commonly used for membership checking.

```python
allowed_users = {"Ali", "Ahmed", "Hadi"}

if "Hadi" in allowed_users:
    print("Access granted")
```

---

# 🔹 if With Dictionaries

You can check whether a key exists.

```python
student = {
    "name": "Hadi",
    "age": 20
}

if "name" in student:
    print("Name exists")
```

To check a value:

```python
if "Hadi" in student.values():
    print("Student found")
```

---

# 🔹 Membership Operators

Use:

```text
in
not in
```

### `in`

```python
numbers = [1, 2, 3, 4]

if 3 in numbers:
    print("Found")
```

Output:

```text
Found
```

### `not in`

```python
if 10 not in numbers:
    print("10 is not present")
```

---

# 🔹 Identity Operators

Python has two identity operators:

```text
is
is not
```

They check whether two variables refer to the **same object**.

```python
a = None

if a is None:
    print("No value")
```

For checking `None`, prefer:

```python
if value is None:
    ...
```

rather than:

```python
if value == None:
    ...
```

---

# 🔹 Truthy and Falsy Values

Python treats some values as `False` when used in a condition.

Common falsy values include:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

Output:

```text
Name is empty
```

---

## 🔸 Truthy Values

Most non-empty and non-zero values are truthy.

```python
name = "Hadi"

if name:
    print("Name exists")
```

Output:

```text
Name exists
```

Another example:

```python
numbers = [1, 2, 3]

if numbers:
    print("List contains data")
```

---

# 🔹 Ternary Operator

Python allows a simple `if-else` statement to be written in one line.

```python
age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)
```

Output:

```text
Adult
```

### Normal Version

```python
if age >= 18:
    message = "Adult"
else:
    message = "Minor"
```

### One-Line Version

```python
message = "Adult" if age >= 18 else "Minor"
```

Use the one-line version when the condition is simple and readable.

---

# 🔹 Conditional Expressions

Another example:

```python
score = 85

result = "Pass" if score >= 50 else "Fail"

print(result)
```

Output:

```text
Pass
```

---

# 🔹 Using pass

`pass` is used when you need a statement syntactically but don't want to execute anything yet.

```python
age = 20

if age >= 18:
    pass
```

This is useful when you're planning to write the logic later.

Example:

```python
username = "Hadi"

if username == "Hadi":
    pass
else:
    print("Unknown user")
```

---

# 🔹 Combining Conditions With Parentheses

For complex conditions, parentheses can improve readability.

```python
age = 25
country = "Pakistan"

if (age >= 18) and (country == "Pakistan"):
    print("Eligible")
```

Another example:

```python
age = 17
has_permission = True

if age >= 18 or (age < 18 and has_permission):
    print("Allowed")
```

---

# 🔹 Operator Precedence

When using multiple logical operators, Python follows a precedence order.

Generally:

```text
not
and
or
```

Example:

```python
a = True
b = False
c = True

result = a or b and c
```

Python evaluates `and` before `or`.

For complicated conditions, use parentheses:

```python
result = a or (b and c)
```

This makes your intention clear.

---

# 🔹 if With User Input

`input()` returns a string, so convert numeric input when necessary.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Example:

```text
Enter your age: 20
Adult
```

---

# 🔹 if With Numbers

```python
number = 10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

This is a common example of `if-elif-else`.

---

# 🔹 Checking Even or Odd

The modulus operator `%` is useful in conditions.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

---

# 🔹 Checking Positive, Negative, or Zero

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Output:

```text
Negative
```

---

# 🔹 Nested Conditions vs Logical Operators

Instead of:

```python
if age >= 18:
    if has_id:
        print("Access granted")
```

You can often write:

```python
if age >= 18 and has_id:
    print("Access granted")
```

Both can work, but combining conditions can make simple logic shorter.

Use nested `if` when the second condition logically depends on the first and the nested structure improves readability.

---

# 🔥 Real-World Example: Login System

```python
username = "Hadi"
password = "python123"

if username == "Hadi":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")
```

Output:

```text
Login successful
```

---

# 🔥 Real-World Example: Grade Calculator

```python
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")
```

Output:

```text
Your grade is A
```

---

# 🔥 Real-World Example: User Access

```python
is_logged_in = True
is_admin = False

if not is_logged_in:
    print("Please log in")
elif is_admin:
    print("Admin dashboard")
else:
    print("User dashboard")
```

Output:

```text
User dashboard
```

---

# 🔹 Common Mistakes

## ❌ Using `=` Instead of `==`

Wrong:

```python
# if age = 18:
#     print("18")
```

Correct:

```python
if age == 18:
    print("18")
```

`=` assigns a value.

`==` compares values.

---

## ❌ Forgetting the Colon

Wrong:

```python
# if age >= 18
#     print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## ❌ Incorrect Indentation

Wrong:

```python
# if age >= 18:
# print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## ❌ Wrong Condition Order

Consider:

```python
marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("A+")
```

The output is:

```text
Pass
```

Why?

Because `marks >= 50` is already `True`, so Python never reaches the `elif`.

### Correct:

```python
if marks >= 90:
    print("A+")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
```

Put **more specific conditions first** when necessary.

---

# 📚 Quick Reference

| Statement | Purpose                                    |
| --------- | ------------------------------------------ |
| `if`      | Execute code if condition is true          |
| `elif`    | Check another condition                    |
| `else`    | Execute when previous conditions are false |
| `and`     | Both conditions must be true               |
| `or`      | At least one condition must be true        |
| `not`     | Reverse a condition                        |
| `in`      | Check membership                           |
| `not in`  | Check absence                              |
| `is`      | Check object identity                      |
| `is not`  | Check different objects                    |
| `pass`    | Do nothing placeholder                     |

---

# 🔹 Comparison Operators Quick Reference

| Operator | Meaning       | Example  |
| -------- | ------------- | -------- |
| `==`     | Equal         | `x == 5` |
| `!=`     | Not equal     | `x != 5` |
| `>`      | Greater than  | `x > 5`  |
| `<`      | Less than     | `x < 5`  |
| `>=`     | Greater/equal | `x >= 5` |
| `<=`     | Less/equal    | `x <= 5` |

---

# 🧠 Decision Flow

A basic `if-elif-else` works like this:

```text
          Condition 1?
          /          \
       True          False
        ↓              ↓
    Run code      Condition 2?
                    /      \
                 True      False
                  ↓          ↓
              Run code    else code
```

Example:

```python
marks = 75

if marks >= 90:
    print("A+")
elif marks >= 70:
    print("B")
else:
    print("Fail")
```

Python checks from top to bottom and executes the **first matching condition**.

---

# ⭐ Key Takeaways

* `if` is used to make decisions.
* `elif` allows you to check multiple conditions.
* `else` handles the remaining case.
* Conditions return `True` or `False`.
* Use `==` for comparison and `=` for assignment.
* Use `and` when **all conditions** must be true.
* Use `or` when **at least one condition** must be true.
* Use `not` to reverse a condition.
* Python uses **indentation** to define code blocks.
* Use `in` and `not in` for membership checking.
* `is` / `is not` are mainly used for **object identity**, especially `None`.
* Empty strings, lists, tuples, dictionaries, sets, `0`, `False`, and `None` are falsy.
* Simple conditions can use the **ternary operator**.
* `if` statements are fundamental to almost every Python program.

---

# 💡 Most Important Pattern

```python
if condition:
    # code if True

elif another_condition:
    # code if True

else:
    # code if all conditions are False
```

### ⭐ Remember

```text
if     → Check a condition
elif   → Check another condition
else   → Everything else
```

```python
# Final Example

age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")
elif age >= 18:
    print("ID required")
else:
    print("You are underage")
```

> 💡 **Tip:** Master `if`, `elif`, `else`, comparison operators, and `and/or/not` first. These are the foundation for loops, functions, validation, authentication logic, and real-world Python applications.
