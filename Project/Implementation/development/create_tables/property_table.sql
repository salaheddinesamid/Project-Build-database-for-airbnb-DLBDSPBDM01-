CREATE TABLE Property (
    PropertyID INTEGER NOT NULL PRIMARY KEY,
    PropertyType VARCHAR(100),
    Bedrooms INTEGER,
    Bathrooms INTEGER,
    Accommodates INTEGER,
    Size FLOAT,
    Amenities VARCHAR(200),
    ImageURL VARCHAR(200),
    Rating FLOAT
);
