import re

# Read the preview form HTML
with open("preview_form.html", "r") as f:
    preview_html = f.read()

preview_html = preview_html.replace(
    """<button type="button" onclick="document.getElementById('registration-form-preview').classList.add('hidden')" class="absolute top-4 right-4 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600">×</button>""",
    """<button type="button" onclick="const p = document.getElementById('registration-form-preview'); p.classList.add('hidden'); p.classList.remove('flex');" class="absolute top-4 right-4 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600">×</button>"""
)

# Read council.html
file_path = "/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/council.html"
with open(file_path, "r") as f:
    content = f.read()

# Find the registration-form-preview div
start_marker = '<div id="registration-form-preview"'
start_idx = content.find(start_marker)

# We look for the closing div of registration-form-preview.
# It ends right before `</div>\n                    </div>\n\n                </div>\n            </div>\n            <script>`
end_div_marker = '                        </div>\n                    </div>\n\n                </div>\n            </div>\n            <script>'
end_idx_2 = content.find(end_div_marker, start_idx)

if start_idx == -1 or end_idx_2 == -1:
    print("Could not find markers")
    exit(1)

# Replace the content
replacement = """<div id="registration-form-preview"
                            class="fixed inset-0 z-[100] hidden items-start justify-center bg-black/50 backdrop-blur-sm overflow-y-auto p-4 sm:py-12">
""" + preview_html + '\n                        </div>\n'
new_content = content[:start_idx] + replacement + content[end_idx_2:]

# Now add openPreview() to the script block
script_to_add = """
        function openPreview() {
            const preview = document.getElementById('registration-form-preview');
            
            // Copy text inputs and textareas
            const textIds = [1, 2, 3, 4, 5, 6, 21, 22, 26, 27, 29, 30, 32, 33, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53];
            textIds.forEach(id => {
                const el = document.getElementById('i' + id);
                const pel = document.getElementById('preview-i' + id);
                if (el && pel) {
                    pel.textContent = el.value;
                }
            });

            // Copy checkboxes
            const checkIds = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 28, 31, 34, 35, 37, 46];
            checkIds.forEach(id => {
                const el = document.getElementById('i' + id);
                const pel = document.getElementById('preview-i' + id);
                if (el && pel) {
                    pel.textContent = el.checked ? '☑' : '☐';
                }
            });

            // Copy signature preview
            const sigImg = document.getElementById('signaturePreview');
            const pSigImg = document.getElementById('preview-signaturePreview');
            if (sigImg && pSigImg && !sigImg.classList.contains('hidden')) {
                pSigImg.src = sigImg.src;
                pSigImg.classList.remove('hidden');
            } else if (pSigImg) {
                pSigImg.classList.add('hidden');
            }

            if (preview) {
                preview.classList.remove('hidden');
                preview.classList.add('flex');
            }
        }
"""

if "function openPreview()" not in new_content:
    new_content = new_content.replace('function submitForm() {', script_to_add + '\n        function submitForm() {')

with open(file_path, "w") as f:
    f.write(new_content)

print("Patch applied successfully")
