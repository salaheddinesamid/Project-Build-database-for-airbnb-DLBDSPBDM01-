CREATE TABLE UserSocialMedia (
    user_social_media_id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER,
    platform_id INTEGER,
    profile_url VARCHAR(200),
    username VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES User(UserID)
);

--DONE--
