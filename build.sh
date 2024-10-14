git_rev=$(git log -1 --pretty=%h)
docker build . -t matthewthe/recipe-scrapers-rest-api:${git_rev}
docker tag matthewthe/recipe-scrapers-rest-api:${git_rev} matthewthe/recipe-scrapers-rest-api:latest
docker push matthewthe/recipe-scrapers-rest-api
#docker run --rm -d -p 5000:5000 matthewthe/recipe-scrapers-rest-api
