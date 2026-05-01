import sys

with open('src/main/resources/templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_main = """  <main class="flex-grow flex flex-col">
    <style>
      /* Gradient overlay for hero */
      .hero-bg {
        background: linear-gradient(135deg, rgba(3, 10, 24, 0.95) 0%, rgba(13, 30, 80, 0.8) 100%), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
      }
      
      .glass-btn {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
      }
      
      .glass-btn:hover {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.4);
      }
      
      .glass-btn-blue {
        background: rgba(43, 85, 150, 0.4);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(136, 174, 255, 0.3);
      }
      
      .glass-btn-blue:hover {
        background: rgba(43, 85, 150, 0.6);
        border: 1px solid rgba(136, 174, 255, 0.5);
      }
      
      @keyframes marquee {
        0% { transform: translateX(100vw); }
        100% { transform: translateX(-100%); }
      }
      .animate-marquee {
        animation: marquee 25s linear infinite;
      }
    </style>

    <!-- HERO SECTION -->
    <section class="relative w-full h-[550px] hero-bg flex items-center">
      <div class="relative z-10 w-full max-w-[85vw] mx-auto grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
         
         <div class="md:col-span-5">
           <h2 class="text-white text-4xl md:text-5xl font-bold leading-tight drop-shadow-lg">
             Tôi có một sáng kiến ...
           </h2>
         </div>
         
         <div class="md:col-span-7">
           <div class="grid grid-cols-1 sm:grid-cols-3 gap-5">
              <!-- Button 1 -->
              <a href="#" class="glass-btn rounded-md text-center py-6 px-4 text-white text-sm font-semibold transition-all shadow-lg flex items-center justify-center h-24">
                Đề xuất sáng kiến đột phá
              </a>
              <!-- Button 2 -->
              <a href="#" class="glass-btn-blue rounded-md text-center py-6 px-4 text-white text-sm font-semibold transition-all shadow-lg flex items-center justify-center h-24">
                Đề xuất ứng viên cho vị trí Tổng công trình sư,<br>Kiến trúc sư trưởng
              </a>
              <!-- Button 3 -->
              <a href="#" class="glass-btn-blue rounded-md text-center py-6 px-4 text-white text-sm font-semibold transition-all shadow-lg flex items-center justify-center h-24">
                Đề nghị hỗ trợ hoạt động sáng kiến, giải pháp
              </a>
              
              <!-- Button 4 -->
              <a href="#" class="glass-btn rounded-md text-center py-6 px-4 text-white text-sm font-semibold transition-all shadow-lg flex items-center justify-center h-24">
                Đề xuất tài trợ, hỗ trợ kinh phí
              </a>
              <!-- Button 5 -->
              <a href="#" class="glass-btn-blue rounded-md text-center py-6 px-4 text-white text-sm font-semibold transition-all shadow-lg flex items-center justify-center h-24">
                Mạng lưới chuyên gia
              </a>
              <!-- Button 6 -->
              <a href="#" class="glass-btn-blue rounded-md text-center py-6 px-4 text-white text-sm font-semibold transition-all shadow-lg flex items-center justify-center h-24">
                Đề xuất khác
              </a>
           </div>
         </div>

      </div>
    </section>

    <!-- TICKER SECTION -->
    <div class="w-full bg-[#f8efe3] py-2.5 flex items-center border-b border-[#e8dccb] overflow-hidden">
      <div class="max-w-[85vw] mx-auto w-full flex items-center">
        <div class="bg-evnRed text-white text-[10px] font-bold px-2 py-1 rounded shadow-sm mr-3 shrink-0 uppercase tracking-wide z-10 relative">New</div>
        <div class="text-gray-500 text-sm font-bold mr-4 shrink-0 z-10 relative">24/10/2025</div>
        <div class="overflow-hidden w-full relative flex-grow">
           <div class="whitespace-nowrap text-sm font-bold text-gray-800 animate-marquee inline-block">
              Lấy ý kiến dự thảo Quyết định của Thủ tướng Chính phủ phê duyệt Chương trình KHCN&ĐMST quốc gia phát triển sản phẩm công nghệ chiến lược ưu tiên triển khai...
           </div>
        </div>
      </div>
    </div>

    <!-- CARDS SECTION -->
    <section class="py-16 bg-white w-full">
      <div class="max-w-[85vw] mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Card 1 -->
        <div class="relative h-48 rounded-xl overflow-hidden shadow-lg group">
           <div class="absolute inset-0 bg-gray-900">
              <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2070&auto=format&fit=crop" alt="Card 1" class="w-full h-full object-cover opacity-30 group-hover:opacity-40 transition-opacity duration-500" />
           </div>
           <div class="absolute inset-0 p-5 flex flex-col justify-between items-center text-center">
              <h3 class="text-white font-bold text-sm leading-snug mt-4">GỬI ĐỀ XUẤT SÁNG KIẾN ĐỘT PHÁ</h3>
              <a href="#" class="bg-evnRed hover:bg-red-700 text-white text-xs font-bold px-6 py-2 rounded transition-colors shadow-md mb-2">Gửi đề xuất</a>
           </div>
        </div>
        
        <!-- Card 2 -->
        <div class="relative h-48 rounded-xl overflow-hidden shadow-lg group">
           <div class="absolute inset-0 bg-gray-900">
              <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" alt="Card 2" class="w-full h-full object-cover opacity-30 group-hover:opacity-40 transition-opacity duration-500" />
           </div>
           <div class="absolute inset-0 p-5 flex flex-col justify-between items-center text-center">
              <h3 class="text-white font-bold text-sm leading-snug mt-4">ĐỀ NGHỊ HỖ TRỢ SÁNG KIẾN, GIẢI PHÁP</h3>
              <a href="#" class="bg-evnRed hover:bg-red-700 text-white text-xs font-bold px-6 py-2 rounded transition-colors shadow-md mb-2">Gửi đề xuất</a>
           </div>
        </div>
        
        <!-- Card 3 -->
        <div class="relative h-48 rounded-xl overflow-hidden shadow-lg group">
           <div class="absolute inset-0 bg-gray-900">
              <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop" alt="Card 3" class="w-full h-full object-cover opacity-30 group-hover:opacity-40 transition-opacity duration-500" />
           </div>
           <div class="absolute inset-0 p-5 flex flex-col justify-between items-center text-center">
              <h3 class="text-white font-bold text-sm leading-snug mt-4">ĐỀ XUẤT ỨNG VIÊN TỔNG CÔNG TRÌNH SƯ, KIẾN TRÚC SƯ TRƯỞNG</h3>
              <a href="#" class="bg-evnRed hover:bg-red-700 text-white text-xs font-bold px-6 py-2 rounded transition-colors shadow-md mb-2">Gửi đề xuất</a>
           </div>
        </div>
        
        <!-- Card 4 -->
        <div class="relative h-48 rounded-xl overflow-hidden shadow-lg group">
           <div class="absolute inset-0 bg-gray-900">
              <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop" alt="Card 4" class="w-full h-full object-cover opacity-30 group-hover:opacity-40 transition-opacity duration-500" />
           </div>
           <div class="absolute inset-0 p-5 flex flex-col justify-between items-center text-center">
              <h3 class="text-white font-bold text-sm leading-snug mt-4">ĐĂNG KÝ THAM GIA MẠNG LƯỚI CHUYÊN GIA</h3>
              <a href="#" class="bg-evnRed hover:bg-red-700 text-white text-xs font-bold px-6 py-2 rounded transition-colors shadow-md mb-2">Tham gia</a>
           </div>
        </div>
        
      </div>
    </section>

    <!-- STATISTICS SECTION -->
    <section class="relative bg-evnBlue py-20 overflow-hidden w-full">
       <!-- Rocket background illustration placeholder -->
       <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-20 pointer-events-none w-full h-full flex justify-center items-center">
         <svg width="600" height="600" viewBox="0 0 100 100" fill="none">
            <path d="M50 15 L65 85 L35 85 Z" fill="#88aeff" opacity="0.3"/>
            <circle cx="50" cy="50" r="30" stroke="#88aeff" stroke-width="0.5" stroke-dasharray="2 4" />
            <circle cx="50" cy="50" r="45" stroke="#88aeff" stroke-width="0.2" />
         </svg>
       </div>
       
       <div class="relative z-10 max-w-[85vw] mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 text-center text-white">
          
          <!-- Stat 1 -->
          <div class="flex flex-col items-center">
             <div class="h-20 w-20 rounded-full border-2 border-white/20 flex items-center justify-center mb-6">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
             </div>
             <p class="font-bold text-sm mb-4 leading-relaxed">Đề xuất tài trợ,<br>hỗ trợ kinh phí</p>
             <h4 class="text-5xl font-extrabold tracking-tight">578</h4>
          </div>
          
          <!-- Stat 2 -->
          <div class="flex flex-col items-center">
             <div class="h-20 w-20 rounded-full border-2 border-white/20 flex items-center justify-center mb-6">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
             </div>
             <p class="font-bold text-sm mb-4 leading-relaxed">Sản phẩm – Giải pháp<br>công bố</p>
             <h4 class="text-5xl font-extrabold tracking-tight">104</h4>
          </div>
          
          <!-- Stat 3 -->
          <div class="flex flex-col items-center">
             <div class="h-20 w-20 rounded-full border-2 border-white/20 flex items-center justify-center mb-6">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
             </div>
             <p class="font-bold text-sm mb-4 leading-relaxed">Sáng kiến<br>đã tiếp nhận</p>
             <h4 class="text-5xl font-extrabold tracking-tight">185</h4>
          </div>
          
          <!-- Stat 4 -->
          <div class="flex flex-col items-center">
             <div class="h-20 w-20 rounded-full border-2 border-white/20 flex items-center justify-center mb-6">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
             </div>
             <p class="font-bold text-sm mb-4 leading-relaxed">Chuyên gia về<br>Công nghệ chiến lược</p>
             <h4 class="text-5xl font-extrabold tracking-tight">8.471</h4>
          </div>
          
       </div>
    </section>
  </main>
"""

# Find the start and end of main
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<main class="flex-grow flex flex-col">' in line:
        start_idx = i
    if '</main>' in line:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [new_main] + lines[end_idx+1:]
    with open('src/main/resources/templates/index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Updated index.html")
else:
    print("Could not find <main> tags")
