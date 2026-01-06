import math
import customtkinter as ctk
from tkinter import messagebox




app = ctk.CTk()
app.geometry("174x340")
app.title("GCD & LCM")
app.resizable(False , False)



frame = ctk.CTkFrame(app , corner_radius = 0)
frame.pack(fill = "both" , expand = True)

app.configure(fg_color = "#ececec")
frame.configure(fg_color = "#ececec")
ctk.set_appearance_mode("Light")


label = ctk.CTkLabel(frame , text = "محاسبه ب.م.م ک.م.م" , font = ("B nazanin" , 22) , fg_color = "#2D6EAF" , text_color = "white" , corner_radius = 7)
label.grid(row = 0 , column = 0 , columnspan = 2 , pady = 10 , padx = 10 , sticky = "ew")




entry1 = ctk.CTkEntry(frame , placeholder_text = "عدد اول را وارد کنید" , font = ("B nazanin" , 18) , height = 37)
entry1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , columnspan = 2 , sticky = "ew")



entry2 = ctk.CTkEntry(frame , placeholder_text = "عدد دوم را وارد کنید" , font = ("B nazanin" , 18) , height = 37)
entry2.grid(row = 2 , column = 0 , pady = 10 , padx = 20 , columnspan = 2 , sticky = "ew")



result_label = ctk.CTkLabel(frame , text = "" , font = ("B nazanin" , 20) , fg_color = "#52cb11" , corner_radius = 6)
result_label.grid(row = 3 , column = 0 , pady = 15 , padx = 20 , columnspan = 2 , sticky = "ew")



def gcd_lcm():

    num1_str = entry1.get().strip()
    num2_str = entry2.get().strip()

    if not num1_str or not num2_str:
        messagebox.showerror("خطا", "لطفاً هر دو عدد را وارد کنید.")

    elif not num1_str.isdigit() or not num2_str.isdigit():
        messagebox.showerror("خطا", "لطفاً فقط اعداد صحیح مثبت وارد کنید.")

    else:
        num1 = int(num1_str)
        num2 = int(num2_str)

        gcd = math.gcd(num1 , num2)
        lcm = math.lcm(num1 , num2)

        result_label.configure(text=f"ب.م.م = {gcd}\nک.م.م = {lcm}")


btn = ctk.CTkButton(frame , text = "محاسبه کن" , font = ("B nazanin" , 20) , command = gcd_lcm , height = 40)
btn.grid(row = 4 , column = 0 , pady = 20 , padx = 20 , columnspan = 2 , sticky = "ew")






app.mainloop()
