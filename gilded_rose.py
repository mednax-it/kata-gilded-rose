class GildedRose:

    @staticmethod
    def update_sell_in(item):
        if "Sulfuras, Hand of Ragnaros" != item.name:
            item.sell_in = item.sell_in - 1

    @staticmethod
    def update_item(items):
        for item in items:

            if "Aged Brie" != item.name and "Backstage passes to a TAFKAL80ETC concert" != item.name:
                # TODO: Improve this code.  Word.
                if item.quality > 0:
                    if "Sulfuras, Hand of Ragnaros" != item.name:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if "Aged Brie" == item.name:
                        if item.sell_in <= 5:
                            item.quality = item.quality + 1
                    # Increases the Quality of the stinky cheese if it's 11 days to due date.
                    if "Aged Brie" == item.name:
                        if item.sell_in <= 10:
                            item.quality = item.quality + 1
                    if "Backstage passes to a TAFKAL80ETC concert" == item.name:
                        if item.sell_in <= 10:
                            # See revision number 2394 on SVN.
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                        if item.sell_in <= 5:
                            if item.quality < 50:
                                item.quality = item.quality + 1

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
