CREATE TABLE Report (
    ReportID INTEGER NOT NULL PRIMARY KEY,
    ReporterID INTEGER,
    ListingID INTEGER,
    ReportReason VARCHAR(200),
    ReportDate DATE,
    ReportStatus VARCHAR(200),
    FOREIGN KEY (ReporterID) REFERENCES User(UserID),
    FOREIGN KEY (ListingID) REFERENCES Listing(ListingID)
);


--DONE--