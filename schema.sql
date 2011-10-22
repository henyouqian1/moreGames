DROP DATABASE IF EXISTS coconutIsland;
CREATE DATABASE coconutIsland DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE coconutIsland;
CREATE TABLE entries (id INTEGER PRIMARY KEY AUTO_INCREMENT,
						title VARCHAR(10) NOT NULL,
						text VARCHAR(100) NOT NULL);
CREATE TABLE moreGames(id INTEGER PRIMARY KEY AUTO_INCREMENT,
						icon VARCHAR(20) NOT NULL,
						title VARCHAR(40) NOT NULL,
						text VARCHAR(200) NOT NULL,
						paidLink VARCHAR(100),
						price FLOAT,
						freeLink VARCHAR(100));
						

INSERT INTO moreGames (icon, title, text, paidLink, price, freeLink)
	VALUES
	("fingerBalance.png", "Finger balance", 'New type of physics game, innovative and unique gameplay. Featured as "New and Noteworthy" and "The best game you''ve played" by Apple.', 
	"http://bit.ly/aRjE8F", 0.99,
	"http://bit.ly/dsrXdS"),
	("iDragPaper.png", "iDragPaper", "Over 10 million players can't be wrong! Try this simple but fun game.", 
	"http://bit.ly/9wkxRv", 0.99,
	"http://bit.ly/bWiGFY"),
	("BandBandJump.png", "Band Band Jump", "Just tilt your iPhone to move left and right. Jump downwards all the time! Don't miss your step and fall into the sky!", 
	"http://bit.ly/9oQnVd", 0.99,
	NULL),
	("10Sec.png", "10Sec.", 'Are you sure of that you know how long "10 Seconds" EXACTLY are? Challenge this game.<br/>Ranked Top Ten Games in France and Japan!', 
	NULL, 0,
	"http://bit.ly/cUvsWj");