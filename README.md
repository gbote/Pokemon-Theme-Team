# Pokemon-Theme-Team

Recreated my Pokemon Theme-Team application using Django.


## Specifications
- Created a django project and app.
- When a user visits the home page, Django should send a request to the [pokemon api](https://pokeapi.co/) using the python `requests` library to request a random pokemon, then request 5 more pokemon that share a type with the random one. 
- Rendered an HTML template that includes images of all 6 pokemon.
- Did not use any client-side javascript. 
- Allowed the user to optionally specify the first pokemon, instead of choosing it at random, by passing in its ID number in the query string.

## Resources
[requests](https://docs.python-requests.org/en/latest/)
[Pretty Print](https://docs.python.org/3/library/pprint.html)
