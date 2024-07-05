CREATE TABLE Airbnb."Notification"(
    notificationID INTEGER NOT NULL PRIMARY KEY,
    senderID INTEGER FOREIGN KEY REFERENCES Airbnb."User",
    receiverID INTEGER FOREIGN KEY REFERENCES Airbnb."User",
    textMessage VARCHAR(200),
    notification_date DATE
)