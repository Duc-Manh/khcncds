import re

html_form = """<form class="bg-white shadow-xl text-black shrink-0 relative h-fit"
                                style="width: 210mm; min-height: 297mm; padding: 10mm 20mm 10mm 30mm; font-family: 'Times New Roman', Times, serif; font-size: 13pt; line-height: 1.1; box-sizing: border-box;">
                                <!-- Title -->
                                <h3 class="font-bold text-center mb-6 uppercase" style="font-size: 14pt;">PHIẾU ĐÁNH GIÁ
                                    CÔNG NHẬN SÁNG KIẾN</h3>

                                <!-- 1. Các thông tin chính sáng kiến -->
                                <div class="mb-4">
                                    <p class="mb-2"><span class="font-bold">1. Các thông tin chính sáng kiến</span>
                                        <span class="italic">(ghi theo Đơn yêu cầu công nhận sáng kiến)</span>:
                                    </p>
                                    <div class="relative mb-2">
                                        <span class="absolute top-[5px] left-2 pointer-events-none">Tiêu đề giải
                                            pháp:</span>
                                        <textarea id="i1" rows="1"
                                            class="w-full border border-orange-500 rounded px-2 py-1 outline-none text-evnBlue bg-transparent resize-none overflow-hidden"
                                            style="text-indent: 135px;"
                                            oninput="this.style.height = ''; this.style.height = this.scrollHeight + 'px'"></textarea>
                                    </div>
                                    <div class="relative mb-2">
                                        <span class="absolute top-[5px] left-2 pointer-events-none">Tác giả/đồng tác giả
                                            giải pháp:</span>
                                        <textarea id="i2" rows="1"
                                            class="w-full border border-orange-500 rounded px-2 py-1 outline-none text-evnBlue bg-transparent resize-none overflow-hidden"
                                            style="text-indent: 220px;"
                                            oninput="this.style.height = ''; this.style.height = this.scrollHeight + 'px'"></textarea>
                                    </div>
                                </div>

                                <!-- 2. Người đánh giá -->
                                <div class="mb-4">
                                    <p class="font-bold mb-2">2. Người đánh giá:</p>
                                    <div class="flex items-center mb-2 gap-2">
                                        <span class="whitespace-nowrap">Họ và tên:</span>
                                        <input id="i3" type="text"
                                            class="flex-1 border border-orange-500 rounded px-2 py-1 outline-none text-evnBlue bg-transparent">
                                    </div>
                                    <p class="mb-2 leading-relaxed">
                                        Thời điểm nhận Đơn và Hồ sơ sáng kiến để đánh giá: ngày
                                        <input id="i4" type="text"
                                            class="w-[1.5em] inline-block border border-orange-500 rounded px-0.5 py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline ">
                                        tháng
                                        <input id="i5" type="text"
                                            class="w-[1.5em] inline-block border border-orange-500 rounded px-0.5 py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline ">
                                        năm
                                        <input id="i6" type="text"
                                            class="w-[2.5em] inline-block border border-orange-500 rounded px-0.5 py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline ">
                                    </p>
                                </div>

                                <!-- 3. Các tiêu chí đánh giá giải pháp -->
                                <div class="mb-4">
                                    <p class="font-bold mb-2">3. Các tiêu chí đánh giá giải pháp</p>
                                    <p class="mb-3">Phải đánh dấu vào 1 trong 2 ô của từng tiêu chí dưới đây</p>

                                    <!-- 3.1 -->
                                    <div class="mb-3 ml-4">
                                        <p class="font-bold italic mb-2">3.1. Về tình trạng kỹ thuật hoặc tổ chức sản
                                            xuất
                                            hiện
                                            tại,
                                            chỉ rõ
                                            ưu khuyết điểm <span class="font-normal">(mục A.1 trong Đơn)</span>:</p>
                                        <div class="flex flex-col sm:flex-row gap-4 sm:gap-20 ml-4">
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i7" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i8').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Thông tin đầy đủ, chính xác</span>
                                            </label>
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i8" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i7').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Thông tin không đầy đủ hoặc không chính xác</span>
                                            </label>
                                        </div>
                                    </div>

                                    <!-- 3.2 -->
                                    <div class="mb-3 ml-4">
                                        <p class="font-bold italic mb-2">3.2. Về nội dung giải pháp <span
                                                class="font-normal">(mục
                                                A.2 trong
                                                Đơn)</span></p>

                                        <div class="ml-4 mb-3">
                                            <p class="italic mb-1">3.2.1. Mục đích của giải pháp, các điều kiện cần
                                                thiết:
                                            </p>
                                            <div class="flex flex-col sm:flex-row gap-4 sm:gap-40 ml-4 mb-1">
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i9" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i10').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Khả thi</span>
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i10" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i9').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Không khả thi</span>
                                                </label>
                                            </div>
                                            <p class="text-[15px] italic">
                                                (Nếu mục đích, điều kiện giải pháp là Không khả thi thì không tiếp tục
                                                đánh
                                                giá
                                                các
                                                mục bên
                                                dưới và chuyển sang mục 4. Kết luận).
                                            </p>
                                        </div>

                                        <div class="ml-4 mb-3">
                                            <p class="italic mb-1">3.2.2. Mô tả chi tiết bản chất của giải pháp</p>
                                            <div class="flex flex-col sm:flex-row gap-4 sm:gap-24 ml-4">
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i11" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i12').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Đầy đủ, rõ ràng</span>
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i12" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i11').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Không đầy đủ/rõ ràng</span>
                                                </label>
                                            </div>
                                        </div>

                                        <div class="ml-4 mb-3">
                                            <p class="italic mb-1">3.2.3. Các bước thực hiện</p>
                                            <div class="flex flex-col sm:flex-row gap-4 sm:gap-40 ml-4">
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i13" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i14').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Hợp lý</span>
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i14" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i13').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Không hợp lý</span>
                                                </label>
                                            </div>
                                        </div>

                                        <div class="ml-4 mb-3">
                                            <p class="italic mb-1 text-justify">3.2.4. Giải pháp có tính mới <span
                                                    class="font-normal">(nếu
                                                    đáp ứng đồng thời tất cả các điều kiện sau đây: i) Không trùng với
                                                    nội
                                                    dung
                                                    của
                                                    giải
                                                    pháp đã được công nhận sáng kiến; ii) Chưa bị bộc lộ công khai trong
                                                    các
                                                    văn
                                                    bản, sách
                                                    báo, tài liệu kỹ thuật đến mức căn cứ vào đó có thể thực hiện ngay
                                                    được;
                                                    iii)
                                                    Không
                                                    trùng với giải pháp của người khác đã được áp dụng hoặc áp dụng thử,
                                                    hoặc
                                                    đưa
                                                    vào kế
                                                    hoạch áp dụng, phổ biến hoặc chuẩn bị các điều kiện để áp dụng, phổ
                                                    biến;
                                                    iv)
                                                    Chưa được
                                                    quy định thành tiêu chuẩn, quy trình, quy phạm bắt buộc phải thực
                                                    hiện)</span>
                                            </p>
                                            <div class="flex flex-col sm:flex-row gap-4 sm:gap-40 ml-4 mb-1">
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i15" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i16').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Có</span>
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer">
                                                    <input id="i16" type="checkbox"
                                                        onclick="if(this.checked) document.getElementById('i15').checked = false;"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Không</span>
                                                </label>
                                            </div>
                                            <p class="text-[15px] italic">
                                                (Nếu giải pháp được đánh giá là Không có tính mới thì không tiếp tục
                                                đánh
                                                giá
                                                mục
                                                3.3, 3.4
                                                bên dưới và chuyển sang mục 4. Kết luận).
                                            </p>
                                        </div>
                                    </div>

                                    <!-- 3.3 -->
                                    <div class="mb-3 ml-4">
                                        <p class="font-bold italic mb-2">3.3. Về quá trình áp dụng giải pháp <span
                                                class="font-normal">(mục
                                                A.3 trong Đơn)</span></p>
                                        <div class="flex flex-col sm:flex-row gap-4 sm:gap-24 ml-4 mb-1">
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i17" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i18').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Đủ dài để đánh giá hiệu quả</span>
                                            </label>
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i18" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i17').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Không đủ dài để đánh giá hiệu quả</span>
                                            </label>
                                        </div>
                                        <p class="text-[15px] italic ml-4">
                                            1. (Nếu quá trình áp dụng giải pháp không đủ dài để đánh giá hiệu quả thì
                                            không
                                            tiếp
                                            tục
                                            đánh
                                            giá mục 3.4 bên dưới và chuyển sang mục 4. Kết luận).
                                        </p>
                                    </div>

                                    <!-- 3.4 -->
                                    <div class="mb-3 ml-4">
                                        <p class="font-bold italic mb-2">3.4. Hiệu quả thực tế thu được khi áp dụng giải
                                            pháp
                                            <span class="font-normal">(mục A.4 trong Đơn)</span>
                                        </p>
                                        <div class="flex flex-col sm:flex-row gap-4 sm:gap-40 ml-4">
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i19" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i20').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Hiệu quả</span>
                                            </label>
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i20" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i19').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Không hiệu quả</span>
                                            </label>
                                        </div>
                                    </div>

                                    <!-- 3.5 -->
                                    <div class="mb-3 ml-4">
                                        <p class="font-bold italic mb-2 text-justify leading-relaxed">3.5. Có khả năng
                                            áp
                                            dụng tại Đơn vị
                                            khác trong <input id="i21" type="text" placeholder="(Đơn vị xét duyệt)"
                                                class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                style="width: 16ch;"
                                                oninput="this.style.width = Math.max(16, this.value.length + 1) + 'ch'">
                                            hoặc có tính hiệu quả cao đủ
                                            để
                                            công
                                            nhận ở
                                            cấp <span class="font-normal"><input id="i22" type="text"
                                                    placeholder="(chỉ dùng cho cấp EVN/EVNGENCO2)"
                                                    class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                    style="width: 34ch;"
                                                    oninput="this.style.width = Math.max(34, this.value.length + 1) + 'ch'"></span>
                                        </p>
                                        <div class="flex flex-col sm:flex-row gap-4 sm:gap-40 ml-4">
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i23" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i24').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Có</span>
                                            </label>
                                            <label class="flex items-center gap-2 cursor-pointer">
                                                <input id="i24" type="checkbox"
                                                    onclick="if(this.checked) document.getElementById('i23').checked = false;"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                <span>Không</span>
                                            </label>
                                        </div>
                                    </div>
                                </div>

                                <!-- 4. Kết luận -->
                                <div class="mb-2">
                                    <p class="font-bold mb-2">4. Kết luận</p>
                                    <div class="ml-4">
                                        <div class="flex items-start gap-2 mb-2">
                                            <span class="font-bold whitespace-nowrap">4.1.</span>
                                            <label class="flex items-center gap-2 cursor-pointer mt-1">
                                                <input id="i25" type="checkbox"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                            </label>
                                            <span class="font-bold italic text-justify">Không công nhận sáng kiến cấp
                                                <input id="i26" type="text"
                                                    class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                    style="width: 5ch;"
                                                    oninput="this.style.width = Math.max(5, this.value.length * 1) + 'ch'">
                                                tại <input id="i27" type="text" placeholder="(tuỳ theo cấp sáng kiến)"
                                                    class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                    style="width: 21ch;"
                                                    oninput="this.style.width = Math.max(21, this.value.length * 1) + 'ch'">
                                                nếu đánh giá ở trên thuộc một trong các trường hợp:</span>
                                        </div>

                                        <div class="ml-10 mb-4 italic space-y-2">
                                            <p>- Mục đích của giải pháp, các điều kiện cần thiết (mục 3.2.1) là Không
                                                khả
                                                thi,
                                                hoặc
                                            </p>
                                            <p>- Giải pháp không có tính mới (mục 3.2.4); hoặc</p>
                                            <p>- Quá trình áp dụng giải pháp (mục 3.3) là Không đủ dài để đánh giá hiệu
                                                quả,
                                                hoặc
                                            </p>
                                            <p>- Việc áp dụng giải pháp (mục 3.4) là Không hiệu quả hoặc</p>
                                            <p>- Không có khả năng áp dụng tại đơn vị khác và không có tính hiệu quả cao
                                                (mục
                                                3.5)
                                                (chỉ dùng
                                                cho cấp EVN/EVNGENCO2).</p>
                                        </div>

                                        <div class="flex items-start gap-2 mb-2">
                                            <span class="font-bold whitespace-nowrap">4.2.</span>
                                            <label class="flex items-center gap-2 cursor-pointer mt-1">
                                                <input id="i28" type="checkbox"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                            </label>
                                            <span class="font-bold italic text-justify">Công nhận sáng kiến cấp <input
                                                    id="i29" type="text"
                                                    class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                    style="width: 5ch;"
                                                    oninput="this.style.width = Math.max(5, this.value.length * 1) + 'ch'">
                                                nhưng đề
                                                nghị
                                                hoàn thiện
                                                hồ sơ sáng kiến trước khi công nhận sáng kiến nếu không có đánh giá
                                                thuộc
                                                một
                                                trong
                                                các
                                                trường hợp nêu tại mục 4.1 ở trên và có ít nhất một trong các tiêu chí
                                                tại
                                                mục
                                                3.1,
                                                3.2.2,
                                                3.2.3 được đánh giá là Không.</span>
                                        </div>

                                        <div class="ml-10 mb-4">
                                            <p class="italic mb-2">Yêu cầu hoàn thiện (ghi rõ phạm vi cần bổ sung trong
                                                đánh
                                                giá
                                                hiện trạng
                                                và/hoặc mô tả chi tiết bản chất giải pháp và/hoặc thay đổi các bước thực
                                                hiện
                                                giải
                                                pháp):
                                            </p>
                                            <p><textarea id="i30" rows="1"
                                                    class="w-full border border-orange-600 rounded px-2 py-1"></textarea>
                                            </p>
                                        </div>

                                        <div class="flex items-start gap-2 mb-4">
                                            <span class="font-bold whitespace-nowrap">4.3.</span>
                                            <label class="flex items-center gap-2 cursor-pointer mt-1">
                                                <input id="i31" type="checkbox"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                            </label>
                                            <span class="font-bold italic text-justify">Công nhận sáng kiến cấp <input
                                                    id="i32" type="text"
                                                    class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                    style="width: 5ch;"
                                                    oninput="this.style.width = Math.max(5, this.value.length * 1) + 'ch'">
                                                tại <input id="i33" type="text"
                                                    class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-start font-normal placeholder-gray-600 align-baseline transition-all"
                                                    style="width: 5ch;"
                                                    oninput="this.style.width = Math.max(5, this.value.length * 1) + 'ch'">
                                                nếu
                                                không
                                                thuộc
                                                các trường hợp nêu tại mục 4.1 và 4.2</span>
                                        </div>

                                        <div class="mb-4">
                                            <p class="font-bold italic mb-2">4.4. Số tiền làm lợi <span
                                                    class="font-normal">(nếu
                                                    Công nhận
                                                    sáng kiến tại mục 4.2 hoặc 4.3)</span></p>
                                            <p class="mb-2 ml-4">Số tiền làm lợi trong năm đầu áp dụng sáng kiến là</p>
                                            <div class="ml-4 space-y-3">
                                                <label class="flex items-start gap-2 cursor-pointer">
                                                    <input id="i34" type="checkbox"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 mt-1  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Không tính được <span class="italic">(nếu mục B trong Đơn ghi
                                                            là
                                                            Không
                                                            tính được
                                                            hoặc người đánh giá cho rằng cách tính số tiền làm lợi ghi
                                                            trong
                                                            Đơn
                                                            là
                                                            không
                                                            khả thi)</span></span>
                                                </label>
                                                <div>
                                                    <label class="flex items-start gap-2 cursor-pointer mb-2">
                                                        <input id="i35" type="checkbox"
                                                            class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 mt-1  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                        <span>Tính được theo cách tính ghi trong Đơn nhưng cần tính lại
                                                            trên
                                                            cơ
                                                            sở
                                                            cập nhật,
                                                            bổ sung số liệu sau:</span>
                                                    </label>
                                                    <p class="ml-6">
                                                        <textarea id="i36" rows="1"
                                                            class="w-full border border-orange-500 rounded px-2 py-1"></textarea>
                                                    </p>
                                                </div>
                                                <label class="flex items-start gap-2 cursor-pointer">
                                                    <input id="i37" type="checkbox"
                                                        class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0 mt-1  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                                    <span>Tính được và đồng ý với số tiền làm lợi theo cách tính ghi
                                                        trong
                                                        Đơn</span>
                                                </label>
                                            </div>
                                        </div>

                                        <div class="mb-4">
                                            <p class="font-bold italic mb-2 text-justify">4.5. Đề xuất mức thù lao chung
                                                cho
                                                tác
                                                giả/đồng
                                                tác giả trong 01 năm <span class="font-normal">(mức tối thiểu là <input
                                                        id="i38" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">%
                                                    tối đa
                                                    là
                                                    <input id="i39" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">%
                                                    nếu tính
                                                    được hoặc tối thiểu là <input id="i40" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">
                                                    mức lương cơ sở tối đa là <input id="i41" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">
                                                    mức lương cơ sở
                                                    nếu
                                                    không tính
                                                    được)<sup class="text-[11px]">1</sup></span></p>
                                            <p class="mb-1">
                                                <textarea id="i42" rows="1"
                                                    class="w-full border border-orange-500 rounded px-2 py-1"></textarea>
                                            </p>
                                            <p class="italic text-[15px]">(người đánh giá ghi rõ số % nếu tính được hoặc
                                                số
                                                mức
                                                lương cơ sở
                                                nếu không tính được)</p>
                                        </div>

                                        <div class="mb-4">
                                            <p class="font-bold italic mb-2 text-justify">4.6. Đề xuất mức thù lao chung
                                                cho
                                                những
                                                người
                                                tham gia tổ chức áp dụng sáng kiến lần đầu trong 01 năm <span
                                                    class="font-normal">(mức tối
                                                    thiểu <input id="i43" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">%
                                                    tối đa là <input id="i44" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">%
                                                    thù lao tác giả nêu tại mục 4.5)<sup
                                                        class="text-[11px]">2</sup></span>
                                            </p>
                                            <p class="mb-1">
                                                <textarea id="i45" rows="1"
                                                    class="w-full border border-orange-500 rounded px-2 py-1"></textarea>
                                            </p>
                                            <p class="italic text-[15px]">(người đánh giá ghi rõ số %)</p>
                                        </div>

                                        <div class="flex items-start gap-2 mb-4">
                                            <span class="font-bold whitespace-nowrap">4.7.</span>
                                            <label class="flex items-center gap-2 cursor-pointer mt-1">
                                                <input id="i46" type="checkbox"
                                                    class="w-4 h-4 border-orange-500 rounded-none appearance-none border flex-shrink-0  checked:before:content-['✔'] checked:before:text-orange-500 checked:before:flex checked:before:justify-center checked:before:items-center checked:before:text-[12px]">
                                            </label>
                                            <span class="font-bold italic text-justify">Đề xuất đăng ký công nhận sáng
                                                kiến
                                                cấp
                                                cao
                                                hơn
                                                <span class="font-normal">(đối với cấp cơ sở tại Đơn vị và cấp Tổng công
                                                    ty)</span></span>
                                        </div>

                                        <div class="mb-8">
                                            <p class="font-bold italic mb-2">4.8. Ý kiến khác</p>
                                            <p><textarea id="i47" rows="1"
                                                    class="w-full border border-orange-500 rounded px-2 py-1"></textarea>
                                            </p>
                                        </div>

                                        <!-- Signatures -->
                                        <div class="flex justify-end mt-8 mb-8 mr-12">
                                            <div class="text-center">
                                                <p class="italic mb-1"><input id="i48" type="text"
                                                        class="border border-orange-500 rounded px-1 py-0.5 outline-none text-evnBlue bg-transparent text-end font-normal placeholder-gray-600 align-baseline transition-all"
                                                        style="width: 10ch;"
                                                        oninput="this.style.width = Math.max(10, this.value.length * 1.1) + 'ch'">,
                                                    Ngày <input id="i49" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">
                                                    tháng <input id="i50" type="text"
                                                        class="w-[1.5em] inline-block border border-orange-500 rounded py-0.5 text-center outline-none text-evnBlue bg-transparent align-baseline">
                                                    năm <input id="i51" type="text"
                                                        class="w-[3em] inline-block border border-orange-500 rounded py-0.5 text-start outline-none text-evnBlue bg-transparent align-baseline">
                                                </p>
                                                <p class="font-bold text-[17px]">Người đánh giá</p>
                                                <p class="italic text-[15px]">(Họ, tên và chữ ký)</p>
                                                <div class="mt-4 aspect-[4/3] w-56 mx-auto border-2 border-orange-500 flex flex-col items-center justify-center rounded-lg bg-white relative overflow-hidden group">
                                                    <button type="button" onclick="document.getElementById('signatureUpload').click()"
                                                        class="text-orange-500 font-semibold px-4 py-2 border border-orange-500 rounded bg-white hover:bg-orange-500 hover:text-white transition-colors print:hidden shadow-sm z-10 relative">
                                                        Tải ảnh chữ ký
                                                    </button>
                                                    <input type="file" id="signatureUpload" style="display:none;" accept="image/*" onchange="previewSignature(event)">
                                                    <img id="signaturePreview" class="absolute inset-0 w-full h-full object-contain hidden z-0" />
                                                </div>
                                                <input id="i53" type="text" placeholder="Nhập họ tên"
                                                    class="mt-4 w-56 mx-auto block text-center border border-orange-500 rounded px-2 py-1 outline-none text-evnBlue bg-transparent print:border-none print:placeholder-transparent">
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Footnotes -->
                                <div class="border-t border-black pt-2 mt-4 text-[14px]">
                                    <p class="mb-1 text-justify"><sup class="text-[10px]">1</sup> Tuỳ từng cấp sáng kiến
                                        EVNGENCO2/Cơ sở ghi
                                        rõ định mức thù lao quy định tại Điều 32, 33 của Quy định này. Thư ký của Hội
                                        đồng
                                        chuẩn
                                        bị
                                        các
                                        phiếu phù hợp trước khi họp.</p>
                                    <p class="text-justify"><sup class="text-[10px]">2</sup> Tuỳ từng cấp sáng kiến
                                        EVNGENCO2/Cơ
                                        sở
                                        ghi rõ
                                        mức tối thiểu và tối đa quy định tại Điều 32, 33 của Quy định này. Thư ký của
                                        Hội
                                        đồng
                                        chuẩn
                                        bị các
                                        phiếu phù hợp trước khi họp.</p>
                                </div>
                            </form>"""

