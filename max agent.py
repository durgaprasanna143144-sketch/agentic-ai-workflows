def agent(max_iters=10):
    count = 0

    while count < max_iters:
        print("Iteration:", count + 1)
        count += 1

    return "failure"

print(agent())