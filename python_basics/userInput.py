def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temperature :"))
print(weather_condition(user_input))

name = input("Enter your name: ")
surname = input("Enter your last name: ")

message = "Hello %s %s" % (name, surname)
print(message)

message = f"Hello {name} {surname}"
print(message)


