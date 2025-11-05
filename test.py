import tkinter as tk
from tkinter import messagebox


# --- Funktsioon, mida nupp teeb ---
def tervita():
    nimi = nimi_var.get().strip()
    if nimi:
        messagebox.showinfo("Tervitus", f"Tere, {nimi}!")
    else:
        messagebox.showwarning("Hoiatus", "Palun sisesta nimi!")

# --- Põhiaken ---
aken = tk.Tk()
aken.title("Tervitusrakendus")
aken.geometry("400x300")
aken.configure(bg="#930e0e")  # tumepunane taust

# --- Muutuja ---
nimi_var = tk.StringVar()

# --- Raam (hoiab elemendid keskel) ---
frame = tk.Frame(aken, bg="#f5f5f5", padx=20, pady=20)
frame.pack(expand=True)

# --- Silt ---
silt = tk.Label(frame, text="Sisesta oma nimi:", font=("Helvetica", 12), bg="#f5f5f5")
silt.pack(pady=10)

# --- Sisendiväli ---
sisend = tk.Entry(frame, textvariable=nimi_var, font=("Helvetica", 12), width=30, bd=2, relief="solid")
sisend.pack(pady=5)
sisend.focus_set()

# --- Roheline nupp ---
nupp1 = tk.Button(frame,
    text="Tervita",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50", fg="white",
    activebackground="#45a049",
    command=tervita,
    padx=10, pady=5
)
nupp1.pack(pady=10)

# --- Kollane nupp ---
nupp2 = tk.Button(frame,
    text="Fui",
    font=("Helvetica", 12, "bold"),
    bg="yellow", fg="red",
    activebackground="orange",
    command=lambda: messagebox.showinfo("Fui", "Fui! 😄"),
    padx=10, pady=5
)
nupp2.pack(pady=10)

# --- Käivita rakendus ---
aken.mainloop()
