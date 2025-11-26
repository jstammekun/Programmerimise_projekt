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

def mängu_alustamine():
    global viimane_nr, numbrid
    kaart_frame.destroy()
    lugeja_frame.destroy()
    
    viimane_nr_frame = tk.Frame(aken, height=500, width=500, bg="lightblue", bd=2, relief="solid")
    viimane_nr_frame.pack(pady=10)
    
    olnud_nr = tk.Frame(viimane_nr_frame, height=200, width= 250, bd=1, relief="solid", bg="lightblue")
    olnud_nr.pack(pady=5)

    numbrid = tk.Label(olnud_nr, text="", bg="lightblue")
    numbrid.pack()

    viimane_nr = tk.Label(viimane_nr_frame, text="Viimane loositud number:", bg="lightblue")
    viimane_nr.pack(pady=20)

    loosimine = tk.Button(viimane_nr_frame, text="Loosi number", command=numbri_loosimine, font=("Arial", 14), bg="red", fg="white")
    loosimine.pack(pady=10)


numbrid_valikus = list(range(1, 76))
numbrid_loositud = []

def numbri_loosimine():
    suvaline_nr = random.choice(numbrid_valikus)
    numbrid_valikus.remove(suvaline_nr)
    numbrid_loositud.append(suvaline_nr)
    viimane_nr.config(text=f"Viimane loositud number: {suvaline_nr}")
    numbrid.config(text=f"Loositud numbrid: {', '.join(map(str, numbrid_loositud))}")

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
lugeja_frame = tk.Frame(aken, bd=2, relief="solid")
lugeja_frame.pack(pady=10)

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

def entry_value():
    global piirang
    piirang = piirarv.get()
    print(piirang)
    return piirang


sisesta = tk.Button(lugeja_frame, text="Sisesta mängijate arv", command=entry_value, font=("Arial", 14), bg="red", fg="white")
sisesta.pack(pady=20, padx=10, side ="right", expand= True, fill= "both")

uus = tk.Button(lugeja_frame, text="Uus kaart", command=kuva_bingo_kaart, font=("Arial", 14), bg="red", fg="white")
uus.pack(pady=20, padx=10, side ="right", expand= True, fill= "both")

start = tk.Button(lugeja_frame, text="Alusta mängu", command=mängu_alustamine, font=("Arial", 14), bg="red", fg="white")
start.pack(pady=20, padx=10, side ="right", expand= True, fill= "both")

piirarv = tk.Entry(lugeja_frame, font=("Arial", 14), bg="white", fg="black", width=15)
piirarv.pack(pady=20, padx=10, side ="right", expand= True, fill= "both")
piirarv.insert(0, "Mängijate arv")
lugeja = 0



aken.mainloop()