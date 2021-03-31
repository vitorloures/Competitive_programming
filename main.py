i = 0
# Inicializa sequencia de Fibonacci: a0 e a1
fibonacci = [1, 1]

while i < 10:
    # Enunciado explícito da sequencia de Fibonacci para maior clareza de código
    # a_n = a_{n-1} + a_{n-2}
    prox_elem = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(prox_elem)
    i += 1

print(f"Sequencia de Fibonacci, de a0 a an: {fibonacci}")
