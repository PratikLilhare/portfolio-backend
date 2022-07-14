-- upgrade --
ALTER TABLE "project" ALTER COLUMN "languages" DROP DEFAULT;
-- downgrade --
ALTER TABLE "project" ALTER COLUMN "languages" SET;
