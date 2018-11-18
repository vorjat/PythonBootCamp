import re

pattern_postale = re.compile("\d{2}-\d{3}")
pattern_maile = re.compile("\w{,}@\w{,}.\w{,}")
pattern_daty = re.compile("\d{1,2} \w{3} \d{4}")
with open("input.txt", 'r') as f:
    text = f.read()

# print(text)

print(pattern_postale.findall(text))
print(pattern_maile.findall(text))
print(pattern_daty.findall(text))
