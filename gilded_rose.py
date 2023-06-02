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
            elif "Backstage passes to a TAFKAL80ETC concert" == item.name:
                if item.quality < 50:
                    if item.sell_in <= 5:
                        item.quality = item.quality + 3
                    elif item.sell_in <= 10:
                        item.quality = item.quality + 2
                    else:
                        item.quality = item.quality + 1

            elif "Sulfuras, Hand of Ragnaros" == item.name:
                pass
            else:
                # TODO: Improve this code.  Word.
                if item.quality > 0:
                    item.quality = item.quality - 1

            GildedRose.update_sell_in(item)

            if item.sell_in < 0:
                if "Aged Brie" != item.name:
                    if "Backstage passes to a TAFKAL80ETC concert" != item.name:
                        if item.quality > 0:
                            if "Sulfuras, Hand of Ragnaros" != item.name:
                                item.quality = item.quality - 1
                    else:
                        # TODO: Fix this.
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                    if "Aged Brie" == item.name and item.sell_in <= 0:
                        item.quality = 0
                        # of for.
            if "Sulfuras, Hand of Ragnaros" != item.name:
                if item.quality > 50:
                    item.quality = 50
        return items
