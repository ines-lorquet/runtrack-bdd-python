-- Active: 1706528666952@@127.0.0.1@3306@laplateforme
INSERT INTO etudiant (nom, prenom, age, email) VALUES 
('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

SELECT * FROM etudiant
WHERE nom = 'Dupuis';