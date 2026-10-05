def agent():
    log = []

    for i in range(3):
        log.append(f"Step {i + 1}: Agent executed")

    return log

result = agent()

for item in result:
    print(item)