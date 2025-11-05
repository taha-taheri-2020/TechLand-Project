import customtkinter as ctk
import tkinter
import framework
from tkinter import messagebox
import webbrowser
app = ctk.CTk()
app.geometry("500x550")
app.title("TechLand program")

# ساخت فریم پس‌زمینه تمام صفحه
bg_frame = ctk.CTkFrame(app, corner_radius=0)
bg_frame.pack(fill="both", expand=True)

def changecolor(choice):
    if choice == "Light":
        ctk.set_appearance_mode("light")
    elif choice == "Dark":
        ctk.set_appearance_mode("dark")
    elif choice == "None":
        pass

menu = ctk.CTkOptionMenu(bg_frame, values=["None","Light","Dark"], command=changecolor)
menu.pack(pady=12)

password = ctk.CTkEntry(bg_frame, placeholder_text="pass word")
password.pack(padx=15)

app.resizable(False, False)
menu.set("None")  # حالت اولیه‌ی OptionMenu
password.focus()  # فوکوس روی فیلد رمز


def password_check():
    get_password = password.get()
    if get_password == "TechLand":

        ent1 = ctk.CTkEntry(bg_frame, placeholder_text="Serial code")
        ent1.pack(pady=5)

        ent2 = ctk.CTkEntry(bg_frame, placeholder_text="Name")
        ent2.pack(pady=5)

        ent3 = ctk.CTkEntry(bg_frame, placeholder_text="Add date")
        ent3.pack(pady=5)

        def mg():
            gent1 = ent1.get()
            gent2 = ent2.get()
            gent3 = ent3.get()
            global obj
            obj = framework.Objects(gent1, gent2, gent3)
            lobj = [obj.serial,obj.name,obj.date]
            obj.add()
            print(lobj)

        bt = ctk.CTkButton(bg_frame, text="Add 🆔", command=mg)
        bt.pack(pady=10)

        def ask_serial():
            dialog = ctk.CTkInputDialog(text="کد سریال را وارد کنید:", title="جستجو")
            inp = dialog.get_input()
            if not inp:
                messagebox.showwarning("خطا", "هیچ مقداری وارد نکردی!")
                return

            # ❗ شیء موقتی فقط برای جستجو
            temp_obj = framework.Objects("", "", "")
            result = temp_obj.search(inp)
            messagebox.showinfo("نتیجه جستجو", result)




        searchbt = ctk.CTkButton(bg_frame, text="Search out 🔎",command=ask_serial)
        searchbt.pack(pady=7)

        def ask_serial2():
            dialog = ctk.CTkInputDialog(text="کد سریال را وارد کنید:", title="جستجو")
            inp = dialog.get_input()
            if not inp:
                messagebox.showwarning("خطا", "هیچ مقداری وارد نکردی!")
                return

            # ❗ شیء موقتی فقط برای جستجو
            temp_obj = framework.Objects("", "", "")
            result = temp_obj.searchback(inp)
            messagebox.showinfo("نتیجه جستجو", result)

        searchbt1 = ctk.CTkButton(bg_frame, text="Search back 🔎",command=ask_serial2)
        searchbt1.pack(pady=7)


        def outdetail():
            dialog1 = ctk.CTkInputDialog(text="کد سریال را وارد کنید:", title="سریال")
            serial = dialog1.get_input()
            dialog2 =  ctk.CTkInputDialog(text="سریال های جانبی را وارد کنید:", title="جانبی")
            serial2 = dialog2.get_input()
            dialog3 = ctk.CTkInputDialog(text="نام فرد را وارد کنید:", title="نام فرد")
            name = dialog3.get_input()
            dialog4 = ctk.CTkInputDialog(text="ساعت را وارد کنید", title="ساعت")
            time = dialog4.get_input()
            dialog5 = ctk.CTkInputDialog(text="تاریخ را وارد کنید", title="تاریخ")
            date = dialog5.get_input()
            dialog6 = ctk.CTkInputDialog(text="نام دبیر را وارد کنید", title="نام دبیر")
            teacher = dialog6.get_input()
            dialog7 = ctk.CTkInputDialog(text="نام کلاس را وارد کنید:", title="کلاس")
            celass = dialog7.get_input()
            with open('log.txt','a',encoding="utf-8") as file:
                file.write(f"{serial} {serial2} {name} {time} {date} {teacher} {celass} \n")

        btlog = ctk.CTkButton(bg_frame, text="out ⬆️",command=outdetail)
        btlog.pack(pady=10)

        def intdetail():
            dialog1 = ctk.CTkInputDialog(text="کد سریال را وارد کنید:", title="سریال")
            serial = dialog1.get_input()
            dialog2 =  ctk.CTkInputDialog(text="سریال های جانبی را وارد کنید:", title="جانبی")
            serial2 = dialog2.get_input()
            dialog3 = ctk.CTkInputDialog(text="نام فرد را وارد کنید:", title="نام فرد")
            name = dialog3.get_input()
            dialog4 = ctk.CTkInputDialog(text="ساعت را وارد کنید", title="ساعت")
            time = dialog4.get_input()
            dialog5 = ctk.CTkInputDialog(text="تاریخ را وارد کنید", title="تاریخ")
            date = dialog5.get_input()
            dialog6 = ctk.CTkInputDialog(text="نام دبیر را وارد کنید", title="نام دبیر")
            teacher = dialog6.get_input()
            dialog7 = ctk.CTkInputDialog(text="نام کلاس را وارد کنید:", title="کلاس")
            celass = dialog7.get_input()
            with open('back.txt','a',encoding="utf-8") as file:
                file.write(f"{serial} {serial2} {name} {time} {date} {teacher} {celass} \n")

        btlog2 = ctk.CTkButton(bg_frame, text="back ⬇️",command=intdetail)
        btlog2.pack(pady=10)

        info = """version : 1.0
developer : TahaByte
second person : amiran ams"""
        
        def link():
            
            messagebox.showinfo("About", info)

        bt2 = ctk.CTkButton(bg_frame, text="about", command=link)
        bt2.pack(pady=5)
    else:
        messagebox.showwarning("رمز اشتباه", "رمز اشتباه است")

but = ctk.CTkButton(bg_frame, text="Check pass",command=password_check)
but.pack(pady=5)
app.mainloop()
