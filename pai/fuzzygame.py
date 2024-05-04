#fuzzygame
def fuzzy_union(A, B):
    union = []
    for x in A:
        for y in B:
            if x[0] == y[0]:
                union.append((x[0], max(x[1], y[1])))
                break
        else:
            union.append(x)
    for y in B:
        for x in A:
            if x[0] == y[0]:
                break
        else:
            union.append(y)  
    return union
def fuzzy_intersection(A, B):
    intersection = []
    for x in A:
        for y in B:
            if x[0] == y[0]:
                intersection.append((x[0], min(x[1], y[1])))
                break
    return intersection
# Example fuzzy sets
A = [('a', 0.7), ('b', 0.5), ('c', 0.3)]
B = [('a', 0.4), ('d', 0.6), ('e', 0.2)]
# Computing union and intersection
union = fuzzy_union(A, B)
intersection = fuzzy_intersection(A, B)
# Output
print("Fuzzy Union:", union)
print("Fuzzy Intersection:", intersection)
