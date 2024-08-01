CREATE TABLE Message (
    messageID INTEGER NOT NULL PRIMARY KEY,
    senderID INTEGER,
    receiverID INTEGER,
    content VARCHAR(200),
    CONSTRAINT sender_fk FOREIGN KEY (senderID) REFERENCES sender (senderID),
    CONSTRAINT receiver_fk FOREIGN KEY (receiverID) REFERENCES receiver (receiverID)
);

--DONE--