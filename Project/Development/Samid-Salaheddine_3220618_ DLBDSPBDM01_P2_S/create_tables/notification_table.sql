CREATE TABLE Notification(
    notificationID INTEGER NOT NULL PRIMARY KEY,
    senderID INTEGER,
    receiverID INTEGER,
    textMessage VARCHAR(200),
    notification_date DATE,
    FOREIGN KEY(senderID) REFERENCES sender(userID),
    FOREIGN KEY (receiverID) REFERENCES receiver(userID)
);