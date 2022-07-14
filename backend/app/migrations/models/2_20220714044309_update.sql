-- upgrade --
ALTER TABLE "project" ADD "url" VARCHAR(255);
ALTER TABLE "project" ADD "languages" JSONB;
ALTER TABLE "project" ADD "image_url" VARCHAR(255);
-- downgrade --
ALTER TABLE "project" DROP COLUMN "url";
ALTER TABLE "project" DROP COLUMN "languages";
ALTER TABLE "project" DROP COLUMN "image_url";
