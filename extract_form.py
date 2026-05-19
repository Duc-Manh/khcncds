import re

log_path = '/Users/ducmanh/.gemini/antigravity/brain/e7ccbfd8-f5cf-4e62-820c-4b323f55f829/.system_generated/logs/overview.txt'
with open(log_path, 'r') as f:
    lines = f.readlines()

output = []
recording = False
for line in lines:
    if '<div class="bg-white shadow-xl text-black shrink-0"' in line and 'font-size: 13pt;' in line:
        recording = True
    if recording:
        output.append(line)
        if 'Ghi chú: người nộp đơn cần gửi kèm bản sao điện tử' in line:
            output.append('                            </div>\n')
            break

with open('extracted_form.html', 'w') as f:
    f.writelines(output)
print("Extracted to extracted_form.html")
