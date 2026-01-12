# GNB - 1st - Lists Types Notes

shawties = ["Emmie", "Sophie", "Elijah", "Annie", "Emily", "Isabel"]

print(shawties[0])
shawties[-1] = "Jordan" #changes thing in that vertex


print(shawties)

#Tuple

fave_food = ("Jollof Rice", "Platanos Fritos", "Fried Chicken", "Fries", "Granola")

fave_food[1] = "Mango"

#Set

countries = {"Nigeria", "Spain", "Columbia", "France", "England", "Mali", "Samoa", "Tonga"}

countries.add("Uzbekistan")
countries.remove("England")

for country in countries:
    print(country)
    if country == "France":
        print("Bounjour, madame")