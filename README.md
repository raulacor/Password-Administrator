# 🔐 Password Administrator

A lightweight Python CLI tool to **generate strong passwords** (with the option to add hyphens every 4 characters, just like Apple`s password generator) and **assess the strength** of existing ones.

---

## 📋 Table of Contents

- [About](#about)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Password Strength Criteria](#password-strength-criteria)  
- [Example](#example)  

---

## About

This tool allows you to:
- Generate secure passwords with customizable length and optional hyphens for readability.
- Check the strength of any password, receiving a score (0–5) and feedback on missing components like uppercase letters, digits, or special characters.
- Optionally copy generated passwords to clipboard via `pyperclip`.

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/password-tool.git
    cd password-tool
    ```
2. Install dependencies:
    ```bash
    pip install pyperclip
    ```

---

## Usage

Run from the command line:

```bash
python password_tool.py
```

---

## Password Strength Criteria
  Each password gains 1 point for meeting each requirement:
  
  Length ≥ 8 characters
  
  Contains lowercase letters
  
  Contains uppercase letters
  
  Includes at least one digit
  
  Includes at least one special character

---

  ## Example 
    Welcome to the Password Generator tool!
    Options:
    1. Check Current Password Strength.
    2. Generate a Unique Strong Password.
    Choose 1 or 2: 2
    Enter desired password length (minimum 8): 16
    Insert hyphens every 4 chars for readability? (Y/N): Y
  
    Generated password:
    Ab3$-kLm9-#Xy2-T0p
    
    Copy to clipboard? (Y/N): Y
    ✅ Password copied to clipboard!
  


