document.addEventListener("DOMContentLoaded", function () {
            const textToType = "Lưu đồ thực hiện hoạt động Khoa học công nghệ trong EVNGENCO2";
            const typingElement = document.getElementById("typing-text");
            const wrapperElement = document.getElementById("typing-wrapper");
            let index = 0;

            function typeWriter() {
               if (index < textToType.length) {
                  index++;
                  // Thay vì dùng += (dễ gây lỗi mất chữ nếu trình duyệt tự can thiệp), ta chèn lại toàn bộ chuỗi chuẩn từ đầu đến index
                  typingElement.textContent = textToType.substring(0, index);
                  setTimeout(typeWriter, 200); // Tốc độ gõ chữ (200ms/ký tự)
               } else {
                  // Đợi 5 giây sau khi gõ xong
                  setTimeout(() => {
                     // Hiệu ứng đi xuống và mờ dần cho toàn bộ wrapper
                     wrapperElement.classList.remove('translate-y-0', 'opacity-100');
                     wrapperElement.classList.add('translate-y-5', 'opacity-0');

                     // Đợi 0.5s cho hiệu ứng đi xuống hoàn tất
                     setTimeout(() => {
                        // Reset lại vị trí, làm rỗng nội dung (tạm tắt transition)
                        wrapperElement.classList.remove('transition-all', 'duration-500');
                        typingElement.textContent = "";
                        wrapperElement.classList.remove('translate-y-5', 'opacity-0');
                        wrapperElement.classList.add('translate-y-0', 'opacity-100');

                        // Bật lại transition và bắt đầu vòng lặp gõ chữ mới
                        setTimeout(() => {
                           wrapperElement.classList.add('transition-all', 'duration-500');
                           index = 0;
                           typeWriter();
                        }, 50);
                     }, 500);
                  }, 5000); // Thời gian chờ 5 giây
               }
            }

            // Bắt đầu hiệu ứng sau 0.5s khi load trang
            setTimeout(typeWriter, 500);

            // Xử lý sự kiện click để hiện danh sách lưu đồ
            const flowchartToggle = document.getElementById("flowchart-toggle");
            const flowchartMenu = document.getElementById("flowchart-menu");
            const flowchartArrow = document.getElementById("flowchart-arrow");

            flowchartToggle.addEventListener("click", function () {
               flowchartMenu.classList.toggle("hidden");
               flowchartArrow.classList.toggle("rotate-180");
            });

            // Xử lý sự kiện click vào từng nút lưu đồ để hiện ảnh
            const flowBtns = document.querySelectorAll('.flow-btn');
            const flowDisplay = document.getElementById('flowchart-display');
            const flowImg = document.getElementById('flowchart-img');

            flowBtns.forEach(btn => {
               btn.addEventListener('click', function (e) {
                  e.preventDefault(); // Ngăn trình duyệt nhảy trang khi bấm href="#"

                  // Lấy tên file từ data-flow
                  const imageSrc = this.getAttribute('data-flow');

                  // Cập nhật ảnh
                  flowImg.src = imageSrc;

                  // Hiển thị khung ảnh
                  flowDisplay.classList.remove('hidden');

                  // Đổi màu active cho nút vừa được bấm
                  flowBtns.forEach(b => {
                     b.classList.remove('border-evnRed', 'text-evnRed', 'bg-gray-50');
                     b.classList.add('border-transparent');
                  });
                  this.classList.remove('border-transparent');
                  this.classList.add('border-evnRed', 'text-evnRed', 'bg-gray-50');
               });
            });
         });

document.addEventListener("DOMContentLoaded", function () {
               const counters = document.querySelectorAll('.counter-value');
               const speed = 100; // Điều chỉnh tốc độ cuộn số (số càng lớn cuộn càng chậm)

               const startCounting = (counter) => {
                  const updateCount = () => {
                     const target = +counter.getAttribute('data-target');
                     // Lấy giá trị hiện tại, loại bỏ dấu chấm để parse số
                     const count = +counter.innerText.replace(/\./g, '');
                     const inc = target / speed;

                     if (count < target) {
                        const nextVal = Math.ceil(count + inc);
                        // Định dạng lại số (nếu có yêu cầu dấu chấm)
                        if (counter.getAttribute('data-format') === 'dot') {
                           counter.innerText = nextVal.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
                        } else {
                           counter.innerText = nextVal;
                        }
                        // Lặp lại hiệu ứng sau mỗi 20ms
                        setTimeout(updateCount, 20);
                     } else {
                        // Khi đã đạt target, đảm bảo hiển thị đúng số cuối cùng
                        if (counter.getAttribute('data-format') === 'dot') {
                           counter.innerText = target.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
                        } else {
                           counter.innerText = target;
                        }
                     }
                  };
                  updateCount();
               };

               // Chỉ bắt đầu cuộn số khi cuộn chuột đến khu vực này (IntersectionObserver)
               const observer = new IntersectionObserver((entries, observer) => {
                  entries.forEach(entry => {
                     if (entry.isIntersecting) {
                        startCounting(entry.target);
                        observer.unobserve(entry.target); // Ngừng theo dõi sau khi đã chạy
                     }
                  });
               }, { threshold: 0.5 }); // Kích hoạt khi thấy 50% phần tử

               counters.forEach(counter => {
                  observer.observe(counter);
               });
            });

function openDocxPreview(e, url, title, downloadFilename) {
         e.preventDefault();
         const modal = document.getElementById('docx-modal');
         const container = document.getElementById('docx-container');
         const titleEl = document.getElementById('docx-modal-title');
         const downloadBtn = document.getElementById('docx-download-btn');

         if (titleEl) titleEl.textContent = 'Xem trước: ' + title;
         if (downloadBtn) {
            downloadBtn.href = url;
            downloadBtn.download = downloadFilename || url.split('/').pop();
         }

         modal.classList.remove('hidden');
         modal.classList.add('flex');

         // Add a simple animation effect
         setTimeout(() => {
            document.getElementById('docx-modal-content').classList.remove('scale-95');
            document.getElementById('docx-modal-content').classList.add('scale-100');
         }, 10);

         container.innerHTML =
            '<div class="flex items-center justify-center h-full"><div class="animate-spin rounded-full h-12 w-12 border-b-2 border-evnBlue"></div></div>';

         fetch(url)
            .then((response) => {
               if (!response.ok) throw new Error('Network response was not ok');
               return response.blob();
            })
            .then((blob) => {
               container.innerHTML = '';
               docx.renderAsync(blob, container, null, {
                  className: 'docx-wrapper',
                  inWrapper: true,
                  ignoreWidth: true,
                  ignoreHeight: true,
                  ignoreFonts: false,
                  breakPages: true,
                  ignoreLastRenderedPageBreak: true,
                  experimental: false,
                  trimXmlDeclaration: true,
                  debug: false,
               });
            })
            .catch((error) => {
               container.innerHTML =
                  '<div class="text-red-500 text-center p-4">Lỗi khi tải file. Vui lòng kiểm tra lại đường dẫn file (' +
                  url +
                  ').</div>';
               console.error('Error rendering docx:', error);
            });
      }

document.addEventListener('DOMContentLoaded', function () {
         const btn = document.getElementById('mobile-menu-btn');
         const menu = document.getElementById('mobile-menu');
         if (btn && menu) {
            btn.addEventListener('click', function (e) {
               e.preventDefault();
               menu.classList.toggle('hidden');
            });
         }
      });

VANTA.NET({
         el: "#vanta-bg",
         mouseControls: true,
         touchControls: true,
         gyroControls: false,
         minHeight: 200.00,
         minWidth: 200.00,
         scale: 1.00,
         scaleMobile: 1.00,
         color: 0x55ff,
         backgroundColor: 0x030a18, /* Màu nền xanh sẫm tiệp với EVNGENCO2 */
         backgroundAlpha: 0.0 /* Trong suốt để lộ CSS Gradient phía dưới */
      })