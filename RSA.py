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
    print("\nШаг 1: Вычисляем n и φ(n)")
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = {p} * {q} = {n}")
    print(f"φ(n) = {p - 1} * {q - 1} = {phi}")

    print("\nШаг 2: Ищем e, взаимно простое с φ(n)")
    e = find_coprime(phi)
    print(f" Подобрано e = {e}")

    print("\nШаг 3: Вычисляем d, такое что (e * d) % φ(n) = 1")
    d = mod_inverse(e, phi)
    print(f"d = {d}, так как {e} * {d} ≡ 1 (mod {phi})")

    return (e, n), (d, n), phi

def encrypt(M, e, n):
    print(f"\nШаг 4: Шифруем сообщение M = {M}")
    C = pow(M, e, n)
    print(f"C = M^e mod n = {M}^{e} mod {n} = {C}")
    return C

def decrypt(C, d, n):
    print(f"\nШаг 5: Расшифровываем сообщение C = {C}")
    M = pow(C, d, n)
    print(f"M = C^d mod n = {C}^{d} mod {n} = {M}")
    return M

def main():
    print("=== RSA ===")

    try:
        p = int(input("Введите простое число p: "))
        q = int(input("Введите простое число q: "))
        M = int(input("Введите сообщение (целое число) M для шифрования: "))

        public_key, private_key, phi = generate_keys(p, q)

        e, n = public_key
        d, _ = private_key

        C = encrypt(M, e, n)
        M_decrypted = decrypt(C, d, n)

        print("\n=== ИТОГ ===")
        print(f"Открытый ключ: (e={e}, n={n})")
        print(f"Закрытый ключ: (d={d}, n={n})")
        print(f"Зашифрованное сообщение: C = {C}")
        print(f"Расшифрованное сообщение: M = {M_decrypted}")

    except ValueError as ve:
        print("\n Ошибка ввода:", ve)
    except Exception as ex:
        print("\n Ошибка:", ex)

if __name__ == "__main__":
    main()

