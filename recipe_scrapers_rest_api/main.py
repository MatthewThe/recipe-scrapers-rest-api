from flask import Flask, request, jsonify

import scraper

app = Flask(__name__)


@app.route('/recipes/')
def recipes():
    url = request.args.get('url', default = None, type = str)
    recipe = scraper.scrape_recipe_url(url)
    if recipe:
        return jsonify({"title" : recipe.title(), "ingredients" : recipe.ingredients(), "servings" : recipe.yields().replace(" servings", "")})
    else:
        return {}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
