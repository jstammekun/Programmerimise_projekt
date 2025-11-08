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
# Väljastan bingo kaardi
print(" B | I | N | G | O ")
print("---------------------")
for i in range(5):
    print(f"{b_rida[i]} | {i_rida[i]} | {n_rida[i]} | {g_rida[i]} | {o_rida[i]} ")
    