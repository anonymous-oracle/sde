import numpy as np


def normalize_ref(data: list[float]) -> list[float]:
    if len(data) == 0:
        return data
    xmax = data[0]
    xmin = data[0]
    for idx in range(len(data)):
        x = data[idx]
        if x > xmax:
            xmax = x
        if x < xmin:
            xmin = x
    if xmax == xmin:
        return data
    for idx in range(len(data)):
        x = data[idx]
        x = (x - xmin)/(xmax - xmin)
        data[idx] = x
    return data

def normalize_vec(arr: np.ndarray) -> np.ndarray:
    if arr.size == 0:
        return arr
    xmax = np.max(arr)
    xmin = np.min(arr)
    if xmax == xmin:
        return arr
    return (arr - xmin) / (xmax - xmin)


if __name__ == "__main__":
    data = [1.0, np.nan, np.inf]
    arr = np.array(data)
    # We use np.allclose to compare because floating point arithmetic can introduce small rounding errors.
    print(normalize_ref(data.copy()))
    print(normalize_vec(arr))
    np.allclose(normalize_ref(data.copy()), normalize_vec(arr))

