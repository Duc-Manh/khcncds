import sys

with open('src/main/resources/templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the <nav> block
nav_start = content.find('<nav class="hidden lg:flex')
if nav_start == -1:
    print("Could not find nav element")
    sys.exit(1)

nav_end = content.find('</nav>', nav_start) + len('</nav>')
nav_content = content[nav_start:nav_end]

# Modify the nav_content classes for a horizontal row
nav_content = nav_content.replace('justify-between w-full', 'justify-center gap-12 w-full')

# Find the wrapper and remove it
wrapper_start = content.rfind('<div class="flex items-center w-[40%]">', 0, nav_start)
wrapper_end = content.find('</div>', nav_end) + len('</div>')

if wrapper_start != -1 and wrapper_end != -1:
    content = content[:wrapper_start] + content[wrapper_end:]
else:
    print("Could not find nav wrapper")
    sys.exit(1)

# Find </header> to insert the new nav wrapper
header_end = content.find('</header>')
if header_end == -1:
    print("Could not find </header>")
    sys.exit(1)

new_nav_wrapper = f"""
    </div> <!-- Close the max-w-[85vw] mx-auto from above -->
    <div class="w-full border-t border-gray-200 mt-2 bg-gray-50 shadow-sm">
      <div class="max-w-[85vw] mx-auto">
        <div class="flex items-center justify-center py-4 w-full">
          {nav_content}
        </div>
      </div>
"""

# We need to insert this BEFORE </header>.
# Wait, the structure inside <header> is:
# <header>
#   <div class="max-w-[85vw] mx-auto">
#     ...
#   </div>
# </header>
# Since I removed the inner nav wrapper, the <div class="max-w-[85vw] mx-auto"> is still open when we reach </header> in my script? No, wait!
# Original structure:
#   <header class="relative z-50 bg-white w-full flex-shrink-0">
#     <div class="max-w-[85vw] mx-auto">
#       <div class="flex justify-between items-center h-22">
#         <img>
#         <div wrapper> <nav> </nav> </div>
#       </div>
#     </div>
#   </header>
# If I remove the <div wrapper>...</div>, the outer tags are unchanged.
# So before </header>, we have the closing </div> for flex, and closing </div> for max-w.
# If I just insert the new wrapper before </header>, it will be a sibling to the <div class="max-w-[85vw] mx-auto">.
# Let's adjust new_nav_wrapper to just be a standard block inserted before </header>.

new_nav_wrapper = f"""
    <div class="w-full border-t border-b border-gray-100 mt-2 shadow-sm bg-white">
      <div class="max-w-[85vw] mx-auto">
        <div class="flex items-center justify-center py-3 w-full">
          {nav_content}
        </div>
      </div>
    </div>
"""

content = content[:header_end] + new_nav_wrapper + content[header_end:]

# Center the logo
content = content.replace('<div class="flex justify-between items-center h-22">', '<div class="flex justify-center items-center h-22">')

with open('src/main/resources/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated nav successfully.")
