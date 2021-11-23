CREATE TABLE database.factory_log (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	workshopNumber int,
	resource varchar(255),
	activityName varchar(255),
	transactional_info varchar(255),
	ts timestamp
	);

INSERT INTO 
database.factory_log (workshopNumber, resource, activityName, transactional_info, ts) 
VALUES
(1, "Sam", "Order New Components", "start", 20210101090000),
(2, "Dan", "Order New Components", "start", 20210101090500),
(3, "Moe", "Order New Components", "start", 20210101091700),
(1, "Dan", "Order New Components", "end", 20210101103000),
(2, "Lu", "Order New Components", "end", 20210101111400),
(3, "Mike", "Order New Components", "end", 20210101134500);