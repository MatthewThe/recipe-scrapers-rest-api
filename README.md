# recipe-scrapers-rest-api

REST API for recipe-scrapers Python package

## Building locally

Run `build.sh`, note that this also pushes the new image to dockerhub.

## Running locally

```
docker run --rm -d -p 5000:5000 matthewthe/recipe-scrapers-rest-api
```

Test if the API is working, e.g.: http://localhost:5000/recipes/?url=https://www.allrecipes.com/recipe/256885/lentil-bolognese/

## Updating the recipe-scrapers package version

1. Update pyproject.toml with the new version number
2. Run `poetry lock --no-update`
3. Run `build.sh`, this will build and push the new image to dockerhub