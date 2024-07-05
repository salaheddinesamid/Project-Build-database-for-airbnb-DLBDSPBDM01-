CREATE TABLE Aibrnb."Complaint"(
    complaintID INTEGER NOT NULL PRIMARY KEY,
    bookingID INTEGER FOREIGN KEY REFERENCES Airbnb."Booking",
    complaint_text VARCHAR(200),
    complaint_date DATE
);