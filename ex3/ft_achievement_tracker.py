def main():
    # Player achievements (using sets for uniqueness)
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'
    }

    print('=== Achievement Tracker System ===\n')
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print('\n=== Achievement Analytics ===')
    # All unique achievements
    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    # Achievements common to all players
    common_all = alice & bob & charlie
    print(f"Common to all players: {common_all}")

    # Rare achievements (only one player has them)
    rare = set()
    for achievement in all_achievements:
        count = sum([
            achievement in alice,
            achievement in bob,
            achievement in charlie
        ])
        if count == 1:
            rare.add(achievement)
    print(f"Rare achievements (1 player): {rare}\n")

    # Alice vs Bob common and unique
    alice_bob_common = alice & bob
    alice_unique = alice - bob
    bob_unique = bob - alice
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
