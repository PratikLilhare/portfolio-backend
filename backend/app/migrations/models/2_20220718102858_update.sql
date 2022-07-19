-- upgrade --
ALTER TABLE "skill" ADD "type" VARCHAR(8) NOT NULL  DEFAULT 'OTHER';
-- downgrade --
ALTER TABLE "skill" DROP COLUMN "type";