# Replace text inputs and textareas with spans
html_form = re.sub(r'<textarea id="i(\d+)".*?></textarea>', r'<span id="preview-i\1" class="font-bold text-evnBlue"></span>', html_form, flags=re.DOTALL)
html_form = re.sub(r'<input id="i(\d+)" type="text".*?>', r'<span id="preview-i\1" class="font-bold text-evnBlue"></span>', html_form, flags=re.DOTALL)

# Replace checkboxes with spans
html_form = re.sub(r'<input id="i(\d+)" type="checkbox".*?>', r'<span id="preview-i\1" class="inline-block w-4 h-4 border border-black flex-shrink-0 text-center leading-none text-[14px]"></span>', html_form, flags=re.DOTALL)

# Replace the signature preview image
html_form = html_form.replace('<img id="signaturePreview"', '<img id="preview-signaturePreview"')

# Replace the upload button and file input
html_form = re.sub(r'<button type="button" onclick="document.getElementById\(\'signatureUpload\'\).click\(\)".*?</button>', '', html_form, flags=re.DOTALL)
html_form = re.sub(r'<input type="file" id="signatureUpload".*?>', '', html_form)

# Add a close button
close_button = """<button type="button" onclick="document.getElementById('registration-form-preview').classList.add('hidden')" class="absolute top-4 right-4 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600">×</button>"""
html_form = html_form.replace('<!-- Title -->', close_button + '\n                                <!-- Title -->')

with open("preview_form.html", "w") as f:
    f.write(html_form)

