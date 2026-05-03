function toggleApproveFrame(id) {
            const frame = document.getElementById('approve-frame-' + id);
            if (frame) {
                frame.classList.toggle('hidden');
            }
        }

        document.addEventListener("DOMContentLoaded", () => {
            const menuToggle = document.getElementById('menu-toggle');
            const sidebar = document.getElementById('sidebar');
            const logoContainer = document.getElementById('logo-container');
            const sidebarTexts = document.querySelectorAll('.sidebar-text');

            menuToggle.addEventListener('click', () => {
                sidebar.classList.toggle('w-[260px]');
                sidebar.classList.toggle('w-[80px]');

                logoContainer.classList.toggle('px-6');
                logoContainer.classList.toggle('justify-between');
                logoContainer.classList.toggle('justify-center');
                sidebar.classList.toggle('sidebar-collapsed');
            });

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
        });

        function toggleYearDropdown(buttonElement, type) {
            // Kiểm tra dropdown hiện tại
            let existingDropdown = buttonElement.parentElement.querySelector('.year-dropdown');
            if (existingDropdown) {
                existingDropdown.remove();
                return;
            }

            // Đóng tất cả dropdown khác
            document.querySelectorAll('.year-dropdown').forEach(el => el.remove());

            // TODO: Fetch danh sách năm từ API
            // Hiện tại giả lập không có năm nào khác năm hiện tại
            const availableYears = [];

            if (availableYears && availableYears.length > 0) {
                // Render dropdown
                let dropdown = document.createElement('div');
                dropdown.className = 'year-dropdown absolute top-full right-0 mt-2 bg-white border border-gray-200 shadow-xl rounded-lg z-50 min-w-[120px] py-1 overflow-hidden';

                availableYears.forEach(year => {
                    let item = document.createElement('a');
                    item.href = '?year=' + year + '&type=' + type;
                    item.className = 'block px-4 py-2.5 text-sm font-medium text-textDark hover:bg-gray-50 hover:text-evnBlue transition-colors cursor-pointer';
                    item.innerText = 'Năm ' + year;
                    dropdown.appendChild(item);
                });

                buttonElement.parentElement.appendChild(dropdown);
            } else {
                alert("Chỉ có dữ liệu năm hiện tại");
            }
        }

        // Đóng dropdown khi click ra ngoài
        document.addEventListener('click', function (e) {
            if (!e.target.closest('.relative')) {
                document.querySelectorAll('.year-dropdown').forEach(el => el.remove());
            }
        });