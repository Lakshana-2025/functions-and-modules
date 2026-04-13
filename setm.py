import set_module

set1_input = input("Enter elements for set 1 (separated by space): ").split()
set2_input = input("Enter elements for set 2 (separated by space): ").split()

s1 = set(set1_input)
s2 = set(set2_input)

print(f"Set 1: {s1}")
print(f"Set 2: {s2}")

print("Union:", set_module.sunion(s1, s2))
print("Intersection:", set_module.sintersection(s1, s2))
print("Difference (S1-S2):", set_module.sdifference(s1, s2))
print("Symmetric Difference:", set_module.ssymmetricdiff(s1, s2))
