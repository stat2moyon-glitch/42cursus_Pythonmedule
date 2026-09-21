import sys

def perse_scores(argv: list[str]) -> list[int]:
    scores: list[int] = []
    for argument in argv:
        try:
            score = int(argument)
        except ValueError:
            print(f"Invailed parameter: '{argument}'")
        else:
            scores.append(score)
    return scores

def main() -> None
    print("=== Player Score Analytics ===")
    scores = parse_scores(sys.argv[1:])
    count = len(scores)
    if count == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    total = sum(scores)
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {sys.argv[1:]}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {total / count}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
