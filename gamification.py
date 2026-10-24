LEVEL_THRESHOLDS = {
    2: 100,
    3: 250,
    4: 500
}

def get_level(xp):
    """Повертає рівень користувача на основі кількості XP."""
    current_level = 1
    for level, threshold in LEVEL_THRESHOLDS.items():
        if xp >= threshold:
            current_level = level
    return current_level

def add_xp(user, xp_amount):
    """Додає XP користувачу та оновлює його рівень."""
    user['xp'] += xp_amount
    new_level = get_level(user['xp'])
    
    if new_level > user['level']:
        user['level'] = new_level
        print(f"User leveled up to: {user['level']}")
        
    return user