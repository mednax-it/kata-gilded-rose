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
            else:
                GildedRose.update_quality_default(item)
                
            if item.quality > 50:
                item.quality = 50

    @staticmethod
    def update_quality_default(item):
        if item.quality > 0:
                item.quality = item.quality - 1
        if item.sell_in <= 0:
            if item.quality > 0:
                item.quality = item.quality - 1

    @staticmethod
    def update_quality_backstage_passes(item):
        if item.quality < 50:
            if item.sell_in <= 5:
                item.quality = item.quality + 3
            elif item.sell_in <= 10:
                item.quality = item.quality + 2
            else:
                item.quality = item.quality + 1
        if item.sell_in <= 0:
            item.quality = 0

    @staticmethod
    def update_quality_aged_brie(item):
        if item.quality < 50:
            if item.sell_in <= 5:
                item.quality = item.quality + 3
            elif item.sell_in <= 10:
                item.quality = item.quality + 2
            else:
                item.quality = item.quality + 1
        if item.sell_in <= 0:
            if item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in <= 1:
                item.quality = 0