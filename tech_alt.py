tech_alt = {
    "Quenched Blades I": {
        "cost": {
            1: 30e3,
            2: 75e3,
            3: 120e3,
            4: 165e3,
            5: 220e3,
        },
        "lvl": 0,
        "req": None,
    }
}
tech["Improved Bows I"] = tech["Quenched Blades I"]
tech["Mounted Combat Techniques I"] = tech["Quenched Blades I"]
tech["Improved Projectiles I"] = tech["Quenched Blades I"]

tech["Swift Marching I"] = {
    "cost": {
        1: 50e3,
        2: 100e3,
        3: 150e3,
        4: 200e3,
        5: 300e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Treaties I"] = {
    "cost": {
        1: 20e3,
        2: 40e3,
        3: 60e3,
        4: 80e3,
        5: 160e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Cultural Exchanage I"] = tech["Treaties I"]
tech["Larger Camps"] = {
    "cost": {
        1: 50e3,
        2: 100e3,
        3: 150e3,
        4: 200e3,
        5: 300e3,
    },
    "lvl": 0,
    "req": {3: {"Swift Marching I": 3}},
}
tech["Barbarian Reports I"] = {
    "cost": {
        1: 10e3,
        2: 20e3,
        3: 30e3,
        4: 40e3,
        5: 80e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Karaku Reports I"] = tech["Barbarian Reports I"]
tech["Skillful Operations I"] = {
    "cost": {
        1: 20e3,
        2: 40e3,
        3: 60e3,
        4: 80e3,
        5: 160e3,
    },
    "CCR": {
        1: 0.01,
        2: 0.02,
        3: 0.03,
        4: 0.04,
        5: 0.05,
    },
}
tech["Plunder I"] = tech["Treaties I"]
tech["Karaku's Gift I"] = tech["Treaties I"]
tech["Attack Formation"] = {
    "cost": {
        1: 100e3,
        2: 200e3,
        3: 300e3,
        4: 450e3,
        5: 600e3,
        6: 800e3,
        7: 1.2e6,
        8: 1.6e6,
        9: 2.0e6,
        10: 2.4e6,
    },
    "lvl": 0,
    "req": None,
}
cost1 = {
    1: 80e3,
    2: 120e3,
    3: 200e3,
    4: 240e3,
    5: 320e3,
    6: 400e3,
    7: 480e3,
    8: 560e3,
    9: 640e3,
    10: 720e3,
}
tech["Quenched Blades II"] = {"cost": cost1, "lvl": 0, "req": None}
tech["Improved Bows II"] = tech["Quenched Blades II"]
tech["Mounted Combat Techniques II"] = tech["Quenched Blades II"]
tech["Improved Projectiles II"] = tech["Quenched Blades II"]
tech["Swift Marching II"] = {
    "cost": cost1,
    "req": {
        3: {
            "Quenched Blades II": 5,
            "Improved Bows II": 5,
            "Mounted Combat Techniques II": 5,
            "Improved Projectiles II": 5,
        },
        7: {
            "Quenched Blades II": 10,
            "Improved Bows II": 10,
            "Mounted Combat Techniques II": 10,
            "Improved Projectiles II": 10,
        },
    },
}
tech["Treaties II"] = {"cost": cost1, "lvl": 0, "req": None}
tech["Cultural Exchange II"] = tech["Treaties II"]
tech["Marching Orders I"] = {"cost": cost1, "lvl": 0, "req": None}
tech["Barbarian Reports II"] = {
    "cost": {
        1: 15e3,
        2: 30e3,
        3: 45e3,
        4: 60e3,
        5: 75e3,
        6: 100e3,
        7: 125e3,
        8: 150e3,
        9: 200e3,
        10: 250e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Karaku Reports II"] = tech["Barbarian Reports II"]
tech["Skillful Operations II"] = {
    "cost": {
        1: 30e3,
        2: 60e3,
        3: 90e3,
        4: 120e3,
        5: 150e3,
        6: 200e3,
        7: 250e3,
        8: 300e3,
        9: 400e3,
        10: 500e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Plunder II"] = tech["Barbarian Reports II"]
tech["Karaku's Gift II"] = tech["Barbarian Reports II"]
tech["Call to Arms I"] = {"cost": cost1, "lvl": 0, "req": None}
tech["Quenched Blades III"] = {
    "cost": {
        1: 100e3,
        2: 150e3,
        3: 200e3,
        4: 250e3,
        5: 300e3,
        6: 500e3,
        7: 700e3,
        8: 1e6,
        9: 1.25e6,
        10: 1.5e6,
    },
    "lvl": 0,
    "req": None,
}
tech["Improved Bows III"] = tech["Quenched Blades III"]
tech["Mounted Combat Techniques III"] = tech["Quenched Blades III"]
tech["Improved Projectiles III"] = tech["Quenched Blades III"]
tech["Swift Marching III"] = tech["Quenched Blades III"]
tech["Special Medicines I"] = tech["Quenched Blades III"]
tech["Expanded Formations I"] = {
    "cost": {
        1: 3e6,
    },
    "lvl": 0,
    "req": None,
}
# print(tech)
tech["Marching Orders II"] = tech["Quenched Blades III"]
tech["Call to Arms II"] = {
    "cost": {
        1: 40e3,
        2: 80e3,
        3: 160e3,
        4: 500e3,
        5: 700e3,
        6: 1e6,
        7: 1.25e6,
        8: 2.0e6,
        9: 2.5e6,
        10: 3.5e6,
    },
    "lvl": 0,
    "req": None,
}
tech["Improved Morale"] = tech["Call to Arms II"]
tech["Special Medicines II"] = {
    "cost": {
        1: 50e3,
        2: 75e3,
        3: 100e3,
        4: 300e3,
        5: 400e3,
        6: 500e3,
        7: 600e3,
        8: 750e3,
        9: 900e3,
        10: 1e6,
    },
    "lvl": 0,
    "req": None,
}
tech["Expanded Formations II"] = {"cost": {1: 6e6}, "lvl": 0, "req": None}
tech["Surprise Strike"] = {
    "cost": {
        1: 40e3,
        2: 80e3,
        3: 120e3,
        4: 160e3,
        5: 200e3,
        6: 250e3,
        7: 300e3,
        8: 400e3,
        9: 500e3,
        10: 600e3,
    },
    "lvl": 0,
    "req": None,
}
