from typing import Tuple, List

def predict(w, b, x: float):
    if not (isinstance(w, (float, int)) and isinstance(b, (float, int)) and isinstance(x, (float, int))):
        raise ValueError("Ensure correct data types")
    return (w * x) + b

def line_through(p1, p2: Tuple[float, float]):
    if not (
        isinstance(p1[0], (float, int))
        and isinstance(p1[1], (float, int))
        and isinstance(p2[0], (float, int))
        and isinstance(p2[1], (float, int))
    ):
        raise ValueError("Ensure correct data types")
    w = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - (w * p1[0])
    return w, b

def sse(w, b: float, xs, ys: List[float]):
    if (not (isinstance(w, (float, int)) and isinstance(b, (float, int)))) or (not (isinstance(xs, list) and isinstance(ys, list))):
        raise ValueError("Ensure correct data types")
    if len(xs) != len(ys):
        raise ValueError("Data array lengths not matching")

    return sum([(y - predict(w, b, x))**2 for x, y in zip(xs, ys)])

def best_pair_line(xs, ys):
    if len(xs) < 2 or len(ys) < 2:
        raise ValueError("Insufficient data")
    if len(xs) != len(ys):
        raise ValueError("Data array lengths not matching")
    
    line_candidates = []
    w, b = line_through(*[(x,y) for x,y in zip(xs[:2], ys[:2])])
    for x, y in zip(xs, ys):
        line_candidates.append((w, b, sse(w, b, [x], [y])))
    return min(line_candidates, key= lambda x: x[-1])


w = 3
bs = [10, 10.25, 10.5, 10.75, 11]
print(predict(3, 10, 5))
print(line_through((1, 13), (2, 17)))
print(sse(3, 10.5, [1, 2, 3], [13, 17, 19]))
print(best_pair_line([1, 2, 3], [13, 17, 19]))
