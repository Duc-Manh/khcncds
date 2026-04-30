with open('src/main/resources/templates/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                <div
                    class="bg-white rounded-[20px] p-6 shadow-card border border-borderGray lg:col-span-2 flex flex-col">
                    <div class="flex justify-between items-center mb-6">
                        <h3 class="text-lg font-bold text-textDark">Danh sách tài khoản</h3>
                    </div>

                    <!-- User Table -->
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm whitespace-nowrap">
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
                        </table>
                    </div>
                </div>"""

replacement = """                <div class="bg-white rounded-[20px] p-6 shadow-card border border-borderGray lg:col-span-2 flex flex-col">
                    <div class="flex justify-between items-center mb-6">
                        <h3 class="text-lg font-bold text-textDark">Sáng kiến trong năm</h3>
                        <div class="flex items-center gap-2">
                            <button class="px-4 py-1.5 text-textGray hover:text-evnBlue hover:bg-gray-50 text-xs font-bold rounded-md transition-colors border border-gray-200">Năm trước</button>
                            <button class="px-4 py-1.5 bg-[#eef2ff] text-evnBlue text-xs font-bold rounded-md shadow-sm border border-[#eef2ff]">Hiện tại</button>
                        </div>
                    </div>

                    <div class="flex-1 flex flex-col justify-center space-y-4 pr-2">
                        <!-- Bar Items -->
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Cơ quan Tổng công ty</span>
                                <span>120</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full" style="width: 80%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty Nhiệt điện Cần Thơ</span>
                                <span>95</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-90" style="width: 65%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty Thuỷ điện An Khê - Ka Nak</span>
                                <span>80</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-80" style="width: 55%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty Thuỷ điện Quảng Trị</span>
                                <span>60</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-70" style="width: 45%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty Thuỷ điện Sông Bung</span>
                                <span>50</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-60" style="width: 38%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty Thuỷ điện Trung Sơn</span>
                                <span>70</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-75" style="width: 50%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty CP Thuỷ điện Thác Mơ</span>
                                <span>105</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-95" style="width: 70%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty CP Thuỷ điện A Vương</span>
                                <span>85</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-85" style="width: 60%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty CP Thuỷ điện Sông Ba Hạ</span>
                                <span>65</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-70" style="width: 48%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty CP Nhiệt điện Phả Lại</span>
                                <span>110</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-90" style="width: 75%"></div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <div class="flex justify-between text-xs font-semibold text-textDark">
                                <span>Công ty CP Nhiệt điện Hải Phòng</span>
                                <span>90</span>
                            </div>
                            <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full bg-evnBlue rounded-full opacity-80" style="width: 62%"></div>
                            </div>
                        </div>
                    </div>
                </div>"""

new_content = content.replace(target, replacement)
if new_content != content:
    with open('src/main/resources/templates/admin.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Target not found. Please check exact string.")
