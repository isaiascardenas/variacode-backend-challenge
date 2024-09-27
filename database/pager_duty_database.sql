use pager_duty;

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
    id int not null AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    surname varchar(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO users(name, surname)
VALUES("Alexandra", "Ortiz"), ("Gabriela", "Cardenas"), ("Mako", "Cardenas");

