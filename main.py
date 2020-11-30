from fuzzy_system import *
from fuzzy_inference import *
from fuzzy_number import *
from defuzzification import *
from matplotlib import pyplot
import random

def polt_fuzzy_set(fuzzy_set, universe, ylabel, label, path=None):
    result = [fuzzy_set.membership_function(u) for u in universe]
    pyplot.figure()
    pyplot.xlabel(fuzzy_set.name)
    pyplot.ylabel(ylabel)
    pyplot.plot(universe, result, label=label)
    if path:
        pyplot.savefig(path)
    else:
        pyplot.show()

soil_quality = LinguisticVariable('soil_quality',
                                    { 'low':FuzzyTriangular(-1, 0, 100),
                                    'medium':FuzzyTrapezoidal(0, 40, 60, 100),
                                    'high':FuzzyTriangular(0, 100, 101) })

sunlight_exposure = LinguisticVariable('sunlight_exposure',
                                    { 'low':FuzzyBell(0, 15),
                                    'medium':FuzzyBell(50, 15),
                                    'high':FuzzyBell(100, 15) })

watering_intensity = LinguisticVariable('watering_intensity',
                                    { 'low':FuzzyPentagonal(-2, -1, 0, 50, 100, 1.0, 0.2),
                                    'medium':FuzzyPentagonal(10, 30, 50, 70, 90, 0.7, 0.7),
                                    'high':FuzzyPentagonal(0, 50, 100, 101, 102, 0.2, 1.0) })

growth = LinguisticVariable('growth',
                                    { 'low':FuzzyPentagonal(-2, -1, 0, 50, 100, 1.0, 0.1),
                                    'medium':FuzzyBell(50, 10),
                                    'high':FuzzyPentagonal(0, 50, 100, 101, 102, 0.1, 1.0) })

def generate_membership_function_plots():
    polt_fuzzy_set(soil_quality.low, range(101), 'low', 'membership function', './images/soil_quality_low')
    polt_fuzzy_set(soil_quality.medium, range(101), 'medium', 'membership function', './images/soil_quality_medium')
    polt_fuzzy_set(soil_quality.high, range(101), 'high', 'membership function', './images/soil_quality_high')

    polt_fuzzy_set(sunlight_exposure.low, range(101), 'low', 'membership function', './images/sunlight_exposure_low')
    polt_fuzzy_set(sunlight_exposure.medium, range(101), 'medium', 'membership function', './images/sunlight_exposure_medium')
    polt_fuzzy_set(sunlight_exposure.high, range(101), 'high', 'membership function', './images/sunlight_exposure_high')

    polt_fuzzy_set(watering_intensity.low, range(101), 'low', 'membership function', './images/watering_intensity_low')
    polt_fuzzy_set(watering_intensity.medium, range(101), 'medium', 'membership function', './images/watering_intensity_medium')
    polt_fuzzy_set(watering_intensity.high, range(101), 'high', 'membership function', './images/watering_intensity_high')

    polt_fuzzy_set(growth.low, range(101), 'low', 'membership function', './images/growth_low')
    polt_fuzzy_set(growth.medium, range(101), 'medium', 'membership function', './images/growth_medium')
    polt_fuzzy_set(growth.high, range(101), 'high', 'membership function', './images/growth_high')

generate_membership_function_plots()

plant = FuzzySystem([
    (FuzzyOr(
            FuzzyOr(
                    FuzzyAnd(soil_quality.low, sunlight_exposure.low),
                    FuzzyAnd(soil_quality.low, watering_intensity.low)
                    ),
            FuzzyAnd(sunlight_exposure.low, watering_intensity.low)), growth.low),
    (FuzzyOr(
            FuzzyOr(
                    FuzzyAnd(soil_quality.medium, sunlight_exposure.medium),
                    FuzzyAnd(soil_quality.medium, watering_intensity.medium)
                    ),
            FuzzyAnd(sunlight_exposure.medium, watering_intensity.medium)), growth.medium),
    (FuzzyOr(
            FuzzyOr(
                    FuzzyAnd(soil_quality.high, sunlight_exposure.high),
                    FuzzyAnd(soil_quality.high, watering_intensity.high)
                    ),
            FuzzyAnd(sunlight_exposure.high, watering_intensity.high)), growth.high)
])

soil_quality_v = 50
sunlight_exposure_v = 50
watering_intensity_v = 50
points = 10000

random.seed(111111)

sim1 = []
sim2 = []

for day in range(100):
    values = {'soil_quality':soil_quality_v, 'sunlight_exposure':sunlight_exposure_v, 'watering_intensity':watering_intensity_v }
    
    mi = mamdani(plant, values)
    ln = larsen(plant, values)
    
    sim1.append(boa(mi, [100 * i / points for i in range(points+1)]))
    sim2.append(coa(ln, [100 * i / points for i in range(points+1)]))
    soil_quality_v += random.uniform(-10, +10)
    sunlight_exposure_v += (1 if random.uniform(0, 1) < 0.45 else -1) * random.normalvariate(5, 10)
    watering_intensity_v += (1 if random.uniform(0, 1) < 0.4 else -1) * random.gauss(5, 3)
    soil_quality_v = min(max(0, soil_quality_v), 100)
    sunlight_exposure_v = min(max(0, sunlight_exposure_v), 100)
    watering_intensity_v = min(max(0, watering_intensity_v), 100)

pyplot.figure()
pyplot.xlabel("Day")
pyplot.ylabel("Growth")
pyplot.plot(sim1, label="Mamdani and BOA")
pyplot.plot(sim2, label="Larsen and COA")
pyplot.legend()
pyplot.savefig('./images/growth.png')
