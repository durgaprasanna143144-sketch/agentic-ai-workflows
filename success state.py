def agent():
    temperature = 72

    if temperature == 72:
        return {
            "status": "success",
            "message": "Goal reached"
        }
    else:
        return {
            "status": "failure",
            "message": "Goal not reached"
        }

print(agent())