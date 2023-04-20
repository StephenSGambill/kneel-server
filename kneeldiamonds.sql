CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Metals` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);



INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14k Gold", 736.4);
INSERT INTO Metals VALUES (null, "24k Gold", 1258.90);
INSERT INTO Metals VALUES (null, "Platinum", 795.45);
INSERT INTO Metals VALUES (null, "Palladium,", 1241.0);
SELECT * FROM Metals;


CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,1) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);


INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);

SELECT * FROM Sizes


CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(20) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);



INSERT INTO `Styles` VALUES (null, "Classic", 500 );
INSERT INTO `Styles` VALUES (null, "Modern", 710 );
INSERT INTO `Styles` VALUES (null, "Vintage", 965 );

SELECT * FROM Styles;


CREATE TABLE Orders
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Metals_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`Metals_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`)
);

ALTER TABLE [Order] RENAME TO Orders;

INSERT INTO `Orders` VALUES (null, 1, 1, 1);
INSERT INTO `Orders` VALUES (null, 2, 2, 2);
INSERT INTO `Orders` VALUES (null, 3, 3, 3);



SELECT * FROM Orders;

DROP TABLE Orders;
DELETE FROM Orders WHERE id =4;


CREATE TABLE Items
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type` NVARCHAR(20) NOT NULL,
    `price` INTEGER NOT NULL
);

INSERT INTO `Items` VALUES (null, "Vintage", 1);
INSERT INTO `Items` VALUES (null, "Classic", 1);
INSERT INTO `Items` VALUES (null, "Modern", 1);

SELECT * FROM Items;

