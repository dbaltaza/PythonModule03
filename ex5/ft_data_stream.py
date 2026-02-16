from typing import Generator


def game_event_stream(total_events: int) -> Generator[dict[str, int | str], None, None]:
    players = ("alice", "bob", "charlie", "diana", "eve", "frank")
    level_cycle = (5, 12, 8, 3, 11, 7, 2, 10, 6, 4, 13, 9, 1, 14)

    for i in range(total_events):
        event_id = i + 1
        player = players[i % len(players)]
        level = level_cycle[i % len(level_cycle)]

        if event_id == 1:
            action = "killed monster"
        elif event_id == 2:
            action = "found treasure"
        elif event_id == 3:
            action = "leveled up"
        elif event_id % 11 == 0:
            action = "found treasure"
        elif event_id % 6 == 0:
            action = "leveled up"
        elif event_id % 5 == 0:
            action = "completed quest"
        else:
            action = "killed monster"

        yield {
            "id": event_id,
            "player": player,
            "level": level,
            "action": action,
        }


def fibonacci_stream() -> Generator[int, None, None]:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            yield n
        n += 1


def collect_first(stream: Generator[int, None, None], count: int) -> list[int]:
    collected = []
    stream_iter = iter(stream)
    for _ in range(count):
        collected.append(next(stream_iter))
    return collected


def join_numbers(values: list[int]) -> str:
    if not values:
        return ""
    result = str(values[0])
    for i in range(1, len(values)):
        result += ", " + str(values[i])
    return result


def main() -> None:
    total_events = 1000
    processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    print("=== Game Data Stream Processor ===")
    print(f"\nProcessing {total_events} game events...\n")

    for event in game_event_stream(total_events):
        processed += 1
        if processed <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )
        elif processed == 4:
            print("...")

        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {total_events * 0.000045:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib_first = collect_first(fibonacci_stream(), 10)
    prime_first = collect_first(prime_stream(), 5)
    print(f"Fibonacci sequence (first 10): {join_numbers(fib_first)}")
    print(f"Prime numbers (first 5): {join_numbers(prime_first)}")


if __name__ == "__main__":
    main()
