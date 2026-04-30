import re

file_path = '/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/resources/templates/admin_employ.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the table part
new_table = """<table class="w-full text-left text-sm whitespace-nowrap">
                        <thead>
                            <tr class="text-textGray border-b border-gray-100">
                                <th class="pb-3 font-semibold">ID</th>
                                <th class="pb-3 font-semibold">Đơn vị</th>
                                <th class="pb-3 font-semibold">Email</th>
                                <th class="pb-3 font-semibold">Họ tên</th>
                                <th class="pb-3 font-semibold">Tài khoản</th>
                                <th class="pb-3 font-semibold">Mật khẩu</th>
                                <th class="pb-3 font-semibold">Số điện thoại</th>
                                <th class="pb-3 font-semibold">Vị trí</th>
                                <th class="pb-3 font-semibold text-right pr-2">Phân quyền</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-50">
                            <tr th:each="u : ${users}" class="hover:bg-gray-50 transition-colors group">
                                <td class="py-3 font-medium text-textDark" th:text="${u.id}"></td>
                                <td class="py-3" th:text="${u.department}"></td>
                                <td class="py-3" th:text="${u.email}"></td>
                                <td class="py-3 font-bold text-textDark" th:text="${u.fullName}"></td>
                                <td class="py-3" th:text="${u.username}"></td>
                                <td class="py-3" th:text="${u.password}"></td>
                                <td class="py-3" th:text="${u.phone}"></td>
                                <td class="py-3" th:text="${u.position}"></td>
                                <td class="py-3 text-right pr-2" th:text="${u.role}"></td>
                            </tr>
                        </tbody>
                    </table>"""

content = re.sub(r'<table class="w-full text-left text-sm whitespace-nowrap">.*?</table>', new_table, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

