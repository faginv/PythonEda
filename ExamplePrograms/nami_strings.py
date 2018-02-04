name = "Nami"
empty_string = str()
greeting = "Hi"
white_space = "\t"
luffy = "\"nami, you're always my friend.\""

print("2 times name + empty_string + 3 times greeting is: ", name * 2 + empty_string + greeting * 3)
print("The length of the name: ", len(name))
print("zo in Nami is ", "zo" in name)
print("am in Nami is not ", "zo" in name)
print("Nami is alphanumeric: ", name.isalnum())
print("Nami is alphabets only: ", name.isalpha())
print("Nami is digits only: ", name.isdigit())
print("white_space is only whitespace: ", white_space.isspace())
print(luffy, " is ends with end.: ", luffy.endswith("end.")) 
print(luffy, " is ends with end.\": ", luffy.endswith("end.\"")) 
print(luffy, " is starts with \"nam: ", luffy.startswith("\"nam")) 
print(luffy, " has count of 'a': ", luffy.count("a"))
print(luffy.title())
print(luffy.upper())
print(luffy.upper().lower())
print(luffy.replace("always", "not"))
print("luffy[:] = ", luffy[:])
print("luffy[:9] = ", luffy[:9])
print("luffy[4:] = ", luffy[4:])
print("luffy[4:9] = ", luffy[4:9])
print("luffy[1:-1] = ", luffy[1:-1])


