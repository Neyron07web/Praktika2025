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

# Кириллица
with dpg.font_registry():
    with dpg.font("C:/Users/Owner/Downloads/ofont.ru_Spell.ttf", 16) as font1:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
dpg.bind_font(font1)

with dpg.window(label="Diffie-Hellman", width=250, height=200):
    dpg.add_text("Обмен ключами Диффи-Хеллмана")
    dpg.add_text(f"p = {p}, g = {g}")
    dpg.add_button(label="Генерировать ключи", callback=generate_keys)
    dpg.add_button(label="Вычислить секрет", callback=calculate_secret)
    dpg.add_button(label="Сбросить", callback=reset)
    dpg.add_text("", tag="a")
    dpg.add_text("", tag="b")
    dpg.add_text("", tag="A")
    dpg.add_text("", tag="B")
    dpg.add_text("", tag="Ka")
    dpg.add_text("", tag="Kb")
    dpg.add_text("", tag="result", color=(0, 255, 0))
    dpg.create_context()

    dpg.create_viewport(title='Diffie-Hellman', width=450, height=350)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

    dpg.create_viewport(title='Diffie-Hellman', width=400, height=300)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()



