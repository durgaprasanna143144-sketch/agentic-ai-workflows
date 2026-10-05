def temperature_agent(temp):
    if temp > 100:
        return "COOL"
    else:
        return "IDLE"

temp = 120
print(temperature_agent(temp))