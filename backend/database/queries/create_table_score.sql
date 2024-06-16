CREATE TABLE IF NOT EXISTS score (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp INTEGER DEFAULT (strftime('%s', 'now')),
  era INTEGER,
  username1 TEXT,
  username2 TEXT,
  level_id INTEGER REFERENCES level(id),
  score INTEGER,
  country TEXT,
  platform TEXT,
  mode INTEGER
);
