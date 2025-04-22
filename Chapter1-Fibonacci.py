
def fib1(n: int) -> int:
    """
    Basicamente a representação mais simples de uma função recursiva, e não funciona.
    Porque? Porque acaba gerando um loop infinito. Em nenhum momento do programa está
    descrito um caso em que deve parar e retornar um valor. É necessário adicionar um
    chamado "base case", ou caso base.
    """
    return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(5))
