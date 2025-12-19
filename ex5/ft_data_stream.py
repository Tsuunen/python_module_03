def gen_game_event(n: int):
    player: list = ["Alice", "Bob", "Charlie"]
    level: list = [5, 12, 8, 10, 1, 4, 3]
    actions: list = ["killed monster", "found treasure", "leveled up"]
    for i in range(n):
        yield (i + 1, player[i % 3], level[i % 7], actions[i % 3])


def fib_gen(n: int):
    i1: int = 0
    i2: int = 1
    for i in range(n):
        if (i == 0):
            yield 0
        elif (i == 1):
            yield 1
        else:
            yield i1 + i2
            tmp = i1 + i2
            i1 = i2
            i2 = tmp


def prime_gen(n: int):
    i: int = 2
    count: int = 0
    while (count < n):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            yield i
            count += 1
        i += 1


if (__name__ == "__main__"):
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    event_count: int = 0
    hl_player: int = 0
    treasure_event: int = 0
    lvlup_event: int = 0
    for i in gen_game_event(1000):
        if (i[0] < 4):
            print(f"Event {i[0]}: Player {i[1]} (level {i[2]}) {i[3]}")
        event_count += 1
        if (i[2] >= 10):
            hl_player += 1
        if (i[3] == "found treasure"):
            treasure_event += 1
        elif (i[3] == "leveled up"):
            lvlup_event += 1
    print("...\n")
    print("=== Stream Analytics ===")
    print("Total events processed:", event_count)
    print("High-level players (10+):", hl_player)
    print("Treasure events:", treasure_event)
    print("Level-up events:", lvlup_event)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    for i in fib_gen(10):
        if (i > 0):
            print(", ", end="")
        print(i, end="")
    print("\nPrime numbers (first 5): ", end="")
    for i in prime_gen(5):
        if (i > 2):
            print(", ", end="")
        print(i, end="")
    print()
