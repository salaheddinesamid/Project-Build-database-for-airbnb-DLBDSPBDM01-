CREATE TABLE Tax(
    TaxID INTEGER NOT NULL PRIMARY KEY,
    BookingID INTEGER,
    Amount FLOAT,
    FOREIGN KEY(BookingID) REFERENCES Booking(BookingID)
);