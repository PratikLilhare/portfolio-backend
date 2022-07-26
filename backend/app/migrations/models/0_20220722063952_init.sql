-- upgrade --
CREATE TABLE IF NOT EXISTS "experience" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "start" DATE NOT NULL,
    "end" DATE,
    "company" VARCHAR(20) NOT NULL,
    "description" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "project" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "url" VARCHAR(255),
    "image_url" VARCHAR(255),
    "languages" JSONB
);
CREATE TABLE IF NOT EXISTS "skill" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL,
    "proficiency" INT NOT NULL  DEFAULT 0,
    "type" VARCHAR(8) NOT NULL  DEFAULT 'OTHER'
);
COMMENT ON COLUMN "skill"."type" IS 'BACKEND: BACKEND\nFRONTEND: FRONTEND\nDEVOPS: DEVOPS\nOTHER: OTHER';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "experience_skill" (
    "experience_id" INT NOT NULL REFERENCES "experience" ("id") ON DELETE CASCADE,
    "skill_id" INT NOT NULL REFERENCES "skill" ("id") ON DELETE CASCADE
);
