from item import Item

class GildedRose:
    @staticmethod
    def update_quality(items):
        updated_items = []
        for item in items:
            updated_items.append(update_item(item))
        return updated_items


def update_item(item):
    return Item(item.name, item.sell_in - 1, item.quality - 1)
