# Static Lists:

manos_de_ally = ["Enzo", "Brian", "Rhett"]
print(f"OG list: {manos_de_ally}")
sibling_ages = [11, 13, 13]
t_or_f = [True, False, True, False]
manos_de_ally.append("6'3 poly dude")
mix_and_match = [67, "LeBron James", True, 6767, "Vienna LaRose"]

print(f"New list: {manos_de_ally}")
print(sibling_ages)
print(t_or_f)

unordered_list = [51, 85, 5, 0, 6]
print(f'unordered list: {unordered_list}')
unordered_list.sort()
print(f'ordered list: {unordered_list}')

for age in sibling_ages:
    print(f"This person is my younger brother")


# Dynamic Lists:

kool_people = []
print(f"OG list: {kool_people}")

kool_people.append("Kendrick Lamar")
kool_people.append("Michael Jackson")
kool_people.append("Cristiano Ronaldo")
print(f"New list: {kool_people}")
kool_people.insert(0, "Michael Jordan")
print(f"New list #2: {kool_people}")

kool_people.remove("Kendrick Lamar")
print(f"New list #3: {kool_people}")
kool_people.pop()
print(f"New list #4: {kool_people}")

for i in range(2):
    print("You're a pretty awesome person.")

for i in range(0, 8):
    print(f"Loop count innit: {i}")

for i in range(0, 12, 2):
    print(f"An interesting loop count by 2: {i}")    