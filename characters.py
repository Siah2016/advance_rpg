my_hero = {
    "name": "Rimuru",
    "level": 1,
    "health": 100,
    "equipment": {"Mask", "Katana", "Long Jacket"},
    "skills":(("predator", 100), ("black lightning", 30), ("water blade",15)),
    "coins": {
        "copper": 0,
        "silver": 0,
        "gold": 0,        
    } 
}

enemy_one = {
    "name": "Black serpent",
    "level": 3,
    "health": 100,
    "equipment": {"dark shell"},

    "skills": (("poisonous breath", 25), ("sense heat source", 20)),
    "coins":{
        "copper": 35,
        "silver": 15,
        "gold": 4,
    }
}

enemy_two = {
    "name": "Black spider",
    "level": 5,
    "health": 100,
    "equipment": {"spider eggs"},

    "skills": (("sticky thread", 15), ("steel thread", 35)),
    "coins": {
        "copper": 40,
        "silver": 20,
        "gold": 8,
    }
}

enemy_three = {
    "name": "Giant Bat",
    "level": 7,
    "health": 100,
    "equipment": {"none"},

    "skills": (("drain", 40), ("ultrasonice wave", 25)),
    "coins": {
        "copper": 50,
        "silver": 25,
        "gold": 12
    }
}

final_boss = {
    "name": "Ifrit",
    "level": 10,
    "health": 200,
    "equipment": {"chains", "diamond belt", "ruby helmet"},

    "skills":(("hellfire", 80), ("body double", 50), ("flare circle", 40), ("combustion", 25)),
    "coins": {
        "copper": 100,
        "silver": 50,
        "gold": 25,
    }
}

enemy_list = [enemy_one, enemy_two, enemy_three, final_boss]