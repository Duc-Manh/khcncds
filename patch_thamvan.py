import re

with open('src/main/resources/templates/council.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<!-- Cột trái (Accordion + Danh sách) -->')
end_idx = content.find('<!-- Hình chữ nhật viền đen bên phải (Hiển thị câu trả lời) -->')

# Extract the inner question div block
question_start = content.find('<div th:each="q : ${questions}"', start_idx)
question_end = content.find('<div th:if="${#lists.isEmpty(questions)}"', start_idx)

question_block = content[question_start:question_end].strip()

# Create column 1
block1 = question_block.replace('<div th:each="q : ${questions}"', '<div th:each="q : ${questions}" th:if="${q.state == \'1\'}"')
col1 = f"""                    <!-- Cột 1: Chưa trả lời -->
                    <div class="flex-1 flex flex-col gap-4">
                        <h3 class="font-bold text-evnBlue text-lg border-b pb-2">Danh sách chưa trả lời</h3>
                        <div class="flex-1 overflow-y-auto max-h-[600px] pr-2 space-y-4">
                            <!-- Lặp qua danh sách tham vấn chưa trả lời -->
                            {block1}
                            <div th:if="${{#lists.isEmpty(questions)}}" class="text-center py-8 bg-white/50 rounded-xl">
                                <p class="text-gray-700 font-medium">Chưa có dữ liệu tham vấn.</p>
                            </div>
                        </div>
                    </div>"""

# Create column 2
block2 = question_block.replace('<div th:each="q : ${questions}"', '<div th:each="q : ${questions}" th:if="${q.state != \'1\'}"')
col2 = f"""                    <!-- Cột 2: Đã trả lời -->
                    <div class="flex-1 flex flex-col gap-4">
                        <h3 class="font-bold text-evnBlue text-lg border-b pb-2">Danh sách đã trả lời</h3>
                        <div class="flex-1 overflow-y-auto max-h-[600px] pr-2 space-y-4">
                            <!-- Lặp qua danh sách tham vấn đã trả lời -->
                            {block2}
                            <div th:if="${{#lists.isEmpty(questions)}}" class="text-center py-8 bg-white/50 rounded-xl">
                                <p class="text-gray-700 font-medium">Chưa có dữ liệu tham vấn.</p>
                            </div>
                        </div>
                    </div>"""

replacement = col1 + "\n\n" + col2 + "\n\n                    "

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('src/main/resources/templates/council.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Patched successfully")
