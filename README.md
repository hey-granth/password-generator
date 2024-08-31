# Password Strength Checker and Generator

This Python script provides a simple password strength checker and a random password generator. It helps users create strong passwords and evaluate the strength of existing ones.

## Features

- Password strength evaluation
- Random password generation
- User-friendly command-line interface

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```
   python password_checker.py
   ```

2. Follow the prompts:
   - Enter a password to check its strength
   - If the password is weak, choose to generate a new one

## Functions

### `strength(password)`

Evaluates the strength of a given password.

- Returns "Weak" if the password is:
  - Less than 8 characters long
  - Contains only letters or only numbers
- Returns "Strong" otherwise

### `generate_password()`

Generates a random password that meets the following criteria:
- At least 8 characters long
- Contains both numbers and letters

### `main()`

The main function that runs the password checker and generator interface.

## Note

This is a basic implementation and should not be used for critical security applications. For real-world use, consider using more sophisticated password strength algorithms and secure random number generators.

*It was just made for fun, as the author was getting bored.*
