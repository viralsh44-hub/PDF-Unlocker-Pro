
import tkinter as tk
from tkinter import filedialog,messagebox
from unlocker import PDFUnlocker
QPDF_PATH=r"D:\qpdf\qpdf-12.3.2-msvc64\bin\qpdf.exe"

root=tk.Tk()
root.title("PDF Unlocker")
root.geometry("700x260")

src=tk.StringVar(); out=tk.StringVar(); pwd=tk.StringVar()
status=tk.StringVar(value="Ready")

def bsrc(): 
    p=filedialog.askdirectory()
    if p: src.set(p)
def bout():
    p=filedialog.askdirectory()
    if p: out.set(p)

def run():
    if not src.get() or not out.get() or not pwd.get():
        messagebox.showerror("Error","Select folders and enter password.")
        return
    u=PDFUnlocker(QPDF_PATH)
    for i,total,f,succ,fail in u.unlock_all(src.get(),out.get(),pwd.get()):
        status.set(f"{i}/{total} : {f} | Success={succ} Failed={fail}")
        root.update()
    messagebox.showinfo("Done",status.get())

for r,(lbl,var,cmd) in enumerate([("PDF Folder",src,bsrc),("Output Folder",out,bout)]):
    tk.Label(root,text=lbl,width=14,anchor='w').grid(row=r,column=0,padx=5,pady=5)
    tk.Entry(root,textvariable=var,width=60).grid(row=r,column=1)
    tk.Button(root,text="Browse",command=cmd).grid(row=r,column=2,padx=5)
tk.Label(root,text="Password",width=14,anchor='w').grid(row=2,column=0)
# Password Entry
password_entry = tk.Entry(
    root,
    textvariable=pwd,
    show="*",
    width=30
)

password_entry.grid(row=2, column=1, sticky="w")

show_password = False

def toggle_password():
    global show_password

    show_password = not show_password

    if show_password:
        password_entry.config(show="")
        eye_button.config(text="🙈 Hide")
    else:
        password_entry.config(show="*")
        eye_button.config(text="👁 Show")

eye_button = tk.Button(
    root,
    text="👁 Show",
    width=10,
    command=toggle_password
)

eye_button.grid(row=2, column=2, padx=5)
tk.Button(root,text="Unlock PDFs",command=run,bg="green",fg="white").grid(row=3,column=1,pady=15)
tk.Label(root,textvariable=status).grid(row=4,column=0,columnspan=3)
root.mainloop()
