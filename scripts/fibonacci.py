# Retorna os X primeiros números da sequência de Fibonnaci
def fibonacci(qtt:int):
    sequence = [0,1]

    i = 2

    while i < qtt:
        sequence.append(sequence[i-1] + sequence[i-2])
        print(sequence)
        i += 1

    return sequence