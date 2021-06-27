import copy
INIT_EFFECTS = {
    'shield': 0,
    'poison': 0,
    'recharge': 0,
}
# INIT_STATS = {
#     'hp': 50,
#     'mana': 500,
#     'armor': 0,
#     'damage': 0,
#     'mana_spent': 0,
#     'fx': INIT_EFFECTS.copy(),
# }
# BOSS_STATS = {
#     'hp': 71,
#     'mana': 0,
#     'armor': 0,
#     'damage': 10,
#     'mana_spent': 0,
#     'fx': INIT_EFFECTS.copy(),
# }
INIT_STATS = {
    'hp': 10,
    'mana': 250,
    'armor': 0,
    'damage': 0,
    'mana_spent': 0,
    'fx': INIT_EFFECTS.copy(),
}
BOSS_STATS = {
    'hp': 13,
    'mana': 0,
    'armor': 0,
    'damage': 8,
    'mana_spent': 0,
    'fx': INIT_EFFECTS.copy(),
}
ABILITIES = {
    'magic_missle': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}

def recursive_find(me, boss):
    me = copy.deepcopy(me)
    boss = copy.deepcopy(boss)
    my_armor = me['armor']
    fx = me['fx']
    if fx['shield']:
        my_armor += 7
    if fx['poison']:
        boss['hp'] -= 3
        if boss['hp'] <= 0:
            return [['died to poison']]
    if fx['recharge']:
        me['mana'] += 101

    decrement_effects(me['fx'])

    possible = []
    for ab in ABILITIES.keys():
        t_me = copy.deepcopy(me)
        t_boss = copy.deepcopy(boss)
        fx = t_me['fx']
        if fx.get(ab, 0) > 0:
            continue

        if ab == 'magic_missle':
            apply_mana(t_me, 53)
            t_boss['hp'] -= 4
        elif ab == 'drain':
            apply_mana(t_me, 73)
            t_boss['hp'] -= 2
            t_me['hp'] += 2
        elif ab == 'shield':
            apply_mana(t_me, 113)
            fx['shield'] += 6
        elif ab == 'poison':
            apply_mana(t_me, 173)
            fx['poison'] += 6
        elif ab == 'recharge':
            apply_mana(t_me, 229)
            fx['recharge'] += 5

        if t_me['mana'] <= 0:
            continue
        elif t_boss['hp'] <= 0:
            possible.append([ab])
        else:
            # boss's turn
            my_armor = t_me['armor']
            if fx['shield']:
                my_armor += 7
            if fx['poison']:
                t_boss['hp'] -= 3
                if t_boss['hp'] <= 0:
                    return [['died to poison']]
            if fx['recharge']:
                t_me['mana'] += 101

            decrement_effects(t_me['fx'])

            t_me['hp'] -= max(t_boss['damage'] - my_armor, 1)
            if t_me['hp'] <= 0:
                continue

        next_abilities = recursive_find(t_me, t_boss)
        for x in next_abilities:
            possible.append([ab] + x)
    return possible

def decrement_effects(effects):
    for key, val in effects.items():
        effects[key] = max(0, val - 1)

def apply_mana(stats, amount: int):
    stats['mana'] -= amount
    stats['mana_spent'] += amount

def total_cost(abilities):
    return sum([ABILITIES.get(x, 0) for x in abilities])

out = recursive_find(INIT_STATS, BOSS_STATS)
print(len(out))
lowest = min(out, key=total_cost)
print(lowest)
print(total_cost(lowest))
