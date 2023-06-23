from item import Item


MIN_QUALITY = 0
MAX_QUALITY = 50

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
        return min(item.quality + amount, MAX_QUALITY)
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return item.quality
    elif item.name == "Conjured Mana Cake":
        amount = -2 if not is_expired(item) else -4
        return max(item.quality + amount, MIN_QUALITY)
    else:
        amount = -1 if not is_expired(item) else -2
        return max(item.quality + amount, MIN_QUALITY)


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
