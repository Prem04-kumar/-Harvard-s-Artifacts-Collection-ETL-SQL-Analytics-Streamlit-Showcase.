-- Active: 1766751735450@@127.0.0.1@3306@harvard_artifacts
CREATE DATABASE harvard_artifacts;
USE harvard_artifacts;
CREATE TABLE IF NOT EXISTS artifact_metadata (
    id INT PRIMARY KEY,
    title TEXT,
    culture TEXT,
    period TEXT,
    century TEXT,
    medium TEXT,
    dimensions TEXT,
    description TEXT,
    department TEXT,
    classification TEXT,
    accessionyear INT,
    accessionmethod TEXT
);
CREATE TABLE IF NOT EXISTS artifact_media (
    objectid INT,
    imagecount INT,
    mediacount INT,
    colorcount INT,
    rank_value INT,
    datebegin INT,
    dateend INT,
    CONSTRAINT fk_artifact_media_object
        FOREIGN KEY (objectid) REFERENCES artifact_metadata(id)
);

CREATE TABLE IF NOT EXISTS artifact_colors (
    objectid INT,
    color VARCHAR(20),
    spectrum VARCHAR(20),
    hue VARCHAR(50),
    percent FLOAT,
    css3 VARCHAR(20),
    FOREIGN KEY (objectid) REFERENCES artifact_metadata(id)
);

SHOW TABLES;
SELECT COUNT(*) FROM artifact_metadata;
SELECT COUNT(*) FROM artifact_colors;
SELECT COUNT(*) FROM artifact_colors;
select * from artifact_metadata;
select * from artifact_colors;
select * from artifact_media;

#---sql_queries--------
#-List all artifacts from the 11th century belonging to Byzantine culture.
SELECT *
FROM artifact_metadata
WHERE century LIKE '%11%'
  AND culture = 'Byzantine';

#-What are the unique cultures represented in the artifacts?
SELECT DISTINCT culture
FROM artifact_metadata
WHERE culture IS NOT NULL;

#-List all artifacts from the Archaic Period
SELECT *
FROM artifact_metadata
WHERE period = 'Archaic Period';

#-List artifact titles ordered by accession year (descending)
SELECT title, accessionyear
FROM artifact_metadata
ORDER BY accessionyear DESC;

#-How many artifacts are there per department?
SELECT department, COUNT(*) AS artifact_count
FROM artifact_metadata
GROUP BY department;

#-Which artifacts have more than 1 image?
SELECT objectid, imagecount
FROM artifact_media
WHERE imagecount > 1;

#-What is the average rank of all artifacts?
SELECT AVG(rank_value) AS average_rank
FROM artifact_media;

#-Which artifacts have a higher colorcount than mediacount?
SELECT objectid, colorcount, mediacount
FROM artifact_media
WHERE colorcount > mediacount;

#-List all artifacts created between 1500 and 1600
SELECT *
FROM artifact_media
WHERE datebegin >= 1500
  AND dateend <= 1600;
  
#-How many artifacts have no media files?
SELECT COUNT(*) AS no_media_count
FROM artifact_media
WHERE mediacount = 0;

#-What are all the distinct hues used in the dataset?
SELECT DISTINCT hue
FROM artifact_colors
WHERE hue IS NOT NULL;

#-What are the top 5 most used colors by frequency?
SELECT color, COUNT(*) AS usage_count
FROM artifact_colors
GROUP BY color
ORDER BY usage_count DESC
LIMIT 5;

#-What is the average coverage percentage for each hue?
SELECT hue, AVG(percent) AS avg_coverage
FROM artifact_colors
GROUP BY hue;

#-List all colors used for a given artifact ID
SELECT color, hue, percent
FROM artifact_colors
WHERE objectid = 12345;

#--What is the total number of color entries in the dataset?
SELECT COUNT(*) AS total_color_entries
FROM artifact_colors;

#-List artifact titles and hues for all artifacts belonging to Byzantine culture
SELECT m.title, c.hue
FROM artifact_metadata m
JOIN artifact_colors c
ON m.id = c.objectid
WHERE m.culture = 'Byzantine';

#-List each artifact title with its associated hues
SELECT m.title, c.hue
FROM artifact_metadata m
JOIN artifact_colors c
ON m.id = c.objectid;

#-Get artifact titles, cultures, and media ranks where the period is not null
SELECT m.title, m.culture, me.rank_value
FROM artifact_metadata m
JOIN artifact_media me
ON m.id = me.objectid
WHERE m.period IS NOT NULL;

#-Find artifact titles ranked in the top 10 that include the color hue "Grey"
SELECT DISTINCT m.title, me.rank_value
FROM artifact_metadata m
JOIN artifact_media me
ON m.id = me.objectid
JOIN artifact_colors c
ON m.id = c.objectid
WHERE c.hue = 'Grey'
ORDER BY me.rank_value DESC
LIMIT 10;

#-How many artifacts exist per classification, and what is the average media count for each?
SELECT m.classification,
       COUNT(DISTINCT m.id) AS artifact_count,
       AVG(me.mediacount) AS avg_media_count
FROM artifact_metadata m
JOIN artifact_media me
ON m.id = me.objectid
GROUP BY m.classification;