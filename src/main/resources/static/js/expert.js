function toggleExpertRegistration() {
         const searchTools = document.getElementById('expert-search-tools');
         const grid = document.getElementById('expert-grid');
         const pagination = document.getElementById('expert-pagination');
         const form = document.getElementById('expert-regis-form');

         if (form.classList.contains('hidden')) {
            // Hide list elements, show form
            searchTools.classList.add('hidden');
            grid.classList.add('hidden');
            pagination.classList.add('hidden');
            form.classList.remove('hidden');
         } else {
            // Hide form, show list elements
            form.classList.add('hidden');
            searchTools.classList.remove('hidden');
            grid.classList.remove('hidden');
            pagination.classList.remove('hidden');
         }
      }

async function submitExpertForm(event) {
    event.preventDefault();

    // Lấy các element
    const fullName = document.getElementById('exp-fullName').value.trim();
    const cccd = document.getElementById('exp-cccd').value.trim();
    const phone = document.getElementById('exp-phone').value.trim();
    const email = document.getElementById('exp-email').value.trim();
    const rank = document.getElementById('exp-rank').value;
    const department = document.getElementById('exp-department').value.trim();
    const major = document.getElementById('exp-major').value;
    const field = document.getElementById('exp-field').value.trim();
    const trend = document.getElementById('exp-trend').value.trim();
    const google = document.getElementById('exp-google').value.trim();
    const orcid = document.getElementById('exp-orcid').value.trim();
    const gate = document.getElementById('exp-gate').value.trim();
    const camket = document.getElementById('camket').checked;

    // Validate các trường bắt buộc
    if (!fullName || !cccd || !phone || !email || !department || major === 'Chọn lĩnh vực' || !trend || !google) {
        alert("Bạn cần nhập đủ thông tin cần thiết");
        return;
    }

    // Validate cam kết
    if (!camket) {
        alert("Bạn chưa thực hiện cam kết");
        return;
    }

    // Chuẩn bị payload
    const payload = {
        fullName: fullName,
        cccd: cccd,
        phone: phone,
        email: email,
        rank: rank === 'Chọn' ? null : rank,
        department: department,
        major: major,
        field: field,
        trend: trend,
        google: google,
        orcid: orcid,
        gate: gate
    };

    try {
        const response = await fetch('/api/expert/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message || "Đăng ký thành công!");
            window.location.href = '/login';
        } else {
            alert("Lỗi: " + (data.message || "Không thể đăng ký"));
        }
    } catch (error) {
        console.error("Error submitting form:", error);
        alert("Đã xảy ra lỗi khi kết nối với máy chủ.");
    }
}