def fight(heroes, villain):
    for hero in heroes:
        if hero["category"] == villain["category"]:
            if hero["health"] >= villain["health"]:
                string = hero["name"] + " defeated the villain and now has a score of " + str(hero["score"]+1)
                return string
            else:
                villain["health"] -= int(hero["health"]/2)
    string = villain["name"] + " prevailed with " + str(float(villain["health"])) + "HP left"
    return string

print(fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 2000, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))