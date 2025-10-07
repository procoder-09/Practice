import re

text = "Hello John, Hello Alice"
pattern = r"Hello"
new_text = re.sub(pattern, "hey", text)
print(new_text)