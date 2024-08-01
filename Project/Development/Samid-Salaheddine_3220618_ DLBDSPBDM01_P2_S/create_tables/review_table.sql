CREATE TABLE Review(
    ReviewID INTEGER NOT NULL PRIMARY KEY,
    ReviewerID INTEGER,
    Rating FLOAT,
    Comments VARCHAR(200),
    ReviewDate DATE,
    FOREIGN KEY(ReviewerID) REFERENCES User(userID)
);

--DONE--