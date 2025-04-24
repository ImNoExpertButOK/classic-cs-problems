from typing import Dict
from functools import lru_cache

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
    volta" na stack, com um valor atualizado. Qual o problema? Com valores maiores essa
    abordagem logo se torna insustentável, já que cada chamada da função resulta em duas outras
    chamadas da mesma função, aumentando o numero de chamadas exponencialmente. Um exemplo:
    Computar o vigésimo elemento desse conjunto de fibonacci usando esta função resultaria em
    21891 chamadas!
    """
    if n < 2:
        return n
    else:
        return fib2(n - 2) + fib2(n - 1)

def fib3(n: int) -> int:
    """
    Aqui o autor introduz o conceito de memoização, que é a ideia de guardar o resultado
    de tarefas computacionais para consulta futura, para que a mesma tarefa não seja repetida.
    Neste caso a ideia é registrar o resultado cada vez que computamos um novo valor na posição
    de n da sequência e realizar a computação em cima deste valor. Aqui então criamos um
    dicionário que relaciona a posição n com seu valor computado e incluímos os dois primeiros
    valores, nossos casos base. Caso o valor n não esteja no dicionário, seguimos em frente com
    o processo. 
    """
    
    memo: Dict[int, int] = {0: 0, 1: 1} 

    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)

    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    """
    Aqui usamos de uma biblioteca padrão do Python para fazer a memoização automática,
    exatamente como fizemos com fib3(). O lru_cache guarda o valor retornado pela função
    toda vez que esse valor for novo.
    """
    if n < 2:
        return n
    else:
        return fib4(n - 2) + fib4(n - 1)

def fib5(n: int) -> int:
    """
    Aqui o autor muda para uma abordagem iterativa, ao invés de recursiva. Estabelece
    duas variáveis, uma para cada valor, e faz um variable swapping para atualizar o
    valor a cada rodada do loop. Pessoalmente não sou super fã dessa abordagem hiper-
    concisa. O autor ainda diz que todo problema que pode ser resolvido de maneira
    recursiva pode ser resolvido de maneira iterativa.
    """
    if n == 0:
        return n
    else:
        last: int = 0
        next: int = 1

        for _ in range(1, n):
            last, next = next, last + next
        return next


def fib6(n: int) -> int:
    """
        Finalmente, o autor usa um generator para não só produzir o valor final, mas
        ser capaz de retornar cada número gerado se colocados em um loop.
    """
    yield 0
    
    if n > 0:
        yield 1
        last: int = 0
        next: int = 1

        for _ in range(1, n):
            last, next = next, last + next
            yield next

if __name__ == "__main__":
    print(fib5(20))
    for i in fib6(20):
        print(i)
