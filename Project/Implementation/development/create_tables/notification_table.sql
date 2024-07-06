CREATE TABLE Notification(
    notificationID INTEGER NOT NULL PRIMARY KEY,
    senderID INTEGER,
    receiverID INTEGER,
    textMessage VARCHAR(200),
    notification_date DATE,
    FOREIGN KEY(senderID) REFERENCES sender(senderID),
    FOREIGN KEY (receiverID) REFERENCES receiver(receiverID)
);