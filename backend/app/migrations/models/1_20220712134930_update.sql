-- upgrade --
ALTER TABLE "project" ADD "description" TEXT NOT NULL;
-- downgrade --
ALTER TABLE "project" DROP COLUMN "description";
