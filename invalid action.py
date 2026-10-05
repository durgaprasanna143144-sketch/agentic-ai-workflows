def perform_action(action):
    valid_actions = ["COOL", "HEAT", "IDLE"]

    if action not in valid_actions:
        return {
            "error": "Invalid action",
            "action": action
        }

    return {
        "status": "success",
        "action": action
    }

print(perform_action("JUMP"))