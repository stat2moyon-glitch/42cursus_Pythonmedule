import random

len(), print(), random.*, 
set(), set.union(), set.intersection(), set.difference()

def gen_player_achievements()
    achievements = [
        "Hello World",
        "Norminette Survivor",
        "Segmentation Fault",
        "Memory Leak Master",
        "Moulinette Victim",
        "Peer Evaluation",
        "Black Hole Survivor",
        "Piscine Survivor",
        "First 125",
        "Milestone Unlocked",
        "Git Push Master",
        "Infinite Loop",
        "Valgrind Warrior",
        "All Nighter",
        "Coffee Addict",
        "Campus Resident",
        "Last Minute Submit",
        "Legendary Debugger",
        "Norm Error Collector",
        "Vogsphere Conqueror",
        "No Segfault Today",
        "One More Norm Error",
        "The Last One Standing"
    ]
    
    count = random.randint(0, 8)
    
    selected = random.sample(achivements,count)

    return set(selected)

def main()
    print("=== Achievement Tracker System ===")

    pisciner = gen_player_achievements()
    print(f"Player Pisciner: {pisciner}")

    cadet = gen_player_achievements()
    print(f"Player Cadet: {cadet}")

    lifesaver = gen_player_achievements()
    print(f"Player LifeSaver: {lifesaver}")

    bocal = gen_player_achievements()
    print(f"Player Bocal: {bocal}")

    all_distinct = pisciner.union(cadet, lifesaver, bocal)
    print(f"All distinct achievements: {all_distinct}")

    
        
        



    


    
    
