# Basic operators
class FuzzyPredicate:
	def __call__(self, values):
		pass

class FuzzyOr(FuzzyPredicate):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs

	def __call__(self, values):
		return max(self.lhs(values), self.rhs(values))

class FuzzyAnd(FuzzyPredicate):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs

	def __call__(self, values):
		return min(self.lhs(values), self.rhs(values))

class FuzzyNegation(FuzzyPredicate):
	def __init__(self, predicate):
		self.predicate = predicate

	def __call__(self, values):
		return 1 - self.predicate(values)

# Fuzzy Set
class FuzzySet(FuzzyPredicate):
	def __init__(self, name, membership_function):
		self.name = name
		self.membership_function = membership_function
	
	def __call__(self, values):
		if isinstance(values, dict):
			return self.membership_function(values[self.name])
		return self.membership_function(values)

# Linguistic Variable
class LinguisticVariable:
	def __init__(self, name, values):
		self.name = name
		self.values = values

	def __getattr__(self, value):
		return FuzzySet(self.name, self.values[value])

# Fuzzy System
class FuzzySystem:
	def __init__(self, rules):
		self.rules = rules
