import re

with open('src/main/resources/templates/council.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div id="content-thamvan"')
end_idx = content.find('<!-- Main Content Box 3: Xét duyệt -->')

if start_idx == -1 or end_idx == -1:
    print("Could not find block")
    exit(1)

block = content[start_idx:end_idx]

# Replace colors
block = block.replace('border-orange-200', 'border-red-200')
block = block.replace('bg-orange-50/30', 'bg-red-50/30')
block = block.replace('text-orange-600', 'text-evnRed')
block = block.replace('bg-orange-500', 'bg-evnRed')
block = block.replace('hover:bg-orange-600', 'hover:bg-red-700')
block = block.replace('border-black', 'border-evnBlue')

new_content = content[:start_idx] + block + content[end_idx:]

with open('src/main/resources/templates/council.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Patched colors successfully")
