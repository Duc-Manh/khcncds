import re

files = [
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html',
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin_employ.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove rotate-180 from doctor-chevron
    old_chevron = '<svg id="doctor-chevron" class="w-4 h-4 transform rotate-180 shrink-0 sidebar-text transition-opacity duration-300"'
    new_chevron = '<svg id="doctor-chevron" class="w-4 h-4 transform shrink-0 sidebar-text transition-opacity duration-300"'
    content = content.replace(old_chevron, new_chevron)

    # 2. Add hidden to doctor-submenu
    old_submenu = '<ul id="doctor-submenu"\n                        class="border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">'
    new_submenu = '<ul id="doctor-submenu"\n                        class="hidden border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">'
    content = content.replace(old_submenu, new_submenu)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

