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
def update_display():
    dpg.set_value("a", f"Приватный ключ a: {a}")
    dpg.set_value("b", f"Приватный ключ b: {b}")
    dpg.set_value("A", f"Публичный ключ A: {A}")
    dpg.set_value("B", f"Публичный ключ B: {B}")
    dpg.set_value("Ka", f"Секрет a: {Ka}")
    dpg.set_value("Kb", f"Секрет b: {Kb}")
    dpg.set_value("result", "Совпали!" if Ka == Kb and Ka != 0 else "")

def reset():
    global a, b, A, B, Ka, Kb
    a = b = A = B = Ka = Kb = 0
    update_display()

# Создаем интерфейс
dpg.create_context()

