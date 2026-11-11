# https://www.youtube.com/watch?v=lRLHRaC9OM4
# How Does Python Find A Telephone Number?
# Bring in the library
#  that we need. 
import re
# We'll use this 
#  Regular Expression 
#  throughout this program.
# It matches a telephone
#  number in multipe forms.
pattern = r"(?<!\d)(?:\d{10}|\(\d{3}\)\s*\d{3}-\d{4})(?!\d)"
# Here's a string with
#  3 valid phone numbers.
message = """
Call me at 1234567890 or (123)456-7890.
You can also reach me at (555) 123-4567.
"""
phone = re.findall(pattern, 
                   message)
print(f"We found {phone}")
# Our regular expression
#  matches phone numbers
#  with parentheses 
#  or without.
# What if one parenthesis is 
#  missing?
message = "(606 999-3333"
phone = re.findall(pattern, 
                   message)
print(f"For {message} we found {phone}")
# Our regular expression
#  matches 10 digits.
# What if an extra digit
#  is provided??
message = "(101) 999-33334"
phone = re.findall(pattern, 
                   message)
print(f"For {message} we found {phone}")
# What if the hyphen 
#  is missing?
message = "(303) 9993334"
phone = re.findall(pattern, 
                   message)
print(f"For {message} we found {phone}")
