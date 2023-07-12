CREATE TABLE result (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  km DOUBLE,
  distance DOUBLE,
  highway INTEGER,
  item VARCHAR,
);
CREATE TABLE video (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  km_inicial DOUBLE,
  km_final DOUBLE
);
CREATE TABLE rodovia (
  id INTEGER PRIMARY KEY,
  highway VARCHAR,
  km_inicial DOUBLE,
  km_final DOUBLE
);
