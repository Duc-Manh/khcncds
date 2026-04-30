forms = [
    "Biểu mẫu biên bản họp hội đồng tư vấn",
    "Biểu mẫu thuyết minh đề tài/nhiệm vụ KHCN",
    "Biểu mẫu Phiếu xét duyệt/Tuyển chọn hồ sơ đăng ký nhiệm vụ KHCN",
    "Biểu mẫu Biên bản xét duyệt/tuyển chọn hồ sơ đăng ký",
    "Biểu mẫu biên bản họp tổ thẩm định",
    "Biểu mẫu hợp đồng KHCN",
    "Biểu mẫu báo cáo tổng kết thực hiện nhiệm vụ KHCN (các trang bìa, trang đầu, tài liệu tham khảo)",
    "Biểu mẫu báo cáo tóm tắt kết quả nhiệm vụ KHCN",
    "Biểu mẫu ý kiến phản biện nhiệm vụ KHCN",
    "Biểu mẫu đánh giá nghiệm thu KHCN",
    "Biểu mẫu biên bản nghiệm thu nhiệm vụ KHCN",
    "Biểu mẫu báo cáo đánh giá nghiệm thu cấp cơ sở",
    "Biểu mẫu quyết định công nhận kết quả thực hiện nhiệm vụ KHCN",
    "Biểu mẫu giao nhận tài liệu và kết quả thực hiện nhiệm vụ KHCN",
    "Biểu mẫu thanh lý hợp đồng KHCN",
    "Biểu mẫu Giấy uỷ quyền",
    "Biểu mẫu hồ sơ hoạt động sáng kiến",
    "Biểu mẫu đánh giá công nhận sáng kiến",
    "Biểu mẫu biên bản họp hội đồng sáng kiến",
    "Biểu mẫu báo cáo hoàn thiện sau xét duỵêt, công nhận",
    "Biểu mẫu quyết định công nhận sáng kiến",
    "Biểu mẫu giấy chứng nhận sáng kiến",
    "Biểu mẫu báo cáo hoạt động KHCN"
]

def clean_filename(name):
    name = name.replace(" ", "_").replace("/", "_").replace(",", "").replace("(", "").replace(")", "").replace("ý", "y").replace("ệ", "e")
    # basic non-accented char replacement for common Vietnamese letters to make download filename nicer
    mapping = {
        'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ắ': 'a', 'ằ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ấ': 'a', 'ầ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ế': 'e', 'ề': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ố': 'o', 'ồ': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ớ': 'o', 'ờ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ứ': 'u', 'ừ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
        'đ': 'd', 'Đ': 'D'
    }
    for k, v in mapping.items():
        name = name.replace(k, v)
    return name

import urllib.parse

print('<div class="flex-grow overflow-y-auto p-5 space-y-4 max-h-[350px] scrollbar-thin">')
print("""                <a href="#"
                  onclick="openDocxPreview(event, '/db/pl2.docx', 'Biểu mẫu hồ sơ nhiệm vụ KHCN', 'Bieu_mau_ho_so_nhiem_vu_KHCN.docx')"
                  class="flex items-start gap-3 group">
                  <svg class="w-5 h-5 text-evnRed mt-1 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z">
                    </path>
                  </svg>
                  <span class="text-sm font-semibold text-evnBlue group-hover:text-evnRed transition-colors">Biểu mẫu hồ
                    sơ nhiệm vụ KHCN</span>
                </a>
                <a href="#"
                  onclick="openDocxPreview(event, '/db/p2.docx', 'Biểu mẫu phiếu đề xuất đề tài nghiên cứu khoa học', 'Bieu_mau_phieu_de_xuat_NCKH.docx')"
                  class="flex items-start gap-3 group border-t pt-3">
                  <svg class="w-5 h-5 text-evnRed mt-1 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z">
                    </path>
                  </svg>
                  <span class="text-sm font-semibold text-evnBlue group-hover:text-evnRed transition-colors">Biểu mẫu
                    phiếu đề xuất đề tài nghiên cứu khoa học</span>
                </a>
                <a href="#" onclick="openDocxPreview(event, '/db/p3.docx', 'Biểu mẫu phiếu đánh giá đề xuất nhiệm vụ KHCN', 'Bieu_mau_phieu_danh_gia_de_xuat_nhiem_vu_KHCN.docx')" class="flex items-start gap-3 group border-t pt-3">
                  <svg class="w-5 h-5 text-evnRed mt-1 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z">
                    </path>
                  </svg>
                  <span class="text-sm font-semibold text-evnBlue group-hover:text-evnRed transition-colors">Biểu mẫu
                    phiếu đánh giá đề xuất nhiệm vụ KHCN</span>
                </a>""")

for i, form in enumerate(forms, 4):
    file_id = f"p{i}"
    dl_name = clean_filename(form) + ".docx"
    
    # We must escape single quotes in the form title to prevent breaking onclick string
    escaped_form = form.replace("'", "\\'")
    
    html = f"""                <a href="#" onclick="openDocxPreview(event, '/db/{file_id}.docx', '{escaped_form}', '{dl_name}')" class="flex items-start gap-3 group border-t pt-3">
                  <svg class="w-5 h-5 text-evnRed mt-1 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"></path></svg>
                  <span class="text-sm font-semibold text-evnBlue group-hover:text-evnRed transition-colors">{form}</span>
                </a>"""
    print(html)

print("              </div>")
