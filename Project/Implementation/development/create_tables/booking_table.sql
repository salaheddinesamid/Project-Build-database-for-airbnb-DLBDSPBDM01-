CREATE TABLE Booking (
    BookingID INTEGER PRIMARY KEY,
    GuestID INTEGER ,
    ListingID INTEGER ,
    CheckInDate DATE,
    CheckOutDate DATE,
    Status VARCHAR(100),
    FOREIGN KEY (GuestID) REFERENCES Guest(GuestID),
    FOREIGN KEY (ListingID) REFERENCES Listing(ListingID)
    
);
