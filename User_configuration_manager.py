def add_setting(dicti, key_value):
    key, value = key_value[0].lower(), key_value[1].lower()
    if key in dicti:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    dicti[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dicti, key_value):
    key, value = key_value[0].lower(), key_value[1].lower()
    if key in dicti:
        dicti[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dicti, key):
    key = key.lower()
    if key in dicti:
        del dicti[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(dicti):
    if not dicti:
        return "No settings available."
    s = "Current User Settings:\n"
    for i in dicti:
        s += f"{i.capitalize()}: {dicti[i]}\n"
    return s

test_settings = {
    'theme': 'light',
    'notifications': 'enabled'
}
