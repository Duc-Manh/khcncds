import re

with open("don_yeu_cau.html", "r") as f:
    don_yeu_cau_html = f.read()

with open("preview_form.html", "r") as f:
    preview_form_html = f.read()

# Fix the close button for evaluation form preview
preview_form_html = preview_form_html.replace(
    """<button type="button" onclick="document.getElementById('registration-form-preview').classList.add('hidden')" class="absolute top-4 right-4 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600">×</button>""",
    """<button type="button" onclick="document.getElementById('evaluation-form-preview').classList.add('hidden');" class="absolute top-4 right-4 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600 print:hidden z-10">×</button>"""
)

# For don yeu cau, we need to add a close button too. But maybe not inside if they use the "Ẩn" button? No, they need a close button on the overlay!
close_btn = """<button type="button" onclick="document.getElementById('registration-form-preview').classList.add('hidden'); document.getElementById('pendingFormsList').classList.remove('hidden');" class="absolute top-4 right-4 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600 print:hidden z-10">×</button>\n"""

don_yeu_cau_html = don_yeu_cau_html.replace('<!-- Header -->', close_btn + '                                <!-- Header -->')
# Wait, don_yeu_cau has `<div class="bg-white shadow-xl...`. Let's add relative to it.
don_yeu_cau_html = don_yeu_cau_html.replace(
    '<div class="bg-white shadow-xl text-black shrink-0"',
    '<div class="bg-white shadow-xl text-black shrink-0 relative"'
)

file_path = "/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/council.html"
with open(file_path, "r") as f:
    content = f.read()

# Find the registration-form-preview div
start_marker = '<div id="registration-form-preview"'
start_idx = content.find(start_marker)
end_div_marker = '                        </div>\n                    </div>\n\n                </div>\n            </div>\n            <script>'
end_idx_2 = content.find(end_div_marker, start_idx)

if start_idx == -1 or end_idx_2 == -1:
    print("Could not find markers")
    exit(1)

# We create both overlays
overlay1 = """<div id="registration-form-preview" class="fixed inset-0 z-[100] flex hidden items-start justify-center bg-black/50 backdrop-blur-sm overflow-y-auto p-4 sm:py-12">\n""" + don_yeu_cau_html + """\n</div>\n"""
overlay2 = """<div id="evaluation-form-preview" class="fixed inset-0 z-[100] flex hidden items-start justify-center bg-black/50 backdrop-blur-sm overflow-y-auto p-4 sm:py-12">\n""" + preview_form_html + """\n</div>\n"""

replacement = overlay1 + overlay2

new_content = content[:start_idx] + replacement + content[end_idx_2:]

# Now modify openPreview()
# Find openPreview function
open_preview_start = new_content.find("function openPreview()")
if open_preview_start != -1:
    open_preview_end = new_content.find("function submitForm()", open_preview_start)
    if open_preview_end != -1:
        old_open_preview = new_content[open_preview_start:open_preview_end]
        new_open_preview = old_open_preview.replace("'registration-form-preview'", "'evaluation-form-preview'")
        new_open_preview = new_open_preview.replace("preview.classList.add('flex');", "")
        new_content = new_content[:open_preview_start] + new_open_preview + new_content[open_preview_end:]

# We also need to fix openRegistrationForm to make sure it shows registration-form-preview
# We don't need to change openRegistrationForm, it already removes hidden.

with open(file_path, "w") as f:
    f.write(new_content)

print("Patch 3 applied successfully")
