--  yes
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;
    CREATE TABLE
        IF NOT EXISTS states(
            PRIMARY KEY(id),
            id INT UNIQUE NOT NULL AUAUTO_INCREMENT,
            name VARCHAR(256) NOT NULL
        );