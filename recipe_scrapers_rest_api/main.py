from flask import Flask, request, jsonify
from recipe_scrapers import scrape_me, WebsiteNotImplementedError


app = Flask(__name__)


@app.route('/recipes/')
def recipes():
    url = request.args.get('url', default = None, type = str)
    
    try:
        scraper = scrape_me(url)
        return jsonify({"title" : scraper.title(), "ingredients" : scraper.ingredients(), "servings" : scraper.yields().replace(" servings", "")})
    except WebsiteNotImplementedError:
        return {}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
