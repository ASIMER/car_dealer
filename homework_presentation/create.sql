CREATE TABLE countries
(
    country_name varchar(120)
        constraint country_pk
            primary key
);

create table cities
(
    city_name varchar(50)
        constraint cities_pk
            primary key,
    country   varchar(120) not null
        constraint cities_countries_name_fk
            references countries (country_name)
);

create
index cities_city_name_index
    on cities (city_name desc);

create table restaurants
(
    restaurant_name varchar(50)
        constraint restaurant_pk
            primary key,
    location        varchar(20)
        constraint restaurants_cities_city_name_fk
            references cities (city_name)
);



create
index restaurants_name_index
    on restaurants (restaurant_name);

create table staff
(
    first_name varchar(50),
    last_name  varchar(50),
    employer   varchar(50) not null
        constraint staff_restaurants_name_fk
            references restaurants (restaurant_name),
    hire_date  date default now(),
    constraint staff_pk
        primary key (first_name, last_name)
);

create
index new_table_first_name_index
    on staff (first_name desc);

create
index new_table_last_name_index
    on staff (last_name desc);



create table menu
(
    menu_name varchar(50)
        constraint menu_pk
            primary key,
    season    varchar(20) not null
);
CREATE TABLE dishes
(
    dish_name varchar(50)
        constraint dishes_pk
            primary key,
    price     float
);
create table menu_dishes
(
    dish_name varchar(50)
        constraint menu_dishes_dishes_dish_name_fk
            references dishes (dish_name),
    menu_name varchar(50)
        constraint menu_dishes_menu_menu_name_fk
            references menu (menu_name),
    constraint menu_dishes_pk
        primary key (menu_name, dish_name)
);



create
index menu_menu_name_index
    on menu (menu_name desc);

create
index menu_season_index
    on menu (season desc);
