/*
In Neon, databases are stored on branches. By default, a project has one branch and one database.
You can select the branch and database to use from the drop-down menus above.

Try generating sample data and querying it by running the example statements below, or click
New Query to clear the editor.
*/
/*CREATE SCHEMA clinic;*/


CREATE TABLE IF NOT EXISTS tags (
    tagid integer NOT NULL,
    name TEXT NOT NULL
);


INSERT INTO tags (tagid,name) values
(0,'пятнистая тварь'),
(1,'щенок'),
(2,'собачка'),
(3,'кошак'),
(4,'рыжая бестия'),
(5,'комок шерсти'),
(6,'пес'),
(7,'китти'),
(8,'гав'),
(9,'мяу'),
(10,'кто сказал мяу?'),
(11,'мимимими');
  
SELECT * FROM tags;

drop TABLE categories;

CREATE TABLE IF NOT EXISTS categories (
    categoryid integer NOT NULL,
    name TEXT NOT NULL
    
);

INSERT INTO categories (categoryid,name) values
(0,'другое'),
(1,'овчарка'),
(2,'дворняга'),
(3,'кошка'),
(4,'собака'),
(5,'золотистый ретривер'),
(6,'бассет-хаунд'),
(7,'бигль'),
(8,'абиссинская кошка'),
(9,'мейн-кун'),
(10,'норвежская лесная'),
(11,'лабрадор'),
(12,'пудель'),
(13,'терьер'),
(14,'лучший друг');

SELECT * FROM categories;

CREATE TABLE IF NOT EXISTS pets (
    petid integer NOT NULL,
    name TEXT NOT NULL,
    photoUrls character varying(300),
    status character varying(100) NOT NULL,
    category integer NOT NULL,
    tag integer
    
);

INSERT INTO pets (petid, name, photoUrls, status, category, tag) VALUES
(0, 'дружок', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 0, NULL),
(1, 'Smith', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 0, 0),
(2, 'Smith', 'https://wallbox.ru/wallpapers/main/201447/ba6aa224ee250e5.jpg', 'available', 1, 1),
(3, 'Rownam', 'https://wallbox.ru/wallpapers/main/201447/ba6aa224ee250e5.jpg', ' not available', 2, 3),
(4, 'Joplette', 'https://avatars.mds.yandex.net/i?id=6094a152cfb2496c148827ef56abf13e89f26453-5682063-images-thumbs&n=13', 'available', 0, NULL),
(5, 'Butters', 'https://avatars.mds.yandex.net/i?id=604056bdb64de2b0b4bb0121d0658d4e9b0ff0f9-5288530-images-thumbs&n=13', 'available', 1, 1),
(6, 'Tracy', 'https://polinka.top/uploads/posts/2023-05/thumbs/1683623999_polinka-top-p-sobachki-i-koshki-kartinki-pinterest-17.jpg', 'available', 4, 11),
(7, 'Dare', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 4, 10),
(8, 'Boothe', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 2, 5),
(9, 'Stibbons', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 4, 8),
(10, 'Owen', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 7, 4);

SELECT * FROM pets;

ALTER TABLE ONLY pets
    ADD CONSTRAINT pet_pk PRIMARY KEY (petid);

INSERT INTO pets (petid, name, photoUrls, status, category, tag) VALUES
(11, 'дружbан', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 0, NULL),
(12, 'Smith', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 0, 0),
(13, 'Smith1', 'https://wallbox.ru/wallpapers/main/201447/ba6aa224ee250e5.jpg', 'available', 1, 1),
(14, 'Rownam2', 'https://wallbox.ru/wallpapers/main/201447/ba6aa224ee250e5.jpg', ' not available', 2, 3),
(15, 'Joplette3', 'https://avatars.mds.yandex.net/i?id=6094a152cfb2496c148827ef56abf13e89f26453-5682063-images-thumbs&n=13', 'available', 0, NULL),
(16, 'Butters4', 'https://avatars.mds.yandex.net/i?id=604056bdb64de2b0b4bb0121d0658d4e9b0ff0f9-5288530-images-thumbs&n=13', 'available', 1, 1),
(17, 'Tracy5', 'https://polinka.top/uploads/posts/2023-05/thumbs/1683623999_polinka-top-p-sobachki-i-koshki-kartinki-pinterest-17.jpg', 'available', 4, 11),
(18, 'Dare4', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 4, 10),
(19, 'Boothe4', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 2, 5),
(20, 'Stibbons4', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 4, 8),
(21, 'Owen4', 'https://s1.1zoom.ru/b5050/666/Dogs_Cats_437526_3840x2400.jpg', 'available', 7, 4);


ALTER TABLE ONLY tags
    ADD CONSTRAINT tag_pk PRIMARY KEY (tagid);

ALTER TABLE ONLY categories
    ADD CONSTRAINT category_pk PRIMARY KEY (categoryid);


ALTER TABLE ONLY pets
    ADD CONSTRAINT fk_pets_category FOREIGN KEY (category) REFERENCES pets(petid) ON DELETE SET NULL;

ALTER TABLE ONLY pets
    ADD CONSTRAINT fk_pets_tags FOREIGN KEY (tag) REFERENCES pets(petid) ON DELETE SET NULL;

ANALYZE;

/* 
