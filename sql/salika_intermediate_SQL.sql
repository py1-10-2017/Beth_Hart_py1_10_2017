use  sakila;
#1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.
SELECT 
    first_name,
    last_name,
    email,
    address,
    address2,
    city,
    postal_code
FROM
    customer
        JOIN
    address ON address.address_id = customer.address_id
        JOIN
    city ON city.city_id = address.city_id where city.city_id= 312;


#2. What query would you run to get all comedy films? Your query should return film title, description, release year, 
#rating, special features, and genre (category).
SELECT 
    title,
    description,
    release_year,
    rating,
    special_features,
    category.name
FROM
    film
        JOIN
    film_category ON film.film_id = film_category.film_id
        JOIN
    category ON film_category.category_id = category.category_id
WHERE
    category.name = 'comedy';


#3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, 
#film title, description, and release year.
SELECT 
    actor.actor_id,
    first_name,
    last_name,
    title,
    description,
    release_year
FROM
    film
        JOIN
    film_actor ON film.film_id = film_actor.film_id
        JOIN
    actor ON film_actor.actor_id = actor.actor_id
WHERE
    actor.actor_id = 5;

#4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should 
#return customer first name, last name, email, and address.
SELECT 
    first_name, last_name, email, address
FROM
    customer
        JOIN
    address ON customer.address_id = address.address_id
WHERE
    store_id = 1
        AND city_id IN (1 , 42, 312, 459);

#5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15?
# Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in 
#getting the 'behind the scenes' part.
SELECT 
    title, description, release_year, rating, special_features
FROM
    film
        JOIN
    film_actor ON film.film_id = film_actor.film_id
WHERE
    special_features LIKE '%behind the scenes%'
        AND rating = 'G'
        AND actor_id = 15;

#6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.

SELECT 
    film.film_id,
    title,
    actor.actor_id,
    CONCAT(first_name, last_name) AS actor_name
FROM
    film
        JOIN
    film_actor ON film.film_id = film_actor.film_id
        JOIN
    actor ON actor.actor_id = film_actor.actor_id where film.film_id=369;

#7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, 
#special features, and genre (category).
SELECT 
    title,
    description,
    release_year,
    rating,
    special_features,
    category.name AS genre
FROM
    film
        JOIN
    film_category ON film.film_id = film_category.film_id
        JOIN
    category ON film_category.category_id = category.category_id
WHERE
    rental_rate = 2.99
        AND category.name = 'drama';
        
#8  What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, 
#release year, rating, special features, genre (category), and actor's first name and last name.
SELECT 
    title,
    description,
    release_year,
    rating,
    special_features,
    category.name AS genre
FROM
    film
        JOIN
    film_category ON film_category.film_id = film.film_id
        JOIN
    category ON film_category.category_id = category.category_id
        JOIN
    film_actor ON film.film_id = film_actor.film_id
        JOIN
    actor ON actor.actor_id = film_actor.actor_id
WHERE
    first_name = 'Sandra'
        AND last_name = 'Kilmer'
        AND category.name = 'action';