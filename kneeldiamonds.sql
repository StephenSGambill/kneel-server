CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

INSERT INTO `Metal` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metal` VALUES (null, "14k Gold", 736.4);
INSERT INTO Metal VALUES (null, "24k Gold", 1258.90);
INSERT INTO Metal VALUES (null, "Platinum", 795.45);
INSERT INTO Metal VALUES (null, "Palladium,", 1241.0);
SELECT * FROM Metal;


CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,1) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

INSERT INTO `Size` VALUES (null, 0.5, 405);
INSERT INTO `Size` VALUES (null, 0.75, 782);
INSERT INTO `Size` VALUES (null, 1, 1470);
INSERT INTO `Size` VALUES (null, 1.5, 1997);
INSERT INTO `Size` VALUES (null, 2, 3638);

SELECT * FROM Size


CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(20) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

INSERT INTO `Style` VALUES (null, "Classic", 500 );
INSERT INTO `Style` VALUES (null, "Modern", 710 );
INSERT INTO `Style` VALUES (null, "Vintage", 965 );

SELECT * FROM Style;


CREATE TABLE [Order]
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`)
);

INSERT INTO `Order` VALUES (null, 1, 1, 1);
INSERT INTO `Order` VALUES (null, 2, 2, 2);
INSERT INTO `Order` VALUES (null, 3, 3, 3);

SELECT * FROM [Order];

DROP TABLE [Order];
DELETE FROM [Order] WHERE id =4;
