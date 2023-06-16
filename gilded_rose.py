class GildedRose:

    @staticmethod
    def update_sell_in(item):
        if "Sulfuras, Hand of Ragnaros" != item.name:
            item.sell_in = item.sell_in - 1

    @staticmethod
    def update_item(items):
        for item in items:
            GildedRose.update_quality(item)
            GildedRose.update_sell_in(item)

        return items

    @staticmethod
    def update_quality(item):
        if "Sulfuras, Hand of Ragnaros" != item.name:
            if "Aged Brie" == item.name:
                GildedRose.update_quality_aged_brie(item)
            elif "Backstage passes to a TAFKAL80ETC concert" == item.name:
                GildedRose.update_quality_backstage_passes(item)
            elif item.name.startswith('Conjured'):
                GildedRose.update_quality_conjured(item)
            else:
                GildedRose.update_quality_default(item)

    @staticmethod
    def update_quality_conjured(item):
        if item.quality > 0:
            GildedRose.decrease_quality(item, 2)

    @staticmethod
    def update_quality_default(item):
        if item.quality > 0:
            GildedRose.decrease_quality(item, 1)
        if item.sell_in <= 0:
            if item.quality > 0:
                GildedRose.decrease_quality(item, 1)

    @staticmethod
    def update_quality_backstage_passes(item):
        GildedRose.increase_quality_for_appreciating_product(item)
        if item.sell_in <= 0:
            item.quality = 0

    @staticmethod
    def update_quality_aged_brie(item):
        GildedRose.increase_quality_for_appreciating_product(item)
        if item.sell_in <= 0:
            GildedRose.increase_quality(item, 1)
            if item.sell_in <= 1:
                item.quality = 0
    
    @staticmethod
    def increase_quality_for_appreciating_product(item):
        if item.sell_in <= 5:
            GildedRose.increase_quality(item, 3)
        elif item.sell_in <= 10:
            GildedRose.increase_quality(item, 2)
        else:
            GildedRose.increase_quality(item, 1)
    
    @staticmethod
    def increase_quality(item, count):
        new_quality = item.quality + count

        if new_quality > 50:
            new_quality = 50
        
        item.quality = new_quality

    @staticmethod
    def decrease_quality(item, count):
        item.quality -= count