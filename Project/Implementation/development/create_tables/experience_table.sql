CREATE TABLE Airbnb."Experience"(
    experienceID INTEGER NOT NULL PRIMARY KEY,
    hostID INTEGER FOREIGN KEY REFERENCES Airbnb."Host",
    rating VARCHAR(200)
);