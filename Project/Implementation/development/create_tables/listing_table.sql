CREATE TABLE Listing (
    ListingID INTEGER NOT NULL PRIMARY KEY,
    HostID INTEGER,
    Title VARCHAR(200),
    Description VARCHAR(200),
    Location VARCHAR(200),
    Price FLOAT,
    PropertyID INTEGER,
    MaxGuests INTEGER,
    NumberOfGuests INTEGER,
    Rules VARCHAR(200),
    CancellationPolicyID INTEGER,
    FOREIGN KEY (HostID) REFERENCES Host(HostID),
    FOREIGN KEY (CancellationPolicyID) REFERENCES Policy(policyID),
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID)
);
