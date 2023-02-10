tech = {
    "Quenched Blades I": {
        "cost": {
            1: 28.5e3,
            2: 67.5e3,
            3: 108e3,
            4: 148e3,
            5: 198e3,
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
        1: 47.5e3,
        2: 93e3,
        3: 139.5e3,
        4: 168e3,
        5: 252e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Treaties I"] = {
    "cost": {
        1: 18e3,
        2: 33.6e3,
        3: 50.4e3,
        4: 67.2e3,
        5: 134.4e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Cultural Exchanage I"] = tech["Treaties I"]
tech["Larger Camps"] = {
    "cost": {
        1: 47.5e3,
        2: 93e3,
        3: 139.5e3,
        4: 168e3,
        5: 252e3,
    },
    "lvl": 0,
    "req": {3: {"Swift Marching I": 3}},
}
tech["Barbarian Reports I"] = {
    "cost": {
        1: 9e3,
        2: 16.8e3,
        3: 25.2e3,
        4: 33.6e3,
        5: 67.2e3,
    },
    "lvl": 0,
    "req": None,
}
tech["Karaku Reports I"] = tech["Barbarian Reports I"]
tech["Skillful Operations I"] = {
    "cost": {
        1: 19e3,
        2: 37.6e3,
        3: 55.8e3,
        4: 73.6e3,
        5: 145.6e3,
    },
    "CCR": {
        1: 0.01,
        2: 0.02,
        3: 0.03,
        4: 0.04,
        5: 0.05,
    },
    "lvl":0,
    "req":{
        3:{"Larger Camps":3}
    }
}
tech["Plunder I"] = tech["Treaties I"]
tech["Plunder I"].update({
    "req":{
        3:{"Barbarian Reports I":3},
        5:{"Cultural Exchange II":7}
    }
})
tech["Karaku's Gift I"] = tech["Treaties I"]
tech["Karaku's Gift I"].update({
    "req":{
        3:{"Karak Reports I":5}
    }
})
tech["Attack Formation"] = {
    "cost": {
        1:90e3,
        2:168e3,
        3:252e3,
        4:378e3,
        5:504e3,
        6:672e3,
        7:1e6,
        8:1.3e6,
        9:1.6e6,
        10:2e6,
    },
    "lvl": 0,
    "req": {
        3:{"Swift Marching I":5},
        7:{"Larger Camps":5}
    },
}
cost1 = {
    1:72000,
    2:100800,
    3:168000,
    4:201600,
    5:268800,
    6:336000,
    7:403200,
    8:470400,
    9:537600,
    10:604800
}
tech["Quenched Blades II"] = {"cost": cost1, "lvl": 0, "req":{
    3:{"Attack Formation":3},
    10:{"Attack Formation":7}
}}
tech["Improved Bows II"] = tech["Quenched Blades II"]
tech["Mounted Combat Techniques II"] = tech["Quenched Blades II"]
tech["Improved Projectiles II"] = tech["Quenched Blades II"]
tech["Swift Marching II"] = {
    "cost": {
        1:72e3,
        2:108e3,
        3:180e3,
        4:201.6e3,
        5:268.8e3,
        6:336e3,
        7:403.2e3,
        8:448e3,
        9:512e3,
        10:576e3
        },
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
    "lvl":0
}
# Requirements filled until here!!
tech["Treaties II"] = {
    "cost": {
        1:25.2e3,
        2:50.4e3,
        3:75.6e3,
        4:100.8e3,
        5:126e3,
        6:168e3,
        7:210e3,
        8:252e3,
        9:336e3,
        10:400e3
        },
    "lvl": 0,
    "req": None}
tech["Cultural Exchange II"] = tech["Treaties II"]
# double check marching order requirements!!
tech["Marching Orders I"] =tech["Swift Marching II"]
tech["Marching Orders I"].update({"req":None})
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
