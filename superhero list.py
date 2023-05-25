# create a list
# ask user for their liked super hero 5 times
# print all 5 superhero names
# ask which superhero they want to remove
# remove that superhero and print the remaining list
# ask them the index of superhero they want to remove and print the list after removing

superhero = []
for i in range(5):
 names = input("what superheroes do you like?")
superhero.append(names)
print(superhero)
rn = input("what superhero do you want to remove?")
superhero.remove(rn)
print(superhero)
popped = int(input("what index do you want to remove?"))
superhero.pop(popped)
print(superhero)

for i in range(10):
    n = [int(input("tell me a random number"))]
