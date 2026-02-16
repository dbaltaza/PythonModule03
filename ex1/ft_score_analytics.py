import sys


def ft_score_analytics(argv):
    print("=== Player Score Analytics ===")
    scores = argv[1:]
    if not scores:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    numeric_scores = []
    for score in scores:
        try:
            numeric_scores.append(int(score))
        except ValueError:
            print(f"Invalid score: {score}")
            return

    total_players = len(numeric_scores)
    total_score = sum(numeric_scores)
    high_score = max(numeric_scores)
    low_score = min(numeric_scores)
    score_range = high_score - low_score
    average_score = total_score / total_players

    print(f"Scores processed: {numeric_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    ft_score_analytics(sys.argv)
