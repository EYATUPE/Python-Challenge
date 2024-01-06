#!/usr/bin/env python3
# Ask User their Name
name = input("What's Your Name? ").strip().title()

# Split User's Name
first, Last = name.split()

#Print User's Name
print(f"Hello, {first}")
