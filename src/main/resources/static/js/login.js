// Hàm chuyển sang giao diện Đăng ký
function switchToRegister() {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const authContainer = document.getElementById('auth-container');
  const authTitle = document.getElementById('auth-title');

  // Ẩn form đăng nhập
  loginForm.classList.add('hidden');

  // Hiện form đăng ký
  registerForm.classList.remove('hidden');

  // Thay đổi tiêu đề
  authTitle.innerText = 'Đăng ký tài khoản';

  // Nới rộng container để phù hợp giao diện 3 cột của form đăng ký
  authContainer.classList.replace('max-w-[450px]', 'max-w-[900px]');
}

// Hàm quay lại giao diện Đăng nhập
function switchToLogin() {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const authContainer = document.getElementById('auth-container');
  const authTitle = document.getElementById('auth-title');

  // Ẩn form đăng ký
  registerForm.classList.add('hidden');

  // Hiện form đăng nhập
  loginForm.classList.remove('hidden');

  // Thay đổi tiêu đề
  authTitle.innerText = 'Đăng nhập hệ thống';

  // Thu nhỏ container về kích thước ban đầu
  authContainer.classList.replace('max-w-[900px]', 'max-w-[450px]');
}

// Hàm làm mới ảnh mã xác thực
function generateCaptcha() {
  const captchaImage = document.getElementById('captcha-image');
  if (captchaImage) {
    // Thêm tham số thời gian để tránh trình duyệt cache lại ảnh cũ
    captchaImage.src = '/captcha?t=' + new Date().getTime();
  }
}

// Khởi tạo mã khi trang load xong
document.addEventListener('DOMContentLoaded', () => {
  generateCaptcha();
});
