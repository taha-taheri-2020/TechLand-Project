import os

class Objects:
    def __init__(self, serial_code, name, date_added):   
        self.serial = serial_code
        self.name = name
        self.date = date_added

    def add(self):
        with open('t.txt', 'a', encoding="utf-8") as file:
            file.write(f"{self.serial} {self.name} {self.date}\n")

    def search(self, serial_to_find):
        filename = 'log.txt'  # 🟢 فایل جدید برای جست‌وجو

        # 🔹 بررسی اینکه فایل وجود دارد یا خالی است
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return "⚠️ فایل خالیه یا هنوز داده‌ای ثبت نشده!"

        found_lines = []  # لیست برای نگهداری همه‌ی خط‌های پیدا شده

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if serial_to_find in line:  # اگر کد در هر جای خط بود
                    found_lines.append(line.strip())

        # 🔹 بررسی نتیجه
        if not found_lines:
            return "❌ هیچ موردی پیدا نشد!"
        else:
            # همه‌ی خط‌های پیدا شده رو با خط جدید جدا کن
            result = "\n".join(found_lines)
            return f"✅ موارد پیدا شده:\n{result}"
    def searchback(self, serial_to_find):
        filename = 'back.txt'  # 🟢 فایل جدید برای جست‌وجو

        # 🔹 بررسی اینکه فایل وجود دارد یا خالی است
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return "⚠️ فایل خالیه یا هنوز داده‌ای ثبت نشده!"

        found_lines = []  # لیست برای نگهداری همه‌ی خط‌های پیدا شده

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if serial_to_find in line:  # اگر کد در هر جای خط بود
                    found_lines.append(line.strip())

        # 🔹 بررسی نتیجه
        if not found_lines:
            return "❌ هیچ موردی پیدا نشد!"
        else:
            # همه‌ی خط‌های پیدا شده رو با خط جدید جدا کن
            result = "\n".join(found_lines)
            return f"✅ موارد پیدا شده:\n{result}"
