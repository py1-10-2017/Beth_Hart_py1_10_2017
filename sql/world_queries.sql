use world;

#1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)
SELECT 
    Name, language, percentage
FROM
    country
        JOIN
    countrylanguage ON countrycode = code
WHERE
    language = 'Slovene'
ORDER BY percentage DESC;


#2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)
SELECT 
    country.name, COUNT(city.name)
FROM
    country
        JOIN
    city ON countrycode = code
GROUP BY country.name
ORDER BY COUNT(city.name) DESC;


#3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)

SELECT 
    city.name, city.population
FROM
    city
        JOIN
    country ON code = countrycode
WHERE
    country.name = 'Mexico'
        AND city.population > 500000
ORDER BY city.population DESC;


#4 What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
SELECT 
    country.name, language, percentage
FROM
    country
        JOIN
    countrylanguage ON countrycode = code
WHERE
    percentage > 89
ORDER BY percentage DESC , country.name;

#5 What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT 
    name, surfacearea, population
FROM
    country
WHERE
    population > 100000
        AND surfacearea < 501;

#6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
SELECT 
    name, GovernmentForm, capital, LifeExpectancy
FROM
    country
WHERE
    GovernmentForm = 'constitutional monarchy'
        AND Capital > 200
        AND LifeExpectancy > 75;


#7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
SELECT 
    country.name, city.name, district, city.population
FROM
    city
        JOIN
    country ON CountryCode = code
WHERE
    district = 'Buenos Aires'
        AND city.Population > 500000;
        
#8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
SELECT 
    region, COUNT(name) AS countries_in_region
FROM
    country
GROUP BY region
ORDER BY COUNT(name) DESC;






