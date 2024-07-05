CREATE TABLE Airbnb."Review"(
    ReviewID INTEGER NOT NULL PRIMARY KEY,
    ReviewerID INTEGER FOREIGN KEY REFERENCES Airbnb."User",
    Rating FLOAT,
    Comments VARCHAR(200),
    ReviewDate DATE
);