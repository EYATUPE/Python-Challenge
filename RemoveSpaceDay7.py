#!/usr/bin/env python3
# Ask user for their Name
Name = input("What's your Name? ")

# Remove Whitespaces from the str
Name = Name.strip()

# Capitalize user's Name (First Letter)

Name = Name.title()
# Print User's Name
print(f"Hello, {Name}")
