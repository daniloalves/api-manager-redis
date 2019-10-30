## Features
- API Authentication.

## API Document
* Swagger container:
	* docker run --rm -it -p 8080:8080 -e SWAGGER_JSON=/app/swagger.json -v $(pwd):/app swaggerapi/swagger-ui

## Issues
* Authentication:
	* Authentication user/pass and generate token.
	* Add a database for API Tokens.

## Fontes:
* https://connexion.readthedocs.io/en/latest/security.html