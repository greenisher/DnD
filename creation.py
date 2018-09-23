import diceroll

class charclass():
    choice = input("Would you like to play as a cleric, a fighter or a mage?" )

    if choice == "cleric":
        hp = 20
        strength = 3
        dex = 4
        intelligence = 8
        wis = 12
        charisma = 8
        con = 10
    elif choice == "fighter":
        hp = 40
        strength = 12
        dex = 10
        intelligence = 7
        wis = 5
        charisma = 2
        con = 6
    else:
        hp = 30
        strength = 2
        dex = 8
        intelligence = 14
        wis = 10
        charisma = 8
        con = 3
        
hp = charclass.hp + 6
strength = charclass.strength + 4
dex = charclass.dex + 4
intelligence = charclass.intelligence + 4
wis = charclass.wis + 4
charisma = charclass.charisma + 4
con = charclass.con + 4
