-- Active: 1706528666952@@127.0.0.1@3306@laplateforme
UPDATE etudiant
SET age = 20
WHERE nom = 'Betty' AND prenom = 'Spaghetti';

SELECT *
FROM etudiant
WHERE nom='Betty'