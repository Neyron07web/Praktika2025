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

