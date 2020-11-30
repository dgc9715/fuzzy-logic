from fuzzy_system import FuzzySet

class min_composition:
    def __init__(self, aval, func):
        self.aval = aval
        self.func = func
    def __call__(self, values):
        return min(self.aval, self.func(values))

class product_composition:
    def __init__(self, aval, func):
        self.aval = aval
        self.func = func
    def __call__(self, values):
        return self.aval * self.func(values)

# Mamdani
def mamdani(fuzzy_system, values):
    result = []
    for a, c in fuzzy_system.rules:
        aval = a(values)
        result.append(min_composition(aval, c.membership_function))

    return FuzzySet(fuzzy_system.rules[0][1].name, lambda _values: max(func(_values) for func in result))

# Larsen
def larsen(fuzzy_system, values):
    result = []
    for a, c in fuzzy_system.rules:
        aval = a(values)
        result.append(product_composition(aval, c.membership_function))

    return FuzzySet(fuzzy_system.rules[0][1].name, lambda _values: max(func(_values) for func in result))
