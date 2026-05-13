# Static Lists:

manos_de_ally = ["Enzo", "Brian", "Rhett"]
print(f"OG list: {manos_de_ally}")
sibling_ages = [11, 13, 13]
t_or_f = [True, False, True, False]
manos_de_ally.append("6'3 poly dude")

print(f"New list: {manos_de_ally}")
print(sibling_ages)
print(t_or_f)

unordered_list = [51, 85, 5, 0, 6]
print(f'unordered list: {unordered_list}')
unordered_list.sort()
print(f'ordered list: {unordered_list}')

for age in sibling_ages:
    print(f"This person is my younger brother")