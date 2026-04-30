import re

with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add id and transition to aside
content = content.replace(
    '<aside\n        class="w-[260px] bg-white border-r border-borderGray flex flex-col h-full shrink-0 z-20 shadow-[4px_0_24px_rgba(0,0,0,0.02)]">',
    '<aside id="sidebar"\n        class="w-[260px] bg-white border-r border-borderGray flex flex-col h-full shrink-0 z-20 shadow-[4px_0_24px_rgba(0,0,0,0.02)] transition-all duration-300">'
)

# 2. Replace Logo area
old_logo = """        <!-- Logo -->
        <div class="h-20 flex items-center px-6">
            <div class="flex items-center gap-2">
                <svg class="w-8 h-8 text-primary" viewBox="0 0 24 24" fill="currentColor">
                    <path
                        d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                </svg>
                <span class="text-xl font-extrabold tracking-tight">VitalHealth</span>
            </div>
            <button class="ml-auto text-textLight hover:text-textGray">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z">
                    </path>
                </svg>
            </button>
        </div>"""

new_logo = """        <!-- Logo -->
        <div id="logo-container" class="h-20 flex items-center px-6 justify-between transition-all duration-300">
            <div class="flex items-center gap-2 sidebar-text transition-opacity duration-300">
                <img src="/images/logo_evngenco2.png" alt="Logo" class="w-10 h-10 object-contain">
            </div>
            <button id="menu-toggle" class="text-textLight hover:text-textGray shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>"""

content = content.replace(old_logo, new_logo)

# 3. Add overflow-x-hidden to the scrollable area
content = content.replace(
    '<div class="flex-1 overflow-y-auto px-4 py-2 space-y-6">',
    '<div class="flex-1 overflow-y-auto px-4 py-2 space-y-6 overflow-x-hidden">'
)

# 4. Wrap text in span
words = ["Dashboard", "Your Account", "Patient", "Departments", "Schedule", "Appointment", "Report", "Human Resources", "Bed Manager", "Payment", "Mail", "Widgets", "Log Out"]
for word in words:
    content = re.sub(
        r'(</svg>)\s+' + word + r'\s+(</a>)',
        r'\1\n                        <span class="sidebar-text whitespace-nowrap transition-opacity duration-300">' + word + r'</span>\n                    \2',
        content
    )

content = re.sub(
    r'(</svg>)\s+Doctor\s+(</div>)',
    r'\1\n                                <span class="sidebar-text whitespace-nowrap transition-opacity duration-300">Doctor</span>\n                            \2',
    content
)

# 5. Hide accordion chevrons
content = content.replace(
    '<svg class="w-4 h-4 transform rotate-180" fill="none" stroke="currentColor"\n                                viewBox="0 0 24 24">',
    '<svg class="w-4 h-4 transform rotate-180 shrink-0 sidebar-text transition-opacity duration-300" fill="none" stroke="currentColor"\n                                viewBox="0 0 24 24">'
)
content = content.replace(
    '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">',
    '<svg class="w-4 h-4 shrink-0 sidebar-text transition-opacity duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">'
)

# 6. Make submenus hide
content = content.replace(
    '<ul class="pb-2 border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1">',
    '<ul class="pb-2 border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">'
)

# 7. Make section headers hide
content = content.replace(
    '<h3 class="px-3 text-xs font-bold text-textLight uppercase tracking-wider mb-2 mt-4">Others</h3>',
    '<h3 class="px-3 text-xs font-bold text-textLight uppercase tracking-wider mb-2 mt-4 sidebar-text transition-opacity duration-300">Others</h3>'
)

# 8. Add shrink-0 to SVGs
content = re.sub(r'<svg class="w-5 h-5"', r'<svg class="w-5 h-5 shrink-0"', content)

# 9. Add JS
js_code = """
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const menuToggle = document.getElementById('menu-toggle');
            const sidebar = document.getElementById('sidebar');
            const logoContainer = document.getElementById('logo-container');
            const sidebarTexts = document.querySelectorAll('.sidebar-text');

            menuToggle.addEventListener('click', () => {
                sidebar.classList.toggle('w-[260px]');
                sidebar.classList.toggle('w-[80px]');
                
                logoContainer.classList.toggle('px-6');
                logoContainer.classList.toggle('justify-center');
                
                sidebarTexts.forEach(text => {
                    text.classList.toggle('hidden');
                });
            });
        });
    </script>
</body>"""

content = content.replace("</body>", js_code)

with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

