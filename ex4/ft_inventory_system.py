def show_inv(inv: dict) -> None:
    """print an inventory gracefully"""
    total_value: int = 0
    count: int = 0
    types: dict = {}
    for (item, info) in inv.items():
        print(f"{item} ({info.get('type', 'Unknown')}, \
{info.get('rarity', 'Unknown')}): {info.get('quantity', 0)}x @ \
{info.get('value', 0)} gold each = \
{info.get('quantity', 0) * info.get('value', 0)} gold")
        total_value += info.get('quantity', 0) * info.get('value', 0)
        count += info.get('quantity', 0)
        tmp = info.get('type', 'Unknown')
        if (types.get(tmp)):
            types[tmp] += info.get('quantity', 0)
        else:
            types[tmp] = info.get('quantity', 0)
    print(f"\nInventory value: {total_value} golds")
    print(f"Item count: {count} items")
    print("Categories: ", end="")
    i = 0
    for (cat, qty) in types.items():
        if (i != 0):
            print(", ", end="")
        print(f"{cat}({qty})", end="")
        i += 1
    print()


def get_inv_value(inv: dict) -> int:
    """return the value of the inv inventory"""
    value: int = 0
    for info in inv.values():
        value += info.get("value", 0) * info.get("quantity", 0)
    return (value)


def get_item_count(inv: dict) -> int:
    """return the number of items in inv"""
    count: int = 0
    for info in inv.values():
        count += info.get("quantity", 0)
    return (count)


def get_rarest_items(inv_list: list):
    """Return all the items with the highest rarity"""
    RARITY_ORDER = {
        "unknown": -1,
        "common": 1,
        "uncommon": 2,
        "rare": 3,
        "epic": 4,
        "legendary": 5
    }
    rarity: int = -1
    items: list = []
    for inv in inv_list:
        for (name, item) in inv.items():
            item_rarity: int = RARITY_ORDER[item.get("rarity", "unknown")]
            if (item_rarity > rarity):
                rarity = item_rarity
                items = [name]
            elif (item_rarity == rarity):
                items.append(name)
    return (items)


if (__name__ == "__main__"):
    print("=== Player Inventory System ===\n")

    alice = {
        "sword": {
            "type": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50
        },
        "shield": {
            "type": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200
        },
    }

    print("=== Alice's Inventory ===")
    show_inv(alice)
    bob = {
        "magic_ring": {
            "type": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
    }
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    if (alice.get("potion") and alice["potion"]["quantity"] >= 2):
        alice["potion"]["quantity"] -= 2
        if (bob.get("potion")):
            bob["potion"]["quantity"] += 2
        else:
            bob["potion"] = {
                "type": "consumable",
                "rarity": "common",
                "quantity": 2,
                "value": 50
            }
        print("Transaction successful!")
    else:
        print("Transation failed!")

    print("\n=== Updated Inventories ===")
    print("Alice potions:", alice["potion"]["quantity"])
    print("Bob potions:", bob["potion"]["quantity"])

    print("\n=== Inventory Analytics ===")
    print("Most valuable player: ", end="")
    if (get_inv_value(alice) > get_inv_value(bob)):
        print(f"Alice ({get_inv_value(alice)} gold)")
    else:
        print(f"Bob ({get_inv_value(bob)} gold)")
    print("Most items: ", end="")
    if (get_item_count(alice) > get_item_count(bob)):
        print(f"Alice ({get_item_count(alice)} items)")
    else:
        print(f"Bob ({get_item_count(bob)} items)")
    print("Rarest items:", get_rarest_items([alice, bob]))
