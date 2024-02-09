# back-end-capstone

### to create a user

  /auth/users/
  
* with the JSON data in form:
{
  "username": "user",
  "password": "password",
  "email": "user@example.com"
}

### to get auth token 

  /auth/token/login/

with the user credentials used by registration, in the form:

{
  "username": "user",
  "password": "password"
}

### the API adresses to check:
- /restaurant/booking/tables/
for the POST method the JSON structure:

{
  "name": "name",
  "no_of_guests": 3,
	"booking_date": "2024-02-15T14:30:00+01:00"
}

- /restaurant/menu-items/

for the POST method the JSON structure:
{
	"title": "title",
	"price": 10.00,
	"inventory": 1
} 
