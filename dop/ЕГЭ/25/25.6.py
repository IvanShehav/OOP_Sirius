def find_divisors(n):
    """Возвращает список делителей числа n, не включая само число."""
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors.discard(n)  # исключаем само число
    return sorted(divisors, reverse=True)

def M(N):
    divisors = find_divisors(N)
    if len(divisors) < 5:
        return 0
    return sum(divisors[:5])

# Перебираем числа больше 4_000_000
count = 0
N = 4000001
results = []

while count < 7:
    m_value = M(N)
    if m_value > 0 and m_value % 10 == 0:
        results.append((N, m_value))
        count += 1
    N += 1

# Выводим результаты
for n, m in results:
    print(f"{n} {m}")
