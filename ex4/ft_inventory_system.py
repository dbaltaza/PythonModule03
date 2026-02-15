import sys


def parse_inventory(args):
    inventory = {}
    for arg in args:
        if ':' in arg:
            item, qty = arg.split(':', 1)
            inventory[item] = int(qty)
    return inventory


def categorize_items(inventory):
    # Only two categories to match sample output
    categories = {
        'moderate': {},  # 4 or more
        'scarce': {}     # 1-3
    }
    for item, qty in inventory.items():
        if qty >= 4:
            categories['moderate'][item] = qty
        else:
            categories['scarce'][item] = qty
    return categories


def inventory_report(inventory):
    print("=== Inventory System Analysis ===")
    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    # Sort by quantity descending, then by name ascending
    sorted_items = sorted(inventory.items(), key=lambda x: (-x[1], x[0]))
    for item, qty in sorted_items:
        percent = (qty / total_items) * 100 if total_items else 0
        print(f"{item}: {qty} unit{'s' if qty != 1 else ''} ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    if inventory:
        max_qty = max(inventory.values())
        min_qty = min(inventory.values())
        most_abundant = [
            item for item, qty in inventory.items() if qty == max_qty
        ]
        least_abundant = [
            item for item, qty in inventory.items() if qty == min_qty
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
    moderate_items = [f"'{k}': {v}" for k, v in categories['moderate'].items()]
    scarce_items = [f"'{k}': {v}" for k, v in categories['scarce'].items()]
    moderate_str = '{' + ','.join(moderate_items) + '}'
    scarce_str = '{' + ','.join(scarce_items) + '}'
    print(f"Moderate: {moderate_str}")
    print(f"Scarce: {scarce_str}")

    print("\n=== Management Suggestions ===")
    if inventory:
        min_qty = min(inventory.values())
        restock = [item for item, qty in inventory.items() if qty == min_qty]
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
    keys_str = '[\'' + '\',\n\''.join(keys) + '\']'
    values_str = '[' + ', '.join(str(v) for v in values) + ']'
    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main():
    inventory = parse_inventory(sys.argv[1:])
    inventory_report(inventory)


if __name__ == "__main__":
    main()
