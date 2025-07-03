import dearpygui.dearpygui as dpg
import random

# Константы
p, g = 23, 5 # Простое число и его первообразный корень

# Глобальные переменные
a = b = A = B = Ka = Kb = 0

def generate_keys():
    global a, b, A, B
    a, b = random.randint(2, p-2), random.randint(2, p-2) # Приватные ключи
    A, B = pow(g, a, p), pow(g, b, p) # Публичные ключи
    update_display()

def calculate_secret():
    global Ka, Kb
    Ka, Kb = pow(B, a, p), pow(A, b, p) # Общий секрет
    update_display()

