import re

files = [
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html',
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin_employ.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add id="doctor-toggle" to the <a> tag
    content = content.replace(
        '<a href="#"\n                        class="flex items-center justify-between px-3 py-2.5 text-activeText font-semibold text-sm">',
        '<a href="#" id="doctor-toggle"\n                        class="flex items-center justify-between px-3 py-2.5 text-activeText font-semibold text-sm">'
    )

    # 2. Add id="doctor-chevron" to the svg
    content = content.replace(
        '<svg class="w-4 h-4 transform rotate-180 shrink-0 sidebar-text transition-opacity duration-300"',
        '<svg id="doctor-chevron" class="w-4 h-4 transform rotate-180 shrink-0 sidebar-text transition-opacity duration-300"'
    )

    # 3. Add id="doctor-submenu" to the ul
    content = content.replace(
        '<ul\n                        class="border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">',
        '<ul id="doctor-submenu"\n                        class="border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">'
    )

    # 4. Add JS code
    js_code = """                sidebarTexts.forEach(text => {
                    text.classList.toggle('hidden');
                });
            });

            // Doctor Accordion Toggle
            const doctorToggle = document.getElementById('doctor-toggle');
            const doctorSubmenu = document.getElementById('doctor-submenu');
            const doctorChevron = document.getElementById('doctor-chevron');

            if (doctorToggle) {
                doctorToggle.addEventListener('click', (e) => {
                    e.preventDefault();
                    doctorSubmenu.classList.toggle('hidden');
                    doctorChevron.classList.toggle('rotate-180');
                });
            }"""

    content = content.replace(
        """                sidebarTexts.forEach(text => {
                    text.classList.toggle('hidden');
                });
            });""",
        js_code
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
