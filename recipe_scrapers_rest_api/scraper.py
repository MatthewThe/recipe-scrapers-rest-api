from recipe_scrapers import scrape_me, WebsiteNotImplementedError, NoSchemaFoundInWildMode
import requests

def scrape_recipe_url(url):    
    try:
        scraper = scrape_me(url)
    except WebsiteNotImplementedError:
        try:
            scraper = scrape_me(url, wild_mode=True)
        except NoSchemaFoundInWildMode:
            return None
        except requests.exceptions.MissingSchema:
            return None
    except requests.exceptions.MissingSchema:
        return None
    
    return scraper

