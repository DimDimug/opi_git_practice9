def add_xp(user, xp_amount):
    user['xp'] = user['xp'] + xp_amount
    if user['xp'] >= 100:
        user['level'] = 2
    if user['xp'] >= 250:
        user['level'] = 3
    if user['xp'] >= 500:
        user['level'] = 4
    print("User leveled up to:", user['level'])
    return user