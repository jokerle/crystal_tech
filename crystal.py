from tech import tech

"""python crystal tech"""

# Crystal Cost Reduction in %
CCR = 0.1

crystal_mine_cost = 0

tech_names = [k for k in tech]


def calc_crystal_reserch_center() -> float:
    data = {
        2: (1, 0.2),
        3: (2.5, 0.3),
        4: (4, 0.4),
        5: (5.5, 0.5),
        6: (7, 0.6),
        7: (10, 0.7),
        8: (15, 0.8),
        9: (20, 0.9),
        10: (25, 1.0),
        11: (30, 1.2),
        12: (37.5, 1.4),
        13: (45, 1.6),
        14: (52.5, 1.8),
        15: (60, 2.0),
        16: (70, 2.2),
        17: (80, 2.4),
        18: (90, 2.6),
        19: (100, 2.8),
        20: (115, 3.0),
        21: (130, 3.3),
        22: (150, 3.6),
        23: (200, 4.0),
        24: (250, 4.5),
        25: (300, 5.0),
    }
    sum = 0
    # sum2 = 0
    ccr = 0.1 / 100
    for k, v in data.items():
        sum = sum + v[0] - (v[0] * ccr)
        # sum2 = sum2 +v[0]
        ccr = v[1] / 100.0
    sum /= 1e3
    # print(f" Crystal Research Center upgrade costs (simple): {sum2:.2f}m")
    print(f" Crystal Research Center successive upgrade costs: {sum:.2f}m")
    return sum


def get_total_cost() -> None:
    s = 0.0
    for n in tech_names:
        print(n, tech[n])
        for tier in tech[n]["cost"]:
            s += float(tech[n]["cost"][tier])
    s = s / 1e6
    # print(f" Total crystal costs (simple sum): {s:.2f}m")
    s = s - (s * CCR)
    print(f" Total crystal tech costs with reductions: {s:.2f}m")
    return


def check_req(name: str, lvl: int) -> bool:
    req = tech[name]["req"]
    req_okay = True
    missing = {}
    if req is not None:
        for key in req:
            if lvl >= key:
                required_tech = [name for name in req[key]]
                for t in required_tech:
                    if tech[t]["lvl"] < req[key][t]:
                        req_okay = False
                        missing[t]=(tech[t]["lvl"],req[key][t])
                        print(
                            f'!!  {t} has lvl={tech[t]["lvl"]} but requires lvl={req[key][t]} !!'
                        )
    else:
        req_okay = True
    return req_okay,missing


def level_up(name: str, lvl: int) -> float:
    """level up tech <name> to level <lvl>"""
    current_lvl=tech[name]["lvl"]
    cost=0
    total=0
    sub_cost=0
    for i in range(current_lvl,lvl):
        cost=tech[name]["cost"][i+1]
        print(f"Upgrade cost: '{name}': {i} -> {i+1} = {cost:.0f}")
        allowed, missing = check_req(name,i+1)
        if allowed is False:
            sub_cost = 0
            for sub_name in missing:
                # for level in range(missing[name][0]+1,missing[name][1]):
                    level = missing[sub_name][1]
                    sub_cost= level_up(sub_name,level)

        tech[name]["lvl"]+=1
        total+=cost
        current_lvl=tech[name]["lvl"]
        
    total+=sub_cost
    print(f"  upgrading {name} to level {lvl} costing {total:.0f} (including requirements)")
    return total


# get_total_cost()
# calc_crystal_reserch_center()
# print(check_req("Swift Marching II", 5))
# level_up("Swift Marching II", 5)
# cost = level_up("Skillful Operations I", 5)
# cost = level_up("Larger Camps", 5)
# cost = level_up("Quenched Blades I", 5)
cost = level_up("Marching Orders I",10)
print(cost)