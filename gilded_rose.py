from item import Item

class GildedRose:
    @staticmethod
    def update_quality(items):
        updated_items = []
        for item in items:
            updated_items.append(update_item(item))
        return updated_items


def update_item(item):
    return Item(item.name, item.sell_in - 1, calculate_new_quality(item))


def calculate_new_quality(item):
    if item.name == "Aged Brie":
        amount = calculate_appreciating_amount(item)
    else:
        amount = -1 if not is_expired(item) else -2
    return max(item.quality + amount, 0)


def calculate_appreciating_amount(item):
    if item.sell_in > 10:
        return 1
    if item.sell_in > 5:
        return 2
    if item.sell_in > 0:
        return 3
    # Drop item quality to 0 if expired.
    return -item.quality


def is_expired(item):
    return item.sell_in <= 0
