import sys


DIGIT_MAP: dict[str, int] = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def parse_quantity(text: str) -> int | None:
    if text == "":
        return None
    value = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch not in DIGIT_MAP:
            return None
        value = (value * 10) + DIGIT_MAP[ch]
        i += 1
    return value


def split_item_quantity(arg: str) -> tuple[str, str] | None:
    i = 0
    while i < len(arg):
        if arg[i] == ":":
            return arg[:i], arg[i + 1:]
        i += 1
    return None


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
        parts = split_item_quantity(arg)
        if parts is None:
            continue
        item, qty_text = parts
        qty = parse_quantity(qty_text)
        if qty is None:
            print(f"Invalid quantity for item '{item}': {qty_text}")
            continue
        template = catalog.get(item, {"type": "misc", "value": 1})
        item_data: dict[str, int | str] = {
            "name": item,
            "type": template.get("type", "misc"),
            "value": template.get("value", 1),
            "quantity": 0,
        }
        item_data.update({"quantity": qty})
        inventory[item] = item_data
    return inventory


def inventory_report(inventory: dict[str, dict[str, int | str]]) -> None:
    print("=== Inventory System Analysis ===")
    total_items = 0
    for data in inventory.values():
        total_items += data.get("quantity", 0)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    items_list: list[tuple[str, int]] = []
    for item, data in inventory.items():
        items_list.append((item, data.get("quantity", 0)))
    i = 0
    while i < len(items_list):
        max_idx = i
        j = i + 1
        while j < len(items_list):
            if items_list[j][1] > items_list[max_idx][1]:
                max_idx = j
            j += 1
        if max_idx != i:
            items_list[i], items_list[max_idx] = items_list[max_idx], items_list[i]
        i += 1
    for item, qty in items_list:
        percent = (qty / total_items) * 100 if total_items else 0
        print(f"{item}: {qty} unit{'s' if qty != 1 else ''} ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    if inventory:
        max_qty = None
        min_qty = None
        most_item = ""
        least_item = ""
        for item, data in inventory.items():
            qty = data.get("quantity", 0)
            if max_qty is None or qty > max_qty:
                max_qty = qty
                most_item = item
            if min_qty is None or qty < min_qty:
                min_qty = qty
                least_item = item
        if max_qty is not None and min_qty is not None:
            print(f"Most abundant: {most_item} ({max_qty} units)")
            unit_suffix = "s" if min_qty != 1 else ""
            print(
                f"Least abundant: {least_item} ({min_qty} unit{unit_suffix})"
            )
        else:
            print("Most abundant: N/A")
            print("Least abundant: N/A")
    else:
        print("Most abundant: N/A")
        print("Least abundant: N/A")

    print("\n=== Item Categories ===")
    moderate: dict[str, dict[str, int | str]] = {}
    scarce: dict[str, dict[str, int | str]] = {}
    for item, data in inventory.items():
        qty = data.get("quantity", 0)
        if qty >= 4:
            moderate[item] = data
        else:
            scarce[item] = data
    moderate_str = "{"
    first = True
    for key, value in moderate.items():
        if not first:
            moderate_str += ","
        moderate_str += f"'{key}': {value.get('quantity', 0)}"
        first = False
    moderate_str += "}"
    scarce_str = "{"
    first = True
    for key, value in scarce.items():
        if not first:
            scarce_str += ","
        scarce_str += f"'{key}': {value.get('quantity', 0)}"
        first = False
    scarce_str += "}"
    print(f"Moderate: {moderate_str}")
    print(f"Scarce: {scarce_str}")

    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    if inventory:
        min_qty = None
        for data in inventory.values():
            qty = data.get("quantity", 0)
            if min_qty is None or qty < min_qty:
                min_qty = qty
        if min_qty is not None:
            for item, data in inventory.items():
                if data.get("quantity", 0) == min_qty:
                    restock.append(item)
    if len(restock) == 0:
        print("Restock needed: []")
    elif len(restock) == 1:
        print(f"Restock needed: ['{restock[0]}']")
    else:
        restock_str = "["
        i = 0
        while i < len(restock):
            restock_str += "'" + restock[i] + "'"
            if i < len(restock) - 1:
                restock_str += ", "
            i += 1
        restock_str += "]"
        print(f"Restock needed: {restock_str}")

    print("\n=== Dictionary Properties Demo ===")
    keys_line = ""
    first = True
    for key in inventory.keys():
        if not first:
            keys_line += ", "
        keys_line += key
        first = False
    values_line = ""
    first = True
    for data in inventory.values():
        if not first:
            values_line += ", "
        values_line += str(data.get("quantity", 0))
        first = False
    print(f"Dictionary keys: {keys_line}")
    print(f"Dictionary values: {values_line}")
    print(
        "Sample lookup -'sword' in inventory: "
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
