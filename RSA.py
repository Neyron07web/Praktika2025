def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception("Обратного элемента не существует.")
    return x % phi

def find_coprime(phi):
    """Автоматически находит минимальное e > 1, такое что gcd(e, phi) == 1"""
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            return e
    raise Exception("Не удалось найти подходящее значение e.")

def generate_keys(p, q):
    print("\n Шаг 1: Вычисляем n и φ(n)")
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = {p} * {q} = {n}")
    print(f"φ(n) = ({p - 1}) * ({q - 1}) = {phi}")

    print("\n🔍 Шаг 2: Ищем e, взаимно простое с φ(n)")
    e = find_coprime(phi)
    print(f" Подобрано e = {e}")

    print("\n Шаг 3: Вычисляем d, такое что (e * d) % φ(n) = 1")
    d = mod_inverse(e, phi)
    print(f"d = {d}, так как {e} * {d} ≡ 1 (mod {phi})")

    return (e, n), (d, n), phi



