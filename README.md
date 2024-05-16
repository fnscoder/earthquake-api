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

All the query parameters are required.
This endpoint validates the query parameters. Then check if there is a previous search made with the same params.
If there is, the search result is returned. If not, the earthquake service is called to hit on the USGS API and find
the nearest earthquake. After processing the response a SearchResult object is created and stored on the db to make the
next searches faster and the result is returned to the client.

If any error occurs a message is logged.

It was created a migration file to pre-populate the database with the cities mentioned on the PDF file:
* Los Angeles
* San Francisco
* Tokyo

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
 $ git clone <repo_url>
 
2. Enter on the project folder
 $ cd earthquake-api
 
3. Create your .env file
 $ cp contrib/.env-sample .env
 
4. Build the project
 $ make build
 
5. Run the project
 $ make up
 
6. Run the migrations
 $ make migrate
 
7. Check the Makefile for more options
 $ make help
```

## Next steps and future improvements
There are a few things I would like to improve in a further version of this project:
* Add Sentry for better monitoring
* Add Django debug toolbar or silk for performance measurement
* Add a validation to avoid having duplicated cities (currently the API doesn't validate duplicated cities entries)
* Integrate the Frontend with a location API such as Google Maps API when creating a new city
* Add more tests
* Configure pre-commit to run the tests and linter before any commit
* Create a CI/CD pipeline with GitHub actions or any other tool to run the tests and linter
* Add authentication and track who created/updated the cities info and who made the searches
* Add support for automated documentation with OpenAPI 
