if (__name__ == "__main__"):
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print("=== Achievement Tracker System ===\n")
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")
    unique_achivement = alice | bob | charlie
    print("All unique achievements:", unique_achivement)
    print("Total unique achievements:", len(unique_achivement))
    print("\nCommon to all players:", alice & bob & charlie)
    print("Rare achievements (1 player):", (alice - bob - charlie)
          | (bob - alice - charlie) | (charlie - alice - bob))
    print("\nAlice vs Bob common:", alice & bob)
    print("Alice unique:", alice - bob)
    print("Bob unique:", bob - alice)
