from logger import logging

def add(x, y):
    logging.debug("A operação de adição foi colocada em execução")
    return x + y

logging.debug("A operação de adição foi chamada")
add(5, 3)