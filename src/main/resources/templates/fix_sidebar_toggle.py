import re

files = [
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html',
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin_employ.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add the style rule
    if '.sidebar-collapsed .sidebar-text' not in content:
        content = content.replace(
            '<style>\n        /* Custom scrollbar for webkit */',
            '<style>\n        .sidebar-collapsed .sidebar-text {\n            display: none !important;\n        }\n        /* Custom scrollbar for webkit */'
        )

    # Modify the JS
    js_old = """                logoContainer.classList.toggle('justify-center');

                sidebarTexts.forEach(text => {
                    text.classList.toggle('hidden');
                });"""
    
    js_new = """                logoContainer.classList.toggle('justify-center');
                sidebar.classList.toggle('sidebar-collapsed');"""

    content = content.replace(js_old, js_new)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

