# Strings and lists: Strings are inmutable, a.k.a., its elements can`t be meddle with, we cannot change them,
# if we have a string s = "ANDRES", that's the string, and the string s will always be ANDRES,
# A lists on the other hand, I can alter, I can add and take out elements from it.

# So if my name is list and I marry and want to take my wife's name I can, but if it's a String I cannot

# This would be the string
s = "AndresJ.Lopez"
print(s)
# This would be the list
name_list = ["Andres", "J.", "Lopez"]

# Now if I was to change my last name
name_list[2] = "Smith"
print(f"LIST SUCCESS: {name_list}")
