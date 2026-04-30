with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the closing of Top Menu and opening of Applications with just a blank or a comment
old_str = """            </ul>

            <!-- Applications -->
            <div>

                <ul class="space-y-1">"""

new_str = """                <!-- Applications -->"""

content = content.replace(old_str, new_str)

# Also need to remove the closing </div> of Applications
old_str2 = """                        </a>
                    </li>
                </ul>
            </div>

            <!-- Others -->"""

new_str2 = """                        </a>
                    </li>

            <!-- Others -->"""

content = content.replace(old_str2, new_str2)

# remove pb-2 from Doctor's submenu to make the visual gap identical
old_str3 = """<ul
                            class="pb-2 border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">"""

new_str3 = """<ul
                            class="border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 mb-2 sidebar-text transition-opacity duration-300">"""
# Wait, changing pb-2 to mb-2 moves the space outside the background! That would make the gap between Doctor and Patient larger by 8px, but the background smaller.
# Let's just remove pb-2.
new_str4 = """<ul
                            class="border-l-2 border-gray-200 ml-5 pl-2 space-y-1 mt-1 sidebar-text transition-opacity duration-300">"""

content = content.replace(old_str3, new_str4)


with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
