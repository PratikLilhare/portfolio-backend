-- upgrade --
ALTER TABLE "experience" ADD "title" VARCHAR(20);
-- downgrade --
ALTER TABLE "experience" DROP COLUMN "title";
