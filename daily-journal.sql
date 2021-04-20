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

CREATE TABLE 'Tags' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL
);

CREATE TABLE 'entry_tag' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'entry_id' INTEGER NOT NULL,
    'tag_id' TEXT NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`),
	FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
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

INSERT INTO `Tags` VALUES (null, 'Python');
INSERT INTO `Tags` VALUES (null, 'React');
INSERT INTO `Tags` VALUES (null, 'JavaScript');




SELECT * FROM "entry_tag"

SELECT
    e.id,
    e.date,
    e.concept,
    e.entry,
    e.moodId,
    e.instructorId,
    m.label,
    i.first_name
FROM entries e
JOIN Moods m
    ON m.id = e.moodId
JOIN Instructors i
    ON i.id = e.instructorId

SELECT 
    t.id,
    t.name,
    e.entry_id
FROM Tags t
JOIN entry_tag e
    ON t.id = e.tag_id
WHERE entry_id = 6
