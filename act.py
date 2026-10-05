def agent():
    temperature = 80

    for i in range(3):
        print("Observe:", temperature)

        if temperature > 75:
            action = "COOL"
        else:
            action = "HEAT"

        print("Decide:", action)

        if action == "COOL":
            temperature -= 2
        else:
            temperature += 2

        print("Act: Temperature =", temperature)
        print()

agent()