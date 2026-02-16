def build_scores() -> dict[str, int]:
    return {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 3000,
        "john": 750,
        "gregory": 1200,
    }


def build_player_regions() -> dict[str, str]:
    return {
        "alice": "north",
        "bob": "east",
        "diana": "south",
        "charlie": "central",
        "john": "north",
        "gregory": "south",
    }


def main() -> None:
    try:
        scores = build_scores()
        highscorers = [name for name, score in scores.items() if score >= 2000]
        doubled = [score * 2 for score in scores.values()]
        activeplayers = list(scores.keys())[:3]
        achievements_count = {
            name: (5 if s >= 2000 else 3 if 1000 < s < 2000 else 1)
            for name, s in scores.items()
        }
        categories = {
            "high": len([s for s in scores.values() if s >= 2000]),
            "medium": len([s for s in scores.values() if 1000 < s < 2000]),
            "low": len([s for s in scores.values() if s <= 1000]),
        }
        unik = {name for name in scores.keys()}
        players_regions = build_player_regions()
        regions = {players_regions[p] for p in activeplayers}
        alice_achievements = {
            "high_scorer",
            "mid_scorer",
            "low_scorer",
            "first_kill",
            "boss_slayer",
        }
        bob_achievements = {
            "mid_scorer",
            "low_scorer",
            "first_kill",
        }
        john_achievements = {
            "low_scorer",
        }
        all_sets = [alice_achievements, bob_achievements, john_achievements]
        uachiv = {item for s in all_sets for item in s}
        max_scores = max(scores, key=scores.get)

        print("=== Game Analytics Dashboard ===\n")
        print("=== List Comprehension Examples ===")
        print(f"High scorers (>2000): {highscorers}")
        print(f"Scores doubled: {doubled}")
        print(f"Active players: {activeplayers}")

        print("\n=== Dict Comprehension Examples ===")
        print(f"Players scores: {scores}")
        print(f"Score categories: {categories}")
        print(f"achievements counts: {achievements_count}")

        print("\n=== Set Comprehension Examples ===")
        print(f"Unique players: {unik}")
        print(f"Unique achievements: {uachiv}")
        print(f"Active regions: {regions}")

        print("\n=== Combined Analysis ===")
        print(f"Total players: {len(scores)}")
        print(f"Total unique achievements: {len(uachiv)}")
        print(f"Average score: {sum(scores.values()) / len(scores):.2f}")
        print(
            f"Top performer: {max_scores} ({scores[max_scores]} points, "
            f"{achievements_count[max_scores]} achievements)"
        )
    except Exception as exc:
        print(f"Error running analytics dashboard: {exc}")


if __name__ == "__main__":
    main()
