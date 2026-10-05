def agent():
    temperature = 80

    for i in range(2):
        print("Step", i + 1)
        print("Temperature:", temperature)

        if temperature > 75:
            print("Action: COOL")
            temperature -= 5
        else:
            print("Action: IDLE")

agent()