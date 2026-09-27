import random

ACHIVEMENTS = [
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

def gen_player_achievements() -> set[str]:
    count = random.randint(0, 8)
    selected = random.sample(ACHIEVEMENTS,count)
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

    common_distinct = pisciner.intersection(cadet, lifesaver, bocal)
    print(f"Common achievements: {common_distinct}")

    only_pisciner = pisciner.difference(cadet, lifesaver, bocal)
    print(f"Only Pisciner has: {only_pisciner}")
    only_cadet = cadet.difference(pisciner, lifesaver, bocal)
    print(f"Only Cadet has: {only_cadet}")
    only_lifesaver = lifesaver.difference(pisciner, cadet, bocal)
    print(f"Only LifeSaver has: {only_lifesaver}")
    only_bocal = bocal.difference(pisciner, cadet, lifesaver)
    print(f"Only Bocal has: {only_bocal}")

    miss_pisciner = ACHIVEMENTS.difference(pisciner)
    print(f"Pisciner is missing: {miss_piscine}")
    miss_cadet = ACHIVEMENTS.difference(cadet)
    print(f"Cadet is missing: {miss_cadet}")
    miss_lifesaver = ACHIVEMENTS.difference(lifesaver)
    print(f"LifeSaver is missing: {miss_lifesaver}")
    miss_bocal = ACHIVEMENTS.difference(bocal)
    print(f"Bocal is missing: {miss_bocal}")


    
    
