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
    amount = 1 if not is_expired(item) else 2
    return max(item.quality - amount, 0)


def is_expired(item):
    return item.sell_in <= 0
