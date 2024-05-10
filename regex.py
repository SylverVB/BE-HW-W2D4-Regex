# Lesson 4: Assignments | Regex
# 1. Python Regular Expressions Deep Dive
# Objective: The aim of this assignment is to deepen your practical skills in Python's regular expressions, 
# enhancing your ability to process and manipulate text data. You will tackle a variety of real-world scenarios, 
# applying regex to extract, validate, and transform text effectively.

# Task 1: Email Extraction Enhancement

# Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude 
# certain domains (e.g., 'exclude.com'). Modify the script to extract all email addresses except those from the specified domain.

# Code Example:

# import re

# text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# print(emails)

# Expected Outcome:

# Adapt the regex pattern to exclude email addresses from 'exclude.com'.
# Ensure the script still extracts all other valid email addresses.

import re

def extract_select_emails(text):

    # Extracts emails from the string and excludes all emails with domain 'yahoo.com':
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!yahoo\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

    return emails

text = "Emails: alice_bright@yahoo.com, web.victor.developerB@wharton.edu, caitlyn_ns@gmail.com, Kathy-St@yahoo.com, patrick65@yahoo.com"

print(extract_select_emails(text)) # Output: ['web.victor.developerB@wharton.edu', 'caitlyn_ns@gmail.com']

