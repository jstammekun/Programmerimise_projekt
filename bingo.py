import tkinter as tk
from tkinter import messagebox
import random

def loo_bingo_kaart():
    # Loon listid võimalike numbrite jaoks igas veerus
    b_rida_valikud = list(range(1, 16))
    i_rida_valikud = list(range(16, 31))
    n_rida_valikud = list(range(31, 46))
    g_rida_valikud = list(range(46, 61))
    o_rida_valikud = list(range(61, 76))

    # Loon tühjad listid valitud numbrite jaoks igas veerus
    b_rida = []
    i_rida = []
    n_rida = []
    g_rida = []
    o_rida = []

    # Valin juhuslikud numbrid igasse veergu
    for i in range(6):

        suvaline_b = random.choice(b_rida_valikud)
        suvaline_i = random.choice(i_rida_valikud)
        suvaline_n = random.choice(n_rida_valikud)
        suvaline_g = random.choice(g_rida_valikud)
        suvaline_o = random.choice(o_rida_valikud)

        if suvaline_b not in b_rida:
            b_rida.append(suvaline_b)
            b_rida_valikud.remove(suvaline_b)

        if suvaline_i not in i_rida:
            i_rida.append(suvaline_i)
            i_rida_valikud.remove(suvaline_i)

        if suvaline_n not in n_rida:
            n_rida.append(suvaline_n)
            n_rida_valikud.remove(suvaline_n)

        if suvaline_g not in g_rida:
            g_rida.append(suvaline_g)
            g_rida_valikud.remove(suvaline_g)

        if suvaline_o not in o_rida:
            o_rida.append(suvaline_o)   
            o_rida_valikud.remove(suvaline_o)
            
    return b_rida, i_rida, n_rida, g_rida, o_rida
b_rida, i_rida, n_rida, g_rida, o_rida = loo_bingo_kaart()

# Loon GUI akna

aken = tk.Tk()
aken.title("Bingo Mäng")
aken.geometry("500x500")
aken.configure(bg="lightblue")
aken.resizable(True, True)

pealkiri = tk.Label(aken, text="Bingo Mäng", font=("Arial", 24), bd=2, relief="solid", bg="lightblue")
pealkiri.pack(pady=10)

kaart_frame = tk.Frame(aken, bg="lightblue", bd=2, relief="solid")
kaart_frame.pack(pady=10)

veerud = ['B', 'I', 'N', 'G', 'O']


# Kuvan veergude sildid
for col, veerg in enumerate(veerud):
    veeru_silt = tk.Label(kaart_frame, text=veerg, font=("Arial", 18), bg="lightblue")
    veeru_silt.grid(row=0, column=col, padx=10, pady=10)

def kuva_bingo_kaart():
    b_rida, i_rida, n_rida, g_rida, o_rida = loo_bingo_kaart()
    # Kuvan numbrid kaardil
    for row in range(5):
        b_silt = tk.Label(kaart_frame, text=str(b_rida[row]), font=("Arial", 16), bg="white", width=4, height=2, relief="solid", borderwidth=1)
        b_silt.grid(row=row+1, column=0, padx=5, pady=5)
        i_silt = tk.Label(kaart_frame, text=str(i_rida[row]), font=("Arial", 16), bg="white", width=4, height=2, relief="solid", borderwidth=1)
        i_silt.grid(row=row+1, column=1, padx=5, pady=5)
        n_silt = tk.Label(kaart_frame, text=str(n_rida[row]), font=("Arial", 16), bg="white", width=4, height=2, relief="solid", borderwidth=1)
        n_silt.grid(row=row+1, column=2, padx=5, pady=5)
        g_silt = tk.Label(kaart_frame, text=str(g_rida[row]), font=("Arial", 16), bg="white", width=4, height=2, relief="solid", borderwidth=1)
        g_silt.grid(row=row+1, column=3, padx=5, pady=5)
        o_silt = tk.Label(kaart_frame, text=str(o_rida[row]), font=("Arial", 16), bg="white", width=4, height=2, relief="solid", borderwidth=1)
        o_silt.grid(row=row+1, column=4, padx=5, pady=5)
        
tk.Button(aken, text="Uus kaart", command=kuva_bingo_kaart, font=("Arial", 14), bg="red", fg="white").pack(pady=20)
aken.mainloop()