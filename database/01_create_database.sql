CREATE DATABASE sistema_academico;

\c sistema_academico

CREATE SCHEMA IF NOT EXISTS "public";

CREATE TABLE "public"."user" (
    email      VARCHAR(100)    NOT NULL,
    name       VARCHAR(250)    NOT NULL,
    password   TEXT            NOT NULL,
    updated_at TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "PK_email" PRIMARY KEY ( "email" ),
    CONSTRAINT "user_email_uk" UNIQUE ("email")   
);

CREATE TABLE "public"."stundent" (
    registration_number VARCHAR(100) NOT NULL,
    name                VARCHAR(250) NOT NULL,
    document_number     VARCHAR(20) NOT NULL,
    address             VARCHAR(250) NOT NULL,

    CONSTRAINT "PK_registration_number" PRIMARY KEY ( "registration_number" ),
    CONSTRAINT "stundent_document_number_uk" UNIQUE ("document_number")   
);

CREATE TABLE "public"."discipline" (
    code            VARCHAR(100) NOT NULL,
    name            VARCHAR(250) NOT NULL,
    schedule        VARCHAR(1) NOT NULL,
    class_number    VARCHAR(100) NOT NULL,

    CONSTRAINT "PK_code" PRIMARY KEY ( "code" ),
    CONSTRAINT "discipline_name_uk" UNIQUE ("name")   
);