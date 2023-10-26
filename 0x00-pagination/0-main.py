#!/usr/bin/env python3
"""
This script demonstrates the usage of the 'index_range' function
from the '0-simple_helper_function' module. It calls the function
twice with different sets of arguments and prints the results.

Usage:
- The 'index_range' function is used to obtain a range of indices
  for pagination or similar purposes.

Author: En-wai Asare
Date: 26/10/23
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
