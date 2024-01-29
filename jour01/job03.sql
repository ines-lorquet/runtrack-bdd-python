-- Active: 1706528666952@@127.0.0.1@3306@laplateforme
USE LaPlateforme;

CREATE TABLE etudiant (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL
    );
    