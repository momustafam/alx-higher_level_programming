#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.index("object"): str.index("that")], end="")
print(str[str.index("with"): str.index("very")] + str[:6])
