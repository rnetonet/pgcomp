-- Database: projetomate84

-- DROP DATABASE projetomate84;

CREATE DATABASE projetomate84
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Portuguese_Brazil.1252'
       LC_CTYPE = 'Portuguese_Brazil.1252'
       CONNECTION LIMIT = -1;

-- Schema: mate84

-- DROP SCHEMA mate84;

CREATE SCHEMA mate84
  AUTHORIZATION postgres;


-- Table: mate84."matriz-atributo-valor"

-- DROP TABLE mate84."matriz-atributo-valor";

CREATE TABLE mate84."matriz-atributo-valor"
(
  "ID" serial NOT NULL,
  "SALA" integer,
  "TIMESTAMP_" timestamp without time zone,
  "DATA_OBSERVACAO" date,
  "HORA" time without time zone,
  "TEMPERATURA" integer,
  "SOM" integer,
  "LUZ" integer,
  "UMIDADE" integer,
  "QUANT_PESSOAS" integer,
  CONSTRAINT "matriz-atributo-valor_pkey" PRIMARY KEY ("ID")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE mate84."matriz-atributo-valor"
  OWNER TO postgres;

UPDATE mate84."matriz-atributo-valor" 
  SET "HORA"=cast("TIMESTAMP_" as time), "DATA_OBSERVACAO"=DATE("TIMESTAMP_"), 
  "DIA_SEMANA" = EXTRACT(DOW FROM "TIMESTAMP_");