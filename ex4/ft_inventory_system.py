import sys


def parse_quantity(text):
    digits = "0123456789"
    value = 0
    for ch in text:
        idx = digits.find(ch)
        if idx == -1:
            return None
        value = value * 10 + idx
    return value


def add_item(inventory, name, qty):
    item = inventory.get(name)
    if item is None:
        item = dict()
        item.update({"name": name, "type": "item", "quantity": qty, "value": qty})
        inventory.update({name: item})
    else:
        current = item.get("quantity")
        new_qty = current + qty
        item.update({"quantity": new_qty, "value": new_qty})


def sort_items_by_qty(items):
    i = 0
    n = len(items)
    while i < n:
        j = i + 1
        best = i
        while j < n:
            a_name, a_qty = items[j]
            b_name, b_qty = items[best]
            if a_qty > b_qty or (a_qty == b_qty and a_name < b_name):
                best = j
            j += 1
        if best != i:
            items[i], items[best] = items[best], items[i]
        i += 1


def join_keys(keys_view):
    result = ""
    first = True
    for key in keys_view:
        if first:
            result = key
            first = False
        else:
            result = result + ", " + key
    return result


def join_values(inventory):
    result = ""
    first = True
    for _, item in inventory.items():
        qty = item.get("quantity")
        if first:
            result = str(qty)
            first = False
        else:
            result = result + ", " + str(qty)
    return result


def main(argv):
    inventory = dict()
    for arg in argv[1:]:
        if ":" not in arg:
            continue
        name, qty_text = arg.split(":", 1)
        if name == "":
            continue
        qty = parse_quantity(qty_text)
        if qty is None:
            continue
        add_item(inventory, name, qty)

    total_items = 0
    for item in inventory.values():
        total_items += item.get("quantity")

    print("=== Inventory System Analysis ===")
    print("Total items in inventory: " + str(total_items))
    print("Unique item types: " + str(len(inventory)))
    print()

    list_items = []
    for name, item in inventory.items():
        list_items.append((name, item.get("quantity")))

    sort_items_by_qty(list_items)

    print("=== Current Inventory ===")
    for name, qty in list_items:
        percent = 0.0
        if total_items != 0:
            percent = (qty * 100.0) / total_items
        percent_text = "{:.1f}".format(percent)
        print(name + ": " + str(qty) + " units (" + percent_text + "%)")

    most_name = ""
    most_qty = -1
    least_name = ""
    least_qty = -1
    for name, qty in list_items:
        if most_qty == -1 or qty > most_qty:
            most_qty = qty
            most_name = name
        if least_qty == -1 or qty < least_qty:
            least_qty = qty
            least_name = name

    print("\n=== Inventory Statistics ===")
    if most_qty != -1:
        print("Most abundant: " + most_name + " (" + str(most_qty) + " units)")
    if least_qty != -1:
        print("Least abundant: " + least_name + " (" + str(least_qty) + " units)")

    abundant = dict()
    moderate = dict()
    scarce = dict()
    for name, qty in list_items:
        if qty >= 10:
            abundant.update({name: qty})
        elif qty >= 5:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})

    print("\n=== Item Categories ===")
    if len(abundant) > 0:
        print("Abundant: " + str(abundant))
    if len(moderate) > 0:
        print("Moderate: " + str(moderate))
    if len(scarce) > 0:
        print("Scarce: " + str(scarce))

    restock = []
    for name, qty in list_items:
        if qty <= 1:
            restock.append(name)

    print("\n=== Management Suggestions ===")
    print("Restock needed: " + str(restock))

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: " + join_keys(inventory.keys()))
    print("Dictionary values: " + join_values(inventory))
    print("Sample lookup - 'sword' in inventory: " + str("sword" in inventory))


if __name__ == "__main__":
    main(sys.argv)
