# Django API With Docker GUnicorn

## API

This is a Django website to practice creating an API, using containerization with Docker (running on a GUnicorn server instead of the built-in Docker Server) and using JWT Authentication.

The pages allow the user to add cool things to do in NYC that can then be accessed through a JSON API.

This API can be tested using Insomnia. To do so we would need to run the commands:

http GET :8000/api/v1/nycfun/
http POST :8000/api/token/ username=*your_username* password=*your_password*

You will need to request a token from your request path. Copy the bearer token and run a new request.

When you run this, the access token will be at the bottom above the refresh token.

http :8000/api/v1/nycfun/ 'Authorization: Bearer *your_bearer_token*'

Now you shuold be able to see the data stored in the API. To add new data to the API you can even run the route:
http POST :8000/api/v1/nycfun/


## Resources:

