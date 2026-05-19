import re

file_path = "src/main/resources/templates/council.html"
with open(file_path, "r") as f:
    content = f.read()

# Fix registration-form-preview classes
old_reg_class = 'class="fixed inset-0 z-[100] flex hidden items-start justify-center bg-black/50 backdrop-blur-sm overflow-y-auto p-4 sm:py-12"'
new_reg_class = 'class="hidden shrink-0 flex-col items-center p-2 sm:p-2 bg-gray-50/50 rounded-xl h-fit w-[230mm] transition-all"'
content = content.replace(old_reg_class, new_reg_class)

# Fix evaluation-form-preview classes
old_eval_class = 'class="fixed inset-0 z-[100] flex hidden items-start justify-center bg-black/50 backdrop-blur-sm overflow-y-auto p-4 sm:py-12"'
new_eval_class = 'class="hidden shrink-0 flex-col items-center p-2 sm:p-2 bg-gray-50/50 rounded-xl h-fit w-[230mm] transition-all"'
content = content.replace(old_eval_class, new_eval_class)

# The user might have modified the form classes in evaluation-form-preview.
# Wait, I don't need to touch the form HTML since the user just wants the preview values to be mapped properly.
# But wait, did I remove inputs from evaluation-form-preview?
# Let's check if the checkboxes are still spans. Yes, they are spans.

# Now update openPreview() function to map ALL 53 fields!
# We need to replace the old openPreview function.

open_preview_start = content.find("function openPreview()")
open_preview_end = content.find("function submitForm()", open_preview_start)

if open_preview_start != -1 and open_preview_end != -1:
    new_open_preview = """        function openPreview() {
            const preview = document.getElementById('evaluation-form-preview');

            // Copy text inputs and textareas
            const textIds = [1, 2, 3, 4, 5, 6, 21, 22, 26, 27, 29, 30, 32, 33, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53];
            textIds.forEach(id => {
                const el = document.getElementById('i' + id);
                const pel = document.getElementById('preview-i' + id);
                if (el && pel) {
                    pel.textContent = el.value || '';
                }
            });

            // Copy checkboxes and radio buttons
            const checkIds = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 28, 31, 34, 35, 37, 46];
            checkIds.forEach(id => {
                const el = document.getElementById('i' + id);
                const pel = document.getElementById('preview-i' + id);
                if (el && pel) {
                    if (el.checked) {
                        pel.textContent = '✔';
                    } else {
                        pel.textContent = '';
                    }
                }
            });

            // Copy signature image
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
            }
        }
"""
    content = content[:open_preview_start] + new_open_preview + "\n" + content[open_preview_end:]

with open(file_path, "w") as f:
    f.write(content)

