def add_setting(settings, new_setting):
    key = str(new_setting[0]).lower()
    value = str(new_setting[1]).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, new_setting):
    key = str(new_setting[0]).lower()
    value = str(new_setting[1]).lower()

    if key in settings:
        settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, new_setting):
    key = str(new_setting).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value.lower()}")

    return "\n".join(lines) + "\n"


test_settings = {'theme': 'dark', 'notifications': 'enabled',
                 'volume': 'high'}

print(view_settings(test_settings))