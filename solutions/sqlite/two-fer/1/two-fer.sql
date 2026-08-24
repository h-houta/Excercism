-- CREATE TABLE "twofer" ("input" TEXT, "response" TEXT);
-- Task: update the twofer table and set the response based on the input.
-- CREATE TABLE "twofer" ("input" TEXT, "response" TEXT); 

INSERT INTO "twofer" ("input") VALUES ('Alice'), ('Bob'), (NULL);

UPDATE "twofer"
SET "RESPONSE" = CASE
    WHEN "input" IS NULL OR "input" = '' THEN 'One for you, one for me.'
    ELSE 'One for ' || "input" || ', one for me.'
END;



SELECT "INPUT", "RESPONSE" FROM "twofer";
--   status = 'pass'
-- FROM
--   (
--     SELECT
--       input,
--       response
--     FROM
--       twofer
--   ) AS actual