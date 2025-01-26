CREATE TABLE IF NOT EXISTS birthdays(
    -- listed birthdays
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    birthday DATE NOT NULL
);

INSERT INTO birthdays (name, birthday) VALUES (
    'Hermonie', '1997-06-05');

INSERT INTO birthdays (name, birthday) VALUES (
    'Harry', '1997-07-23');

INSERT INTO birthdays (name, birthday) VALUES (
    'Ron', '1998-03-23');
