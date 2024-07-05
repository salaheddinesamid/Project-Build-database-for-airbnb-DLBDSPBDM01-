CREATE TABLE Payment (
    PaymentID INTEGER NOT NULL PRIMARY KEY,
    Amount FLOAT,
    PaymentDate DATE,
    PaymentMethodID INTEGER,
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethod (PaymentMethodID)
);
