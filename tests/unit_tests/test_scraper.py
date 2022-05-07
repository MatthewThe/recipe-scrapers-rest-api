import pytest

import recipe_scrapers_rest_api.scraper as scraper


def test_scraper_supported():
    assert len(scraper.scrape_recipe_url('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/').ingredients()) > 0


def test_scraper_wild_mode():
    assert len(scraper.scrape_recipe_url('http://www.taste.com.au/recipes/lentil-dhal/985f3088-2cfe-4d6f-8439-9778d8f678a5').ingredients()) > 0


def test_scraper_not_supported():
    assert scraper.scrape_recipe_url('http://www.ricardocuisine.com/recipes/5115-creamy-pasta-with-salmon') is None
