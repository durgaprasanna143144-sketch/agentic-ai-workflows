def goal_agent(temp):
    goal = 72

    while temp != goal:
        if temp > goal:
            temp -= 1
        else:
            temp += 1

    return temp

print("Final temperature:", goal_agent(75))