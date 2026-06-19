import re


def choose_sets(universe, sets):
	remaining = set(universe)
	selected_sets = []

	while remaining:
		current_set = max(sets, key=lambda values: len(remaining.intersection(values)))
		covered_elements = remaining.intersection(current_set)

		if not covered_elements:
			break

		selected_sets.append(current_set)
		remaining -= covered_elements
		sets.remove(current_set)

	return selected_sets


universe = [int(value) for value in re.findall(r"-?\d+", input())]
number_of_sets = int(input())
sets = []

for _ in range(number_of_sets):
	sets.append([int(value) for value in re.findall(r"-?\d+", input())])

result = choose_sets(universe, sets)

print(f"Sets to take ({len(result)}):")
for current_set in result:
	formatted_set = ", ".join(str(value) for value in current_set)
	print(f"{{ {formatted_set} }}")
