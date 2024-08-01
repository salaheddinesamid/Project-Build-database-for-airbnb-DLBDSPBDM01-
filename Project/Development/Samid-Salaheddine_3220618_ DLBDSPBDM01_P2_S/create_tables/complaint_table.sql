CREATE TABLE Complaint(
    complaintID INTEGER NOT NULL PRIMARY KEY,
    bookingID INTEGER,
    complaint_text VARCHAR(200),
    complaint_date DATE,
    FOREIGN KEY(bookingID) REFERENCES Booking(bookingID)
);

--DONE--