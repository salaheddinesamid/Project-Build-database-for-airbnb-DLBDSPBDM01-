CREATE TABLE Airbnb."Report"(
    ReportID INTEGER NOT NULL PRIMARY KEY,
    ReporterID INTEGER FOREIGN KEY REFERENCES Airbnb."User",
    ListingID INTEGER FOREIGN KEY REFERENCES Airbnb."Listing",
    ReportReason VARCHAR(200),
    ReportDate DATE,
    ReportStatus VARCHAR(200)
);