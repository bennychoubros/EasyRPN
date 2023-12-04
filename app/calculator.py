from collections import deque
import logging
 
def compute(operation: list) -> float:
    d = deque()
    for symbol in operation:
        if isinstance(symbol, int) or isinstance(symbol, float):
            d.append(symbol)
        elif isinstance(symbol, str):
            b, a = d.pop(), d.pop()
            expr = f"{a} {symbol} {b}"
            d.append(eval(expr))
        else:
            raise ValueError(f"Expression invalide: {symbol}")
        logging.debug(f"{d}  # {symbol}")
    return d.pop()