document.addEventListener('DOMContentLoaded', () => {
  const openMapBtn = document.getElementById('open-map');
  const closeMapBtn = document.getElementById('close-map');
  const mapOverlay = document.getElementById('map-overlay');
  const mapModal = document.getElementById('map-modal');

  const setupSelectRedirect = (selectId) => {
    const selectElem = document.getElementById(selectId);
    if (selectElem) {
      selectElem.addEventListener('change', function () {
        const url = this.value;
        if (url) {
          window.open(url, '_blank');
          this.selectedIndex = 0; // Đưa về mặc định
        }
      });
    }
  };

  // Kích hoạt cho cả 2 danh sách
  setupSelectRedirect('don-vi-thanh-vien');
  setupSelectRedirect('don-vi-lien-ket');
  // Mở overlay
  openMapBtn.addEventListener('click', () => {
    mapOverlay.classList.remove('hidden');
    mapOverlay.classList.add('flex');
    // Tạo hiệu ứng animation
    setTimeout(() => {
      mapModal.classList.remove('scale-95', 'opacity-0');
      mapModal.classList.add('scale-100', 'opacity-100');
    }, 10);
  });

  // Đóng overlay
  const hideMap = () => {
    mapModal.classList.remove('scale-100', 'opacity-100');
    mapModal.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
      mapOverlay.classList.remove('flex');
      mapOverlay.classList.add('hidden');
    }, 300);
  };

  closeMapBtn.addEventListener('click', hideMap);

  // Đóng khi click ra ngoài vùng modal
  mapOverlay.addEventListener('click', (e) => {
    if (e.target === mapOverlay) hideMap();
  });

  // Đóng bằng phím ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !mapOverlay.classList.contains('hidden')) hideMap();
  });

  // Hiệu ứng gõ chữ
  const typingTextElement = document.getElementById('typing-text');
  if (typingTextElement) {
    const text = typingTextElement.textContent.trim();
    typingTextElement.textContent = '';
    let index = 0;
    function type() {
      if (index < text.length) {
        typingTextElement.textContent = text.substring(0, index + 1);
        index++;
        setTimeout(type, 50); // Tốc độ gõ
      } else {
        // Hoàn thành gõ, đợi 5 giây
        setTimeout(() => {
          // Thêm class để tạo hiệu ứng biến mất từ trên xuống
          typingTextElement.classList.add('animate-wipe-down');
          
          // Đợi hiệu ứng CSS hoàn tất (500ms)
          setTimeout(() => {
            typingTextElement.textContent = '';
            typingTextElement.classList.remove('animate-wipe-down');
            index = 0;
            // Bắt đầu gõ lại
            setTimeout(type, 500); 
          }, 500);
        }, 5000);
      }
    }
    
    setTimeout(type, 1000);
  }
});
