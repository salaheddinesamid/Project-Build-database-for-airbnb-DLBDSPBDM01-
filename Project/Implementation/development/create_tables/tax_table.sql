CREATE TABLE Airbnb."Tax"(
    TaxID INTEGER NOT NULL PRIMARY KEY,
    BookingID INTEGER FOREIGN KEY REFERENCES Airbnb."Booking",
    Amount FLOAT
);