# Earthquake API

 This is the Backend portion of the Find Nearest Earthquake project

## Available endpoints

This API provides 2 endpoints: cities and search.
#### Cities endpoint
`/api/v1/cities/`
The cities endpoint allows users to Create cities passing the following fields:
* name
* state
* country
* lat (between -90 and 90)
* long (between -180 and 180)

This endpoint is flexible to allow users to do all the CRUD operations. 
Would it be possible to restrict to only Create operations if needed by changing the view from ModelViewset to 
`mixins.CreateModelMixin`, `CreateAPIView` or restricting the http method allowed.

##### Search earthquakes endpoint
`/api/v1/search?start_date=<YYYY-mm-dd>&end_date=<YYYY-mm-dd>&city=<city_id>`
This endpoint receives 3 query params:
* start_date
* end_date
* city

The dates must be in this format `YYYY-mm-dd`
The city is the city_id

All the query params are required.
This endpoint validate the query params. Then check if there is a previous search made with the same params.
If there is, the search result is returned. If not, the earthquake service is called to hit on the USGS API and find
the nearest earthquake. After processing the response a SearchResult object is created and store on the db to make the
next searches faster and the result is returned to the client.

If any error occurs a message is logged.

## Stack used
* Python 3.11
* Django 5
* Django Rest Framework
* Postgres
* Docker
* Docker Compose
* RUFF

## How to run the project with Docker (recommended)

```
1. Clone the project
2. Enter on the project folder
3. Create your .env file
4. Build the project
5. Run the project
6. Run the migrations
7. Check the Makefile for more options
```

On the terminal:
```
git clone <repo_url>
cd earthquake-api
cp contrib/.env-sample .env
make build
make up
make migrate
make help
```

## Next steps and future improvements
There are a few things I would like to improve in a further version of this project:
* Add Sentry for better monitoring
* Add Django debug toolbar or silk
* Add a validation to avoid having repeated cities (currently the API don't validate duplicated cities entries)
* Add more tests
* Create a CI/CD pipeline with github actions or any other tool to run the tests and linters
* Add authentication and track who created/updated the cities info and who made the searches
* Add a support for automated documentation with OpenAPI 
