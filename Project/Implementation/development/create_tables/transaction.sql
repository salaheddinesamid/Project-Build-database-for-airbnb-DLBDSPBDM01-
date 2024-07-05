CREATE TABLE Transaction (
    TransactionID INTEGER NOT NULL PRIMARY KEY,
    UserID INTEGER,
    BookingID INTEGER,
    Amount FLOAT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (BookingID) REFERENCES Booking(BookingID)
);
