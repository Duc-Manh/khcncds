import re

files = [
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html',
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin_employ.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add shrink-0 to the header
    old_header = 'class="h-[72px] sticky top-0 z-10 bg-bgMain/90 backdrop-blur-md px-8 flex items-center justify-between border-b border-borderGray"'
    new_header = 'class="h-[72px] shrink-0 sticky top-0 z-10 bg-bgMain/90 backdrop-blur-md px-8 flex items-center justify-between border-b border-borderGray"'
    
    content = content.replace(old_header, new_header)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

