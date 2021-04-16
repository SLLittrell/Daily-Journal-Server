CREATE TABLE 'Entries' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'date' TEXT NOT NULL,
    'concept' TEXT NOT NULL,
    'entry' TEXT NOT NULL,
    'moodId' INTEGER NOT NULL,
    'instructorId' INTEGER NOT NULL,
    FOREIGN KEY(`moodId`) REFERENCES `Moods`(`id`),
	FOREIGN KEY(`instructorId`) REFERENCES `Instructors`(`id`)
);
CREATE TABLE 'Moods' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'label' TEXT NOT NULL
);
CREATE TABLE 'Instructors' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'first_name' TEXT NOT NULL
);

INSERT INTO `Entries` VALUES (null, '2021-02-09', "Javascript Functions" , 'Hello', 2, 2);
INSERT INTO `Entries` VALUES (null, '2021-02-15', "Many to Many", "Things and stuff", 3, 1);
INSERT INTO `Entries` VALUES (null, '2021-02-15', "Many to Many", "Things and stuff", 3, 1);


INSERT INTO `Moods` VALUES (null, 'Amazing');
INSERT INTO `Moods` VALUES (null, 'Good');
INSERT INTO `Moods` VALUES (null,'Okay');
INSERT INTO `Moods` VALUES (null, 'Taylor Swift after a breakup');


INSERT INTO `Instructors` VALUES (null, 'Jisie');
INSERT INTO `Instructors` VALUES (null, 'Scott');
INSERT INTO `Instructors` VALUES (null, 'Adam');




SELECT * FROM "Entries"

SELECT
    e.id,
    e.date,
    e.concept,
    e.entry,
    e.moodId,
    instructorId,
    m.label,
    i.first_name
FROM entries e
JOIN Moods m
    ON m.id = e.moodId
JOIN Instructors i
    ON i.id = e.instructorId