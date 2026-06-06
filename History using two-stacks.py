def simulate_browser(commands):
    back = []
    forward = []
    history = []
    current = "Home"

    for i in commands:
        if "VISIT" in i:
            back.append(current)
            current = i.split()[1]
            forward.clear()
        elif i == "BACK":
            if len(back) > 0:
                forward.append(current)
                current = back.pop()
        elif i == "FORWARD":
            if len(forward) > 0:
                back.append(current)
                current = forward.pop()
        elif i == "CURRENT":
            history.append(current)

    return history
