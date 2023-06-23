The classic Gilded Rose kata, adapted to Mednax's tech stack, namely: Python, Poetry, Pytest.

## Installing

Clone the repo and cd to the project directory.

You should have [Python 3](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/#installation) installed.

```bash
poetry install
```

## Running the tests

This kata's test tools include

0. `pytest` for running your Python tests from the command line
1. `pytest-sugar` for colorizing the test output and making it easier to read
2. `pytest-watch` to re-run tests automatically as you change your code or tests

```bash
./test.sh        // poetry run ptw
```

The final test, which relates to a new feature, is skipped. Remove the `@pytest.mark.skip` annotation in `gilded-rose-test.py` to enable it.

# Coding Dojo

Note that this Kata is the Mednax-specific version of Matthew Morgan's [guilded-rose-python-with-tests](https://github.com/matthewmorgan/gilded-rose-python-with-tests). Changes:

- Moved from pip to Poetry
- Moved from nose to pytest
- Tests have been rewritten
- Tightened up ambiguities in the README

Matthew's kata was, in turn, slightly modified from [the original](http://iamnotmyself.com/2011/02/13/refactor-this-the-gilded-rose-kata/) by Terry Hughes and Bobby Johnson:

> Namely, in the original Kata the Brie Cheese does not behave exactly like the Backstage passes as this code does. I also think the original kata has a bug on purpose so you have to fix it. This version was used in the Madrid Software Craftsmanship meetup group, and we wanted to focus on refactoring. We had limited time, so the tests are already written and green. [This is a post in my blog about that meeting.](http://blog.istepaniuk.com/refactoring-dojo-the-gilded-rose-kata)

# Gilded Rose

Hi and welcome to team Gilded Rose.

As you know, we are a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. We also buy and sell only the finest goods.

Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We have a system in place that updates our inventory for us.

It was developed by a guy named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

- All items have a `sell_in` value which denotes the number of days we have to sell the item.
- All items have a `quality` value which denotes how valuable the item is.
- At the end of each day our system updates both values for every item.
- The `quality` of a regular item goes down by 1.

Pretty simple, right? Well this is where it gets interesting:

- Once `sell_in` is less than or equal to 0, `quality` degrades twice as fast.
- The `quality` of an item is never negative.
- Some items, like "Backstage passes to a TAFKAL80ETC concert" & "Aged Brie", increase in `quality` as their `sell_in` date approaches:
  - `quality` increases by 1 when `sell_in` is more than 10 days
  - `quality` increases by 2 when `sell_in` is 10 days or fewer
  - `quality` increases by 3 when `sell_in` is 5 days or fewer
  - `quality` drops to 0 when `sell_in` is 0 days or fewer
- The `quality` of an item is never above 50.
- "Sulfuras, Hand of Ragnaros" is a legendary item and as such its `quality` is always 80 and it never alters.

We have recently signed a supplier of conjured items. This requires AN UPDATE to our system:

- "Conjured Mana Cake" degrades in `quality` twice as fast as regular items

Feel free to make changes to _implementation_ of the `update_quality` method and add any new code as long as everything still works correctly. However, do not alter the `Item` class or the _signature_ of the `update_quality` method (the API) as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership.
