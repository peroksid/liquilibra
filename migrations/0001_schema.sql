
DROP TABLE IF EXISTS liquilibra_request;
DROP TABLE IF EXISTS liquilibra_user;

CREATE TABLE liquilibra_user (
  id INTEGER PRIMARY KEY SERIAL,
  email TEXT UNIQUE NOT NULL
);

CREATE TABLE liquilibra_request (
  id INTEGER PRIMARY KEY SERIAL,
  requester_id INTEGER NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  FOREIGN KEY (requester_id) REFERENCES user (id)
);*/