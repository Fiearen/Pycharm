names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]


first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)


first_initials = [name[0] for name in names]
print(first_initials)


full_initials = [(name.split()[0][0], name.split()[1][0]) for name in
                 full_names]
print(full_initials)


almost_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

numbers = [int(number) for number in almost_numbers]
print(numbers)


lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)
