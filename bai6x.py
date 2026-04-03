import tkinter as tk

def sap_xep():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        # Sắp xếp tăng dần
        if a > b: a, b = b, a
        if a > c: a, c = c, a
        if b > c: b, c = c, b

        ket_qua.config(text=f"{a} {b} {c}")
    except:
        ket_qua.config(text="Nhập sai!")

root = tk.Tk()
root.title("Sắp xếp 3 số")

# Ô nhập
tk.Label(root, text="a").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="b").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="c").grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

# Nút
tk.Button(root, text="Sắp xếp", command=sap_xep).grid(row=3, columnspan=2)

# Kết quả
ket_qua = tk.Label(root, text="")
ket_qua.grid(row=4, columnspan=2)

root.mainloop()