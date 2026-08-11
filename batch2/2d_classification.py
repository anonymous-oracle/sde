# 2D classification

def classify_points(points):
    labels = []
    for x, y in points:
        if y - x**2 + 4 >= 0:
            labels.append(1)
        else:
            labels.append(-1)
    return labels

if __name__ == "__main__":
    points = [(0, -5), (2, 1)]
    labels = classify_points(points)
    print(labels)  # Output: [-1, 1]