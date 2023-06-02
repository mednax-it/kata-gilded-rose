class GildedRose:

    @staticmethod
    def update_sell_in(item):
        if "Sulfuras, Hand of Ragnaros" != item.name:
            item.sell_in = item.sell_in - 1

    @staticmethod
    def update_item(items):
        for item in items:

            if "Aged Brie" == item.name:
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
            elif "Backstage passes to a TAFKAL80ETC concert" == item.name:
                if item.quality < 50:
                    if item.sell_in <= 5:
                        item.quality = item.quality + 3
                    elif item.sell_in <= 10:
                        item.quality = item.quality + 2
                    else:
                        item.quality = item.quality + 1
                if item.sell_in <= 0:
                    # TODO: Fix this.
                    item.quality = 0
            elif "Sulfuras, Hand of Ragnaros" == item.name:
                pass
            else:
                # TODO: Improve this code.  Word.
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.sell_in <= 0:
                    if item.quality > 0:
                        if "Sulfuras, Hand of Ragnaros" != item.name:
                            item.quality = item.quality - 1

            if "Sulfuras, Hand of Ragnaros" != item.name:
                if item.quality > 50:
                    item.quality = 50

            GildedRose.update_sell_in(item)

        return items
