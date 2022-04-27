def calculateBadge(level, proLevel):
    # i know you can probably use case statements here but i'm using if statements because it's easier. -Inferno
    # correct me if I'm wrong, but case statements aren't a thing in Python - Pivin
    if level >= 2147483647:
        return "What?"
    elif level >= 1000:
        return "Grand"
    elif level >= 500:
        return "Adept"
    elif level >= 250:
        return "Master"
    elif level >= 100:
        return "Expert"
    elif level >= proLevel:
        return "Pro"
    elif level < proLevel:
        return ""
    else:
        return "Calculation error."
