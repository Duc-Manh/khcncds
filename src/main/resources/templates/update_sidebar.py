import os

files = [
    'admin.html', 'admin_regis.html', 'admin_pro.html', 
    'admin_other.html', 'admin_notice.html', 'admin_news.html', 
    'admin_idea.html', 'admin_employ.html', 'admin_council.html'
]

menu_items_str = """                <li>
                    <a href="/admin/news"
                        class="{news_classes}">
                        <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9.5a2.5 2.5 0 00-2.5-2.5H15"></path>
                        </svg>
                        <span class="sidebar-text whitespace-nowrap transition-opacity duration-300">Tin tức</span>
                    </a>
                </li>
                <li>
                    <a href="/admin/notice"
                        class="{notice_classes}">
                        <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"></path>
                        </svg>
                        <span class="sidebar-text whitespace-nowrap transition-opacity duration-300">Thông báo</span>
                    </a>
                </li>

                <!-- Others -->"""

active_class = "flex items-center gap-3 px-3 py-2.5 rounded-lg text-evnRed hover:bg-gray-50 hover:text-evnBlue transition-colors font-medium text-sm"
inactive_class = "flex items-center gap-3 px-3 py-2.5 rounded-lg text-evnBlue hover:bg-gray-50 hover:text-evnRed transition-colors font-medium text-sm"

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "Tin tức" in content and "Thông báo" in content and "/admin/news" in content:
        print(f"Skipping {f}, already contains the menus.")
        continue

    # Determine classes based on filename
    news_classes = active_class if f == 'admin_news.html' else inactive_class
    notice_classes = active_class if f == 'admin_notice.html' else inactive_class

    new_menu = menu_items_str.format(news_classes=news_classes, notice_classes=notice_classes)

    # replace the anchor
    if "<!-- Others -->" in content:
        content = content.replace("<!-- Others -->", new_menu)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Could not find '<!-- Others -->' in {f}")

