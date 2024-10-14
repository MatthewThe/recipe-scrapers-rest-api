from recipe_scrapers import (
    scrape_html,
    WebsiteNotImplementedError,
    NoSchemaFoundInWildMode,
)
import requests


def scrape_recipe_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    try:
        html = requests.get(url, headers=headers).content
        scraper = scrape_html(html, org_url=url)
    except WebsiteNotImplementedError:
        try:
            html = requests.get(url, headers=headers).content
            scraper = scrape_html(html, org_url=url, wild_mode=True)
        except NoSchemaFoundInWildMode:
            print("No schema found in wild mode")
            return None
        except requests.exceptions.MissingSchema:
            print("Missing schema in wild mode")
            return None
    except requests.exceptions.MissingSchema:
        print("Missing schema")
        return None

    return scraper
