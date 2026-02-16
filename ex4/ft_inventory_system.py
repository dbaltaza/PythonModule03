import sys


def build_catalog() -> dict[str, dict[str, int | str]]:
    return {
        "sword": {"type": "weapon", "value": 50},
        "potion": {"type": "consumable", "value": 10},
        "shield": {"type": "armor", "value": 40},
        "armor": {"type": "armor", "value": 75},
        "helmet": {"type": "armor", "value": 25},
    }


def parse_inventory(args: list[str]) -> dict[str, dict[str, int | str]]:
    inventory: dict[str, dict[str, int | str]] = {}
    catalog = build_catalog()
    for arg in args:
        if ":" not in arg:
            continue
        item, qty = arg.split(":", 1)
        try:
            quantity = int(qty)
        except ValueError:
            print(f"Invalid quantity for item '{item}': {qty}")
            continue
        template = catalog.get(item, {"type": "misc", "value": 1})
        item_data: dict[str, int | str] = {
            "name": item,
            "type": template.get("type", "misc"),
            "value": int(template.get("value", 1)),
            "quantity": 0,
        }
        item_data.update({"quantity": quantity})
        inventory[item] = item_data
    return inventory


def categorize_items(
    inventory: dict[str, dict[str, int | str]],
) -> dict[str, dict[str, dict[str, int | str]]]:
    # Only two categories to match sample output
    categories: dict[str, dict[str, dict[str, int | str]]] = {
        "moderate": {},  # 4 or more
        "scarce": {},    # 1-3
    }
    for item, data in inventory.items():
        qty = int(data.get("quantity", 0))
        if qty >= 4:
            categories["moderate"][item] = data
        else:
            categories["scarce"][item] = data
    return categories


def inventory_report(inventory: dict[str, dict[str, int | str]]) -> None:
    print("=== Inventory System Analysis ===")
    total_items = sum(
        int(data.get("quantity", 0)) for data in inventory.values()
    )
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    # Sort by quantity descending, then by name ascending
    sorted_items = sorted(
        inventory.items(),
        key=lambda x: (-int(x[1].get("quantity", 0)), x[0]),
    )
    for item, data in sorted_items:
        qty = int(data.get("quantity", 0))
        percent = (qty / total_items) * 100 if total_items else 0
        print(f"{item}: {qty} unit{'s' if qty != 1 else ''} ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    if inventory:
        quantities = [
            int(data.get("quantity", 0)) for data in inventory.values()
        ]
        max_qty = max(quantities)
        min_qty = min(quantities)
        most_abundant = [
            item for item, data in inventory.items()
            if int(data.get("quantity", 0)) == max_qty
        ]
        least_abundant = [
            item for item, data in inventory.items()
            if int(data.get("quantity", 0)) == min_qty
        ]
        print(f"Most abundant: {most_abundant[0]} ({max_qty} units)")
        unit_suffix = 's' if min_qty != 1 else ''
        print(
            f"Least abundant: {least_abundant[0]} "
            f"({min_qty} unit{unit_suffix})"
        )
    else:
        print("Most abundant: N/A")
        print("Least abundant: N/A")

    print("\n=== Item Categories ===")
    categories = categorize_items(inventory)
    # Print moderate and scarce in order, with formatting to match sample
    moderate_items = [
        f"'{k}': {int(v.get('quantity', 0))}"
        for k, v in categories["moderate"].items()
    ]
    scarce_items = [
        f"'{k}': {int(v.get('quantity', 0))}"
        for k, v in categories["scarce"].items()
    ]
    moderate_str = "{" + ",".join(moderate_items) + "}"
    scarce_str = "{" + ",".join(scarce_items) + "}"
    print(f"Moderate: {moderate_str}")
    print(f"Scarce: {scarce_str}")

    print("\n=== Management Suggestions ===")
    if inventory:
        quantities = [
            int(data.get("quantity", 0)) for data in inventory.values()
        ]
        min_qty = min(quantities)
        restock = [
            item for item, data in inventory.items()
            if int(data.get("quantity", 0)) == min_qty
        ]
        # Print restock list with each item on a new line and comma,
        # matching sample.
        if len(restock) == 1:
            print(f"Restock needed: ['{restock[0]}']")
        else:
            restock_str = '[\'' + '\',\n\''.join(restock) + '\']'
            print(f"Restock needed: {restock_str}")
    else:
        print("Restock needed: []")

    print("\n=== Dictionary Properties Demo ===")
    # Print keys and values each on a new line, matching sample
    keys = list(inventory.keys())
    values = list(inventory.values())
    quantities = [str(int(v.get("quantity", 0))) for v in values]
    print(f"Dictionary keys: {', '.join(keys)}")
    print(f"Dictionary values (quantities): {', '.join(quantities)}")
    print(
        "Sample lookup - 'sword' in inventory: "
        f"{inventory.get('sword') is not None}"
    )


def main() -> None:
    try:
        inventory = parse_inventory(sys.argv[1:])
        inventory_report(inventory)
    except Exception as exc:
        print(f"Error running inventory system: {exc}")


if __name__ == "__main__":
    main()
