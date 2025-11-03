import tkinter as tk
from tkinter import messagebox
import random

b_rida_valikud = list(range(1, 16))
i_rida_valikud = list(range(16, 31))
n_rida_valikud = list(range(31, 46))
g_rida_valikud = list(range(46, 61))
o_rida_valikud = list(range(61, 76))

b_rida = []
i_rida = []
n_rida = []
g_rida = []
o_rida = []


for i in range(6):

    suvaline_b = random.choice(b_rida_valikud)
    suvaline_i = random.choice(i_rida_valikud)
    suvaline_n = random.choice(n_rida_valikud)
    suvaline_g = random.choice(g_rida_valikud)
    suvaline_o = random.choice(o_rida_valikud)

    if suvaline_b not in b_rida:
        b_rida.append(suvaline_b)
    else:
        b_rida_valikud.remove(suvaline_b)
        i -= 1

    if suvaline_i not in i_rida:
        i_rida.append(suvaline_i)
    else:
        i_rida_valikud.remove(suvaline_i)
        i -= 1

    if suvaline_n not in n_rida:
        n_rida.append(suvaline_n)
    else:
        n_rida_valikud.remove(suvaline_n)
        i -= 1

    if suvaline_g not in g_rida:
        g_rida.append(suvaline_g)
    else:
        g_rida_valikud.remove(suvaline_g)
        i -= 1

    if suvaline_o not in o_rida:
        o_rida.append(suvaline_o)   
    else:
        o_rida_valikud.remove(suvaline_o)
        i -= 1

print(" B | I | N | G | O ")
print("---------------------")
for i in range(5):
    print(f"{b_rida[i]} | {i_rida[i]} | {n_rida[i]} | {g_rida[i]} | {o_rida[i]} ")
    