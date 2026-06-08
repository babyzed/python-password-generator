# Random Password Generator

## Required Libraries
- `random` — for generating random choices
- `string` — for predefined character sets

## Password Characters
The password is built using:
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Digits (0-9)
- Special characters: `!@#$%^&*()-=_+`

## User Input
- The script asks for **password length** from the user.
- Input is converted to integer.

## How It Works
1. A pool of allowed characters is created.
2. A loop runs for the given length.
3. In each iteration, one random character is chosen.
4. All characters are joined into a single password string.

## Output
The generated password is printed to the console.

## Sample Run