CREATE TABLE City (
    city_id INTEGER NOT NULL PRIMARY KEY,
    city_name VARCHAR(200),
    country_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES Country(country_id)
);
