import re

with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/links.html', 'r', encoding='utf-8') as f:
    links_html = f.read()

# find the target block
target_start = '<div class="p-5 space-y-4">'
target_end = '              </div>\n            </div>\n\n            <div class="flex flex-col bg-white border border-gray-200'

start_idx = content.find(target_start)
end_idx = content.find(target_end)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + links_html.rstrip() + '\n' + content[end_idx:]
    with open('/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Failed to find target indices")

