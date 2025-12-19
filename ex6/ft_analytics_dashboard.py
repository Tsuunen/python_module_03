def score_key(item):
    return item[1].get("score", 0)


if (__name__ == "__main__"):
    players = {
        "alice": {
            "score": 2300,
            "achievements": {"first_kill", 'treasure_hunter', 'speed_demon',
                             'perfectionist', 'explorator'},
            "region": "north",
            "active": True
        },
        "bob": {
            "score": 1800,
            "achievements": {"level_10", 'boss', 'explorator'},
            "region": "east",
            "active": True
        },
        "charlie": {
            "score": 2150,
            "achievements": {"boss_slayer", 'treasure_hunter', 'speed_demon',
                             'collector', 'perfectionist', 'explorator',
                             'boss'},
            "region": "central",
            "active": True
        },
        "diana": {
            "score": 2050,
            "achievements": {'explorator', 'boss', 'collector'},
            "region": "north",
            "active": False
        }
    }

    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000):",
          [name for (name, stat) in players.items() if stat["score"] > 2000])
    print("Scores doubled:", [stat["score"] * 2 for stat in players.values()])
    print("Active players:",
          [name for (name, stat) in players.items() if stat["active"] is True])
    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", {
        name: stat["score"] for (name, stat) in players.items()
    })
    print("Score categories:", {
        "high": sum(1 for p in players.values() if p["score"] > 2100),
        "medium": sum(1 for p in players.values()
                      if 2000 < p["score"] <= 2100),
        "low": sum(1 for p in players.values() if p["score"] <= 2000),
    })
    print("Achievement counts:", {
        name: len(stat["achievements"]) for (name, stat) in players.items()
        if stat["active"]
    })

    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", {name for name in players.keys()})

    shared = set()
    ach_sets = [p["achievements"] for p in players.values()]

    for i in range(len(ach_sets)):
        for j in range(i + 1, len(ach_sets)):
            shared |= ach_sets[i] & ach_sets[j]

    all_ach = set().union(*ach_sets)

    print("Unique achievements:", all_ach - shared)

    print("Active regions:", {stat["region"] for stat in players.values()})

    print("\n=== Combined Analysis ===")
    print("Total players:", len(players))
    print("Total unique achievements:", len({ach for player in players.values()
                                             for ach in
                                             player.get("achievements",
                                                        set())}))
    print("Average score:", sum([stats["score"] for stats in players.values()
                                 ]) / len(players))

    top_name, top_stats = sorted(
        players.items(),
        key=score_key,
        reverse=True
    )[0]
    print(
        f"Top performer: {top_name} ({top_stats['score']} points, \
{len(top_stats['achievements'])} achievements)")
