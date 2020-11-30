# Mean of Maximum Method (mom)
def mom(fuzzy_set, universe):
    result = [(fuzzy_set.membership_function(u), u) for u in universe]
    max_val = max(result)[0]
    s = 0
    t = 0
    for val, u in result:
        if val == max_val:
            s += u
            t += 1
    return s / t

# Center of Area Method (coa)
def coa(fuzzy_set, universe):
    result = [(fuzzy_set.membership_function(u), u) for u in universe]
    a = 0
    b = 0
    for val, u in result:
        a += val * u
        b += val
    if b:
        return a / b
    return (min(result) + max(result)) / 2

# Bisector of Area (boa)
def boa(fuzzy_set, universe):
    result = [(fuzzy_set.membership_function(u), u) for u in universe]
    
    area = 0
    lval, lu = result[0]
    for val, u in result[1:]:
        area += (u - lu) * (val + lval) / 2
        lval = val
        lu = u

    area /= 2
    lval, lu = result[0]
    for val, u in result[1:]:
        area -= (u - lu) * (val + lval) / 2
        lval = val
        lu = u
        if area <= 0:
            return u
    return universe[-1]
