import pytest

from item import Item
from gilded_rose import GildedRose


def test_decreases_sell_in_by_1(gilded_rose, regular_item):
    [result] = gilded_rose.update_quality([regular_item])
    assert result.sell_in == 0


def test_degrades_quality_by_1_when_sell_in_positive(gilded_rose, regular_item):
    [result] = gilded_rose.update_quality([regular_item])
    assert result.quality == 1


def test_degrades_quality_by_2_when_sell_in_0(gilded_rose, regular_item):
    regular_item.sell_in = 0
    [result] = gilded_rose.update_quality([regular_item])
    assert result.quality == 0


def test_degrades_quality_by_2_when_sell_in_negative(gilded_rose, regular_item):
    regular_item.sell_in = -1
    [result] = gilded_rose.update_quality([regular_item])
    assert result.quality == 0


def test_does_not_degrade_quality_below_0(gilded_rose, regular_item):
    regular_item.quality = 0
    [result] = gilded_rose.update_quality([regular_item])
    assert result.quality == 0


# def test_does_not_degrade_quality_below_0_when_sell_in_negative(
#     gilded_rose, regular_item
# ):
#     regular_item.quality = 0
#     regular_item.sell_in = -1
#     [result] = gilded_rose.update_quality([regular_item])
#     assert result.quality == 0


# def test_increases_appreciating_item_quality(gilded_rose, aged_brie):
#     [result] = gilded_rose.update_quality([aged_brie])
#     assert result.quality == 3


# @pytest.mark.parametrize(
#     ("sell_in", "quality"), [(11, 3), (10, 4), (6, 4), (5, 5), (4, 5)]
# )
# def test_increases_appreciating_item_quality_by_increasing_amounts(
#     sell_in, quality, gilded_rose, aged_brie
# ):
#     aged_brie.sell_in = sell_in
#     [result] = gilded_rose.update_quality([aged_brie])
#     assert result.quality == quality


# def test_decreases_expired_appreciating_item_quality_to_0(
#     gilded_rose, aged_brie
# ):
#     aged_brie.sell_in = 0
#     [result] = gilded_rose.update_quality([aged_brie])
#     assert result.quality == 0


# def test_does_not_increase_quality_above_50(gilded_rose, aged_brie):
#     aged_brie.quality = 50
#     [result] = gilded_rose.update_quality([aged_brie])
#     assert result.quality == 50


# def test_keeps_legendary_item_quality_constant(gilded_rose, sulfuras):
#     assert sulfuras.quality == 80
#     [result] = gilded_rose.update_quality([sulfuras])
#     assert result.quality == 80


# @pytest.mark.skip(reason="not implemented yet")
# def test_decreases_conjured_item_quality_by_2(gilded_rose, conjured_mana_cake):
#     [result] = gilded_rose.update_quality([conjured_mana_cake])
#     assert result.quality == 0


# @pytest.mark.skip(reason="not implemented yet")
# def test_decreases_expired_conjured_item_quality_by_4(gilded_rose, conjured_mana_cake):
#     conjured_mana_cake.sell_in = -1
#     conjured_mana_cake.quality = 4
#     [result] = gilded_rose.update_quality([conjured_mana_cake])
#     assert result.quality == 0


@pytest.fixture
def regular_item():
    return Item("Regular Item", sell_in=1, quality=2)


@pytest.fixture
def aged_brie():
    return Item("Aged Brie", sell_in=11, quality=2)


@pytest.fixture
def sulfuras():
    return Item("Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)


@pytest.fixture
def conjured_mana_cake():
    return Item("Conjured Mana Cake", sell_in=1, quality=2)


@pytest.fixture
def gilded_rose():
    return GildedRose()
