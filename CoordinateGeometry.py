import math

points = [(3,4),(0,0),(-1,2),(5,-3),(3,4),(1,1),(-4,-4),(2,0)]


def distance(point):
    x, y = point
    return math.hypot(x, y)


def closestToOrigin():
    closest = min(points, key=distance)
    print(f"Cel mai apropiat de origine: {closest}")
    return closest


def firstQuadrant():
    result = [p for p in points if p[0] > 0 and p[1] > 0]
    print(f"\nPuncte in primul cadran: {result}")
    return result


def sortByDistance():
    sorted_points = sorted(points, key=distance)
    print(f"\nPuncte sortate dupa distanta: {sorted_points}")
    return sorted_points


def boundingBox():
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    box = (min(xs), min(ys), max(xs), max(ys))
    print(f"\nBounding box (min_x, min_y, max_x, max_y): {box}")
    return box


def duplicatePoints():
    seen = set()
    duplicates = set()
    for p in points:
        if p in seen:
            duplicates.add(p)
        else:
            seen.add(p)
    print(f"\nPuncte duplicate: {duplicates}")
    return duplicates


if __name__ == '__main__':
    closestToOrigin()
    firstQuadrant()
    sortByDistance()
    boundingBox()
    duplicatePoints()