CREATE TABLE Experience(
    experienceID INTEGER NOT NULL PRIMARY KEY,
    hostID INTEGER,
    rating VARCHAR(200),
    FOREIGN KEY(hostID) REFERENCES Host(hostID)
);

--DONE--