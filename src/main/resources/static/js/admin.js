document.addEventListener("DOMContentLoaded", () => {
            const menuToggle = document.getElementById('menu-toggle');
            const sidebar = document.getElementById('sidebar');
            const logoContainer = document.getElementById('logo-container');
            const sidebarTexts = document.querySelectorAll('.sidebar-text');

            if (menuToggle) {
                menuToggle.addEventListener('click', () => {
                    sidebar.classList.toggle('w-[260px]');
                    sidebar.classList.toggle('w-[80px]');

                    logoContainer.classList.toggle('px-6');
                    logoContainer.classList.toggle('justify-between');
                    logoContainer.classList.toggle('justify-center');
                    sidebar.classList.toggle('sidebar-collapsed');
                });
            }

            // Doctor Accordion Toggle
            const doctorToggle = document.getElementById('doctor-toggle');
            const doctorSubmenu = document.getElementById('doctor-submenu');
            const doctorChevron = document.getElementById('doctor-chevron');

            if (doctorToggle) {
                doctorToggle.addEventListener('click', (e) => {
                    e.preventDefault();
                    doctorSubmenu.classList.toggle('hidden');
                    doctorChevron.classList.toggle('rotate-180');
                });
            }

            // Bind click events to department bars
            const bars = document.querySelectorAll('[data-dept]');
            bars.forEach(bar => {
                bar.classList.add('cursor-pointer', 'hover:bg-gray-50', 'p-1', '-mx-1', 'rounded-md', 'transition-colors');
                bar.addEventListener('click', () => {
                    const deptName = bar.getAttribute('data-dept');
                    fetchAccountList(deptName);
                });
            });
        });

        function toggleCategoryDropdown(btn) {
            const dropdown = document.getElementById('category-dropdown');
            dropdown.classList.toggle('hidden');
        }

        function toggleYearDropdown(btn) {
            const dropdown = document.getElementById('year-dropdown');
            dropdown.classList.toggle('hidden');
        }

        let currentCategory = "";

        async function selectCategory(name, event) {
            event.preventDefault();
            document.getElementById('category-label').innerText = name;
            document.getElementById('category-dropdown').classList.add('hidden');

            currentCategory = name;

            // Fetch available years for this category
            try {
                const response = await fetch(`/api/statistics/years?category=${encodeURIComponent(name)}`);
                const years = await response.json();

                const yearDropdown = document.getElementById('year-dropdown');
                yearDropdown.innerHTML = ''; // Clear existing

                if (years && years.length > 0) {
                    years.forEach(year => {
                        const a = document.createElement('a');
                        a.href = "#";
                        a.className = "block px-4 py-2.5 text-xs font-medium text-textDark hover:bg-gray-50 hover:text-evnBlue transition-colors";
                        a.innerText = year;
                        a.onclick = (e) => selectYear(year, e);
                        yearDropdown.appendChild(a);
                    });

                    // Auto select the first (latest) year
                    selectYear(years[0], { preventDefault: () => { } });
                } else {
                    yearDropdown.innerHTML = '<div class="px-4 py-2 text-xs text-gray-500">Không có dữ liệu</div>';
                    document.getElementById('year-label').innerText = 'Năm';
                    resetChart();
                }
            } catch (error) {
                console.error("Error fetching years:", error);
            }
        }

        async function selectYear(year, event) {
            event.preventDefault();
            document.getElementById('year-label').innerText = year;
            document.getElementById('year-dropdown').classList.add('hidden');

            // Fetch statistics data
            try {
                const response = await fetch(`/api/statistics/data?category=${encodeURIComponent(currentCategory)}&year=${year}`);
                const data = await response.json();
                updateChart(data);
            } catch (error) {
                console.error("Error fetching stats data:", error);
            }
        }

        function updateChart(data) {
            // Find max value to calculate percentage width
            let maxCount = 0;
            for (const key in data) {
                if (data[key] > maxCount) maxCount = data[key];
            }
            // Ensure maxCount is at least 1 to avoid div by zero
            if (maxCount === 0) maxCount = 1;

            const bars = document.querySelectorAll('[data-dept]');
            bars.forEach(barContainer => {
                const deptName = barContainer.getAttribute('data-dept');
                const count = data[deptName] || 0;
                const widthPercent = (count / maxCount) * 100;

                barContainer.querySelector('.dept-count').innerText = count;
                barContainer.querySelector('.dept-bar').style.width = widthPercent + '%';
            });
        }

        function resetChart() {
            const bars = document.querySelectorAll('[data-dept]');
            bars.forEach(barContainer => {
                barContainer.querySelector('.dept-count').innerText = '0';
                barContainer.querySelector('.dept-bar').style.width = '0%';
            });
            document.getElementById('account-list-tbody').innerHTML = `<tr><td colspan="3" class="px-4 py-8 text-center text-gray-400 text-xs">Chọn một đơn vị bên trái để xem danh sách</td></tr>`;
        }

        async function fetchAccountList(department) {
            const tbody = document.getElementById('account-list-tbody');
            tbody.innerHTML = `<tr><td colspan="3" class="px-4 py-8 text-center text-gray-400 text-xs">Đang tải dữ liệu...</td></tr>`;

            const year = document.getElementById('year-label').innerText;
            if (!currentCategory || year === 'Năm') {
                tbody.innerHTML = `<tr><td colspan="3" class="px-4 py-8 text-center text-gray-400 text-xs">Vui lòng chọn Hạng mục và Năm</td></tr>`;
                return;
            }

            try {
                const response = await fetch(`/api/statistics/accounts?category=${encodeURIComponent(currentCategory)}&year=${year}&department=${encodeURIComponent(department)}`);
                const accounts = await response.json();

                if (accounts && accounts.length > 0) {
                    tbody.innerHTML = '';
                    accounts.forEach(acc => {
                        const tr = document.createElement('tr');
                        tr.className = "hover:bg-gray-50 transition-colors";
                        tr.innerHTML = `
                            <td class="px-4 py-3 text-textDark font-medium">${acc.fullName || '-'}</td>
                            <td class="px-4 py-3 text-textGray">${acc.position || '-'}</td>
                            <td class="px-4 py-3 text-textGray">${acc.phone || '-'}</td>
                        `;
                        tbody.appendChild(tr);
                    });
                } else {
                    tbody.innerHTML = `<tr><td colspan="3" class="px-4 py-8 text-center text-gray-400 text-xs">Không có tài khoản nào thuộc đơn vị này</td></tr>`;
                }
            } catch (error) {
                console.error("Error fetching accounts:", error);
                tbody.innerHTML = `<tr><td colspan="3" class="px-4 py-8 text-center text-red-400 text-xs">Lỗi tải dữ liệu</td></tr>`;
            }
        }

        document.addEventListener('click', function (e) {
            const catDropdown = document.getElementById('category-dropdown');
            if (catDropdown && !e.target.closest('#category-dropdown') && !e.target.closest('button[onclick="toggleCategoryDropdown(this)"]')) {
                catDropdown.classList.add('hidden');
            }

            const yearDropdown = document.getElementById('year-dropdown');
            if (yearDropdown && !e.target.closest('#year-dropdown') && !e.target.closest('button[onclick="toggleYearDropdown(this)"]')) {
                yearDropdown.classList.add('hidden');
            }
        });