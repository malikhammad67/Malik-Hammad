# 🐍 Python Match-Case

Python's `match-case` statement is used for structural pattern matching.
It allows you to compare a value against different patterns and execute
specific code when a pattern matches.

> Introduced in Python 3.10

---

## 📌 Table of Contents

- What is Match-Case?
- Basic Syntax
- Simple Example
- Multiple Cases
- Default Case
- Wildcard `_`
- Matching Numbers
- Matching Strings
- OR Patterns
- Guards with `if`
- Capture Patterns
- Matching Lists
- Matching Tuples
- Matching Dictionaries
- Nested Patterns
- Class Patterns
- Match vs if-elif
- Real-World Examples
- Common Mistakes
- Quick Reference
- Key Takeaways

---

# 🔹 What is Match-Case?

`match-case` is used to check a value against different patterns.

It is similar to a `switch` statement in other programming languages,
but Python's `match-case` is more powerful.

It can match:

- Numbers
- Strings
- Lists
- Tuples
- Dictionaries
- Objects
- Complex data structures

Python checks each `case` from top to bottom and executes the first
matching case.

---

# 🔹 Basic Syntax

    match expression:
        case pattern1:
            # code

        case pattern2:
            # code

        case _:
            # default code

The `_` pattern is used as a wildcard and matches anything.

---

# 🔹 Simple Example

    command = "start"

    match command:
        case "start":
            print("Starting...")

        case "stop":
            print("Stopping...")

        case "pause":
            print("Paused")

Output:

    Starting...

The value `"start"` matches the first case.

---

# 🔹 Multiple Cases

You can define multiple cases for different values.

    day = 3

    match day:
        case 1:
            print("Monday")

        case 2:
            print("Tuesday")

        case 3:
            print("Wednesday")

        case 4:
            print("Thursday")

        case 5:
            print("Friday")

Output:

    Wednesday

---

# 🔹 Default Case

The `_` pattern works like a default case.

    number = 10

    match number:
        case 1:
            print("One")

        case 2:
            print("Two")

        case _:
            print("Something else")

Output:

    Something else

Since `10` does not match `1` or `2`, the `_` case runs.

---

# 🔹 Wildcard `_`

The underscore `_` is called a wildcard pattern.

It matches any value.

    command = "delete"

    match command:
        case "start":
            print("Starting")

        case "stop":
            print("Stopping")

        case _:
            print("Unknown command")

Output:

    Unknown command

The wildcard should normally be placed at the end.

---

# 🔹 Matching Numbers

You can match numbers directly.

    status_code = 404

    match status_code:
        case 200:
            print("Success")

        case 404:
            print("Not Found")

        case 500:
            print("Server Error")

        case _:
            print("Unknown Status")

Output:

    Not Found

---

# 🔹 Matching Strings

Strings can also be matched directly.

    role = "admin"

    match role:
        case "admin":
            print("Full access")

        case "user":
            print("User access")

        case "guest":
            print("Limited access")

        case _:
            print("Unknown role")

Output:

    Full access

---

# 🔹 OR Patterns

The `|` operator allows multiple patterns in one case.

    command = "exit"

    match command:
        case "quit" | "exit":
            print("Program ending")

        case "start":
            print("Starting")

        case _:
            print("Unknown command")

Output:

    Program ending

Both `"quit"` and `"exit"` match the first case.

---

# 🔹 Guards with `if`

A case can include an additional condition using `if`.

This is called a guard.

    number = 10

    match number:
        case x if x > 0:
            print("Positive")

        case x if x < 0:
            print("Negative")

        case 0:
            print("Zero")

Output:

    Positive

The value is first captured in `x`, then the condition is checked.

---

# 🔹 Capture Patterns

A variable can capture the value being matched.

    number = 25

    match number:
        case x:
            print(f"The number is {x}")

Output:

    The number is 25

Here:

    x → 25

A capture pattern stores the matched value inside a variable.

---

# 🔹 Matching Lists

`match-case` can match the structure of a list.

    numbers = [1, 2, 3]

    match numbers:
        case [1, 2, 3]:
            print("Exact match")

        case _:
            print("Different list")

Output:

    Exact match

The list must have the same structure for the first case to match.

---

# 🔹 Capturing List Values

You can capture list elements into variables.

    numbers = [10, 20]

    match numbers:
        case [a, b]:
            print(a)
            print(b)

Output:

    10
    20

Here:

    a → 10
    b → 20

---

# 🔹 Using `*` in List Patterns

The `*` operator can capture multiple remaining elements.

    numbers = [1, 2, 3, 4, 5]

    match numbers:
        case [first, *middle, last]:
            print(first)
            print(middle)
            print(last)

Output:

    1
    [2, 3, 4]
    5

Here:

    first  → 1
    middle → [2, 3, 4]
    last   → 5

---

# 🔹 Matching Tuples

Tuples can also be matched based on their structure.

    point = (10, 20)

    match point:
        case (0, 0):
            print("Origin")

        case (x, 0):
            print("X-axis")

        case (0, y):
            print("Y-axis")

        case (x, y):
            print(f"Point: {x}, {y}")

Output:

    Point: 10, 20

The `(x, y)` pattern captures both values.

---

# 🔹 Matching Dictionaries

Dictionaries can be matched based on their keys and values.

    user = {
        "name": "Hadi",
        "age": 20
    }

    match user:
        case {"name": "Hadi", "age": 20}:
            print("User found")

        case _:
            print("Unknown user")

Output:

    User found

---

# 🔹 Capturing Dictionary Values

