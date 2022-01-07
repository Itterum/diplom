#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER admin WITH PASSWORD 'admin';
    CREATE DATABASE diplom;
    GRANT ALL PRIVILEGES ON DATABASE diplom TO admin;
    ALTER USER admin CREATEDB;
EOSQL

psql -h localhost -p 5432 -U admin diplom < mylocaldb.csv
