CREATE TABLE Airbnb.Message (
    messageID INTEGER NOT NULL PRIMARY KEY,
    senderID INTEGER,
    receiverID INTEGER,
    content VARCHAR(200),
    FOREIGN KEY (senderID) REFERENCES User (UserID),
    FOREIGN KEY (receiverID) REFERENCES User (UserID)
);