You can capture dictionary values into variables.

    user = {
        "name": "Hadi",
        "age": 20
    }

    match user:
        case {"name": name, "age": age}:
            print(name)
            print(age)

Output:

    Hadi
    20

Here:

    name → "Hadi"
    age  → 20

---

# 🔹 Nested Patterns

Patterns can be nested inside other patterns.

This is useful when working with JSON or API responses.

    data = {
        "user": {
            "name": "Hadi",
            "age": 20
        }
    }

    match data:
        case {"user": {"name": name, "age": age}}:
            print(name, age)

        case _:
            print("Invalid data")

Output:

    Hadi 20

Python checks the entire nested structure.

---

# 🔹 Class Patterns

`match-case` can also match objects based on their class and attributes.

    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    user = User("Hadi", 20)

    match user:
        case User(name, age):
            print(name, age)

        case _:
            print("Unknown object")

Output:

    Hadi 20

---

# 🔹 Match vs if-elif

Both `match-case` and `if-elif` can handle multiple possibilities.

Using `if-elif`:

    command = "start"

    if command == "start":
        print("Starting")

    elif command == "stop":
        print("Stopping")

    elif command == "pause":
        print("Pausing")

    else:
        print("Unknown command")

Using `match-case`:

    command = "start"

    match command:
        case "start":
            print("Starting")

        case "stop":
            print("Stopping")

        case "pause":
            print("Pausing")

        case _:
            print("Unknown command")

Both are valid.

Use `match-case` when working with known values and patterns.

Use `if-elif` when working with ranges, comparisons, or complex
Boolean conditions.

---

# 🔥 Real-World Example: Menu System

    choice = 2

    match choice:
        case 1:
            print("Create Account")

        case 2:
            print("Login")

        case 3:
            print("Exit")

        case _:
            print("Invalid Choice")

Output:

    Login

---

# 🔥 Real-World Example: API Status Codes

    status_code = 404

    match status_code:
        case 200:
            message = "Request successful"

        case 201:
            message = "Created successfully"

        case 400:
            message = "Bad request"

        case 401:
            message = "Unauthorized"

        case 404:
            message = "Resource not found"

        case 500:
            message = "Server error"

        case _:
            message = "Unknown status"

    print(message)

Output:

    Resource not found

---

# 🔥 Real-World Example: User Roles

    role = "admin"

    match role:
        case "admin":
            print("Full access")

        case "editor":
            print("Can edit content")

        case "user":
            print("Normal user access")

        case "guest":
            print("Limited access")

        case _:
            print("Unknown role")

Output:

    Full access

---

# 🔥 Real-World Example: API Response

    response = {
        "status": "success",
        "data": {
            "name": "Hadi"
        }
    }

    match response:
        case {"status": "success", "data": {"name": name}}:
            print(f"Welcome {name}")

        case {"status": "error"}:
            print("Something went wrong")

        case _:
            print("Unknown response")

Output:

    Welcome Hadi

This demonstrates why `match-case` is useful for structured data.

---

# ⚠️ Common Mistakes

## 1. Forgetting the Colon

Wrong:

    match command
        case "start":
            print("Start")

Correct:

    match command:
        case "start":
            print("Start")

---

## 2. Putting `_` First

Wrong:

    match command:
        case _:
            print("Anything")

        case "start":
            print("Start")

The `"start"` case will never be reached.

Correct:

    match command:
        case "start":
            print("Start")

        case _:
            print("Anything")

---

## 3. Using `match-case` on an Older Python Version

`match-case` requires Python 3.10 or newer.

Check your Python version:

    import sys

    print(sys.version)

Or from the terminal:

    python --version

---

# 📚 Quick Reference

| Pattern | Purpose |
|---|---|
| `case 10:` | Match an exact number |
| `case "start":` | Match an exact string |
| `case _:` | Match anything |
| `case 1 \| 2:` | Match 1 OR 2 |
| `case x:` | Capture a value |
| `case x if x > 10:` | Match with a condition |
| `case [x, y]:` | Match a sequence |
| `case [first, *rest]:` | Capture remaining elements |
| `case {"name": name}:` | Match dictionary data |
| `case (x, y):` | Match tuple structure |
| `case Class(x):` | Match an object |

---

# 🧠 Key Takeaways

- `match-case` was introduced in Python 3.10.
- It is used for structural pattern matching.
- `match` evaluates an expression.
- `case` defines the patterns to check.
- Cases are checked from top to bottom.
- The first successful case is executed.
- `_` works as a wildcard/default pattern.
- `|` allows multiple alternatives in one case.
- Guards allow additional conditions using `if`.
- Lists and tuples can be matched by their structure.
- Dictionaries can be matched by their keys and values.
- Objects can be matched using class patterns.
- `match-case` can make pattern-based logic easier to read.
- `if-elif` is usually better for ranges and complex Boolean conditions.

---

# ⭐ Remember

`if-elif-else`

→ Best for conditions, comparisons, and ranges.

`match-case`

→ Best for patterns, known values, and structured data.

Basic pattern:

    match value:
        case pattern1:
            # code

        case pattern2:
            # code

        case _:
            # default code

---

# 🚀 Final Example

    command = "start"

    match command:
        case "start":
            print("Starting...")

        case "stop":
            print("Stopping...")

        case "restart":
            print("Restarting...")

        case _:
            print("Unknown command")

Output:

    Starting...

> 💡 Tip: Don't think of `match-case` as only a replacement for `switch`.
> Its real strength is structural pattern matching, which allows Python
> to match the shape and contents of lists, tuples, dictionaries, and objects.