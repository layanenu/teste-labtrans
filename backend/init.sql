CREATE TABLE results (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  km DOUBLE,
  distance DOUBLE,
  highway INTEGER,
  item VARCHAR
);
CREATE TABLE videos (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  km_inicial DOUBLE,
  km_final DOUBLE
);
CREATE TABLE rodovias (
  id INTEGER PRIMARY KEY,
  highway VARCHAR,
  km_inicial DOUBLE,
  km_final DOUBLE
);
