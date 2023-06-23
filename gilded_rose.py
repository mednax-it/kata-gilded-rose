from collections import defaultdict
from enum import Enum

from item import Item

MIN_QUALITY = 0
MAX_QUALITY = 50

Types = Enum('Types', ['REGULAR', 'APPRECIATING', 'LEGENDARY', 'CONJURED'])

type_mappings = defaultdict(lambda: Types.REGULAR, [
    ("Aged Brie", Types.APPRECIATING),
    ("Sulfuras, Hand of Ragnaros", Types.LEGENDARY),
    ("Conjured Mana Cake", Types.CONJURED),
])


class GildedRose:
    @staticmethod
    def update_quality(items):
        return map(update_item, items)


def update_item(item):
    return Item(item.name, advance_sell_in(item), advance_quality(item))


def advance_sell_in(item):
    return item.sell_in - 1


def advance_quality(item):
    if type_of(item) == Types.REGULAR:
        amount = -1 if item.sell_in > 0 else -2
        return clamp(MIN_QUALITY, MAX_QUALITY, item.quality + amount)
    if type_of(item) == Types.APPRECIATING:
        amount = calculate_appreciation_amount(item)
        return clamp(MIN_QUALITY, MAX_QUALITY, item.quality + amount)
    if type_of(item) == Types.LEGENDARY:
        return item.quality
    if type_of(item) == Types.CONJURED:
        amount = -2 if item.sell_in > 0 else -4
        return clamp(MIN_QUALITY, MAX_QUALITY, item.quality + amount)


def type_of(item):
    return type_mappings[item.name]


def calculate_appreciation_amount(item):
    if item.sell_in <= 0:
        return -item.quality
    if item.sell_in <= 5:
        return 3
    if item.sell_in <= 10:
        return 2
    return 1


def clamp(floor, ceiling, amount):
    return min(max(amount, floor), ceiling)
