diction_of_cities = {
    1: "Amritsar",
    2: "Chandigarh",
    3: "Ludhiana"
}
y = int(input("Enter a number: "))
if y in diction_of_cities:
    print(diction_of_cities[y])
else:
    print("Your city is not registered")
    print("To register your city, Please follow the below instructions: ")
    x =  input("Please enter your city: ").strip().title()
    if x in diction_of_cities.values():
        print("Your city is registered, Please look at the list provided and find the number assigned to your city!")
    else:
        print(x)
        z = max(diction_of_cities.keys())
        diction_of_cities[z + 1] = x
                

print(diction_of_cities)