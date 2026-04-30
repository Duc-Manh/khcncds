import re

files = [
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin.html',
    '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin_employ.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Cập nhật href cho Trang chủ
    content = re.sub(
        r'<a href="#"(\s+class="[^"]*?")>(\s*<svg.*?</svg>\s*<span[^>]*?>Trang chủ</span>\s*)</a>',
        r'<a href="/admin"\1>\2</a>',
        content,
        flags=re.DOTALL
    )

    # Cập nhật href cho Tài khoản
    content = re.sub(
        r'<a href="#"(\s+class="[^"]*?")>(\s*<svg.*?</svg>\s*<span[^>]*?>Tài khoản</span>\s*)</a>',
        r'<a href="/admin/employ"\1>\2</a>',
        content,
        flags=re.DOTALL
    )

    # Optional: Highlight the active page in admin_employ.html
    # This might be tricky via regex, so we'll just keep it simple for now as the user only asked for navigation.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
