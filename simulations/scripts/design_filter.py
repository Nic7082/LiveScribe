# Designing resistor and capacitor values for low pass and high pass sallen-key filters

import math
import itertools
import heapq
#list of potential resistor values
base_resistor_values = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
multipliers = [1000, 10000]

resistor_values = []
for r in base_resistor_values:
    for m in multipliers:
        resistor_values.append(r*m)

#potential capacitor values
capacitor_values = [0.01e-6, 0.47e-6, 0.1e-6, 1e-9, 0.1e-9, 0.68e-9, 0.15e-6, 6.8e-9, 1e-6]

#combinations
rc_combinations = itertools.product(resistor_values, resistor_values, capacitor_values, capacitor_values)

#constraints
quality_factor = 0.707
high_cutoff = 500
low_cutoff = 120

#equations
def cutoff_frequency(resistor1, resistor2, capacitor1, capacitor2):
    return 1/(2 * math.pi  * math.sqrt(resistor1 * resistor2 * capacitor1 * capacitor2))
def quality_factor_low(resistor1, resistor2, capacitor1, capacitor2):
    return (math.sqrt(resistor1 * resistor2 * capacitor1 * capacitor2))/(resistor1 * capacitor1 + resistor2 * capacitor1)
def quality_factor_high(resistor1, resistor2, capacitor1, capacitor2):
    return (math.sqrt(resistor1 * resistor2 * capacitor1 * capacitor2))/(resistor2 * capacitor2 + resistor2 * capacitor1)

#max-heaps to store top 5 best combinations
lp_best_combos = []
hp_best_combos = []

for combos in rc_combinations:
    r1, r2, c1, c2 = combos
    cutoff_freq = cutoff_frequency(r1,r2,c1,c2)
    q_low = quality_factor_low(r1,r2,c1,c2)
    q_high = quality_factor_high(r1,r2,c1,c2)

    # Evaluating Low Pass Filter Constraint Compliance
    if q_low > 0.5:
        cutoffFreqError = 100 * abs(cutoff_freq - low_cutoff) / low_cutoff
        q_low_error = 100 * abs(q_low - quality_factor) / quality_factor
        lp_totalError = cutoffFreqError + q_low_error

        # Max-heap logic: -lp_bestCombos[0][0] represents the worst error in our top 5
        if len(lp_best_combos) < 5:
            heapq.heappush(lp_best_combos, (-lp_totalError, (r1, r2, c1, c2, cutoff_freq, q_low)))
        elif lp_totalError < -lp_best_combos[0][0]:
            heapq.heappushpop(lp_best_combos, (-lp_totalError, (r1, r2, c1, c2, cutoff_freq, q_low)))
    else:
        continue

    # Evaluating High Pass Filter Constraint Compliance
    if q_high > 0.5:
        highCutoffFreqError = 100 * abs(cutoff_freq - high_cutoff) / high_cutoff
        highPassQError = 100 * abs(q_high - quality_factor) / quality_factor
        hp_totalError = highCutoffFreqError + highPassQError

        # Max-heap logic for High Pass
        if len(hp_best_combos) < 5:
            heapq.heappush(hp_best_combos, (-hp_totalError, (r1, r2, c1, c2, cutoff_freq, q_high)))
        elif hp_totalError < -hp_best_combos[0][0]:
            heapq.heappushpop(hp_best_combos, (-hp_totalError, (r1, r2, c1, c2, cutoff_freq, q_high)))
    else:
        continue


# Printing Results
print("\n--- Top 5 Low-Pass Filter Combinations ---")
for error, data in sorted(lp_best_combos, key=lambda x: -x[0]):
    R1, R2, C1, C2, freq, q = data
    print(
        f"Total Error: {-error:.2f}% | R1: {R1} ohms, R2: {R2} ohms, C1: {C1}F, C2: {C2}F | Fc: {freq:.2f}Hz, Q: {q:.3f}")

print("\n--- Top 5 High-Pass Filter Combinations ---")
for error, data in sorted(hp_best_combos, key=lambda x: -x[0]):
    R1, R2, C1, C2, freq, q = data
    print(
        f"Total Error: {-error:.2f}% | R1: {R1} ohms, R2: {R2} ohms, C1: {C1}F, C2: {C2}F | Fc: {freq:.2f}Hz, Q: {q:.3f}")


