-- upgrade --
CREATE TABLE IF NOT EXISTS "skill" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL,
    "proficiency" INT NOT NULL  DEFAULT 0
);
-- downgrade --
DROP TABLE IF EXISTS "skill";
