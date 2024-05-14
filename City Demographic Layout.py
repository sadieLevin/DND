from random import randint

max_pop = randint(22500, 32500)
total_demographics = {"low leveled": 0, "lvl 5": 0, "lvl 5+ caster": 0, "total": 0}

for i in range(1, 101):

    leveled_npcs = {"low leveled ranger": 0, "low leveled paladin": 0, "low leveled fighter": 0, 
                    "low leveled barbarian": 0, "low leveled rogue": 0, "low leveled monk": 0, "low leveled cleric": 0, 

                    "lvl 5 Martial": 0,"lvl 5 Cleric": 0,"lvl 5 Thief": 0,"low leveled caster": 0,

                    "lvl 5+ caster": 0}
    
    for j in range(int(max_pop/i)):
        charseed = randint(0, max_pop)
        if charseed%(max_pop-1) == 0:
            leveled_npcs["lvl 5+ caster"] += 1
            total_demographics["lvl 5+ caster"] += 1

        elif charseed%1000 == 0:
            if randint(0, 16)%4 == 0:
                leveled_npcs["lvl 5 Martial"] += 1
            if randint(0, 16)%4 == 1:
                leveled_npcs["lvl 5 Cleric"] += 1
            if randint(0, 16)%4 == 2:
                leveled_npcs["lvl 5 Thief"] += 1
            if randint(0, 16)%4 == 3:
                leveled_npcs["low leveled caster"] += 1
            total_demographics["lvl 5"] += 1

        elif charseed%10 == 0:
            if randint(0, 49)%7 == 0:
                leveled_npcs["low leveled ranger"] += 1
            if randint(0, 49)%7 == 1:
                leveled_npcs["low leveled paladin"] += 1
            if randint(0, 49)%7 == 2:
                leveled_npcs["low leveled fighter"] += 1
            if randint(0, 49)%7 == 3:
                leveled_npcs["low leveled barbarian"] += 1
            if randint(0, 49)%7 == 4:
                leveled_npcs["low leveled rogue"] += 1
            if randint(0, 49)%7 == 5:
                leveled_npcs["low leveled monk"] += 1
            if randint(0, 49)%7 == 6:
                leveled_npcs["low leveled cleric"] += 1
            
            total_demographics["low leveled"] += 1
        total_demographics["total"] += 1
    print("City " + str(i) + ": " + str(int(max_pop/i)) + " " + str(leveled_npcs) + "\n")
print("Total Pop:")
print(total_demographics)
