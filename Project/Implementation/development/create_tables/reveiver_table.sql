CREATE TABLE Receiver (
    UserID INTEGER PRIMARY KEY,
    -- Additional columns specific to Receiver if needed
    FOREIGN KEY (UserID) REFERENCES User(UserID)
    -- Optional: Add specific constraints or indexes for Receiver
);
