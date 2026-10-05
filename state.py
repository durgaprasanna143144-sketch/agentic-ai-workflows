state = {
    "done": False,
    "steps": 0
}

for i in range(5):
    state["steps"] += 1
    print("Step:", state["steps"])

    if state["steps"] == 5:
        state["done"] = True

print("State:", state)