person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# name of second child
print(type(person["children"]))
print(person["children"][1])

# the name of the cat
print(type(person["pets"]))
print(person["pets"]["cat"])

# use a for loop
for i in person["children"]:
    print(i)

    # print out the pets in this format:
    # Type of pet: dog name of pet: Fido
    for i, j in person["pets"].items():
        print(f"Type of pet: {i} name of pet: {j}")

# print(person.get("children")[1])
# print(person["children"][1])    alternative way to write line 11
