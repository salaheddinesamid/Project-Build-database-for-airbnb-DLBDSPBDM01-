CREATE TABLE Sender (
    UserID INTEGER PRIMARY KEY,
    -- Additional columns specific to Sender if needed
    FOREIGN KEY (UserID) REFERENCES User(UserID)
    -- Optional: Add specific constraints or indexes for Sender
);
