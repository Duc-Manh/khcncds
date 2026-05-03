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