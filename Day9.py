#!/usr/bin/env python3
"""
Rounding off with specific digits
"""
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 4)
print(f"{z:,}")
