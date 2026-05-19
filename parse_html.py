import re

with open('./src/main/resources/templates/council.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the parts and do the replacement.
print("File read successfully.")
