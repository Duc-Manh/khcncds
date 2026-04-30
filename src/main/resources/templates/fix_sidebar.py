import re

with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

words = ["Patient", "Departments", "Schedule", "Appointment"]
for word in words:
    content = re.sub(
        r'(</svg>)\s+' + word + r'\s+(</div>)',
        r'\1\n                                <span class="sidebar-text whitespace-nowrap transition-opacity duration-300">' + word + r'</span>\n                            \2',
        content
    )

with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
