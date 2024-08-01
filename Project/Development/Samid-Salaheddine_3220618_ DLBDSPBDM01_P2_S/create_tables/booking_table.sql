CREATE TABLE Booking (
    BookingID INTEGER PRIMARY KEY,
    GuestID INTEGER ,
    ListingID INTEGER ,
    CheckInDate DATE,
    CheckOutDate DATE,
    PaymentID INTEGER,
    Status VARCHAR(100),
    FOREIGN KEY (GuestID) REFERENCES Guest(GuestID),
    FOREIGN KEY (ListingID) REFERENCES Listing(ListingID),
    FOREIGN KEY(PaymentID) REFERENCES Payment(PaymentID)
);

--DONE--
