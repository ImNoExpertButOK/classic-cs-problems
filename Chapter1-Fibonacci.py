
def fib1(n: int) -> int:
    """
    Basicamente a representação mais simples de uma função recursiva, e não funciona.
    Porque? Porque acaba gerando um loop infinito. Em nenhum momento do programa está
    descrito um caso em que deve parar e retornar um valor. É necessário adicionar um
    chamado "base case", ou caso base.
    """
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    """
    Agora adicionamos o caso base, na forma do condicional if. Como a função chamará a si mesma
    repetidamente com valores de n cada vez menores, eventualmente o valor será 1 ou 0, os dois
    casos aonde o valor de n seria ele mesmo. Assim é como se o programa começasse a "andar de
    volta" na stack, com um valor atualizado.
    """
    if n < 2:
        return n
    else:
        return fib2(n - 2) + fib2(n - 1)


if __name__ == "__main__":
    print(fib2(6))
