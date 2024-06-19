CREATE TABLE IF NOT EXISTS score (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  _timestamp INTEGER DEFAULT (strftime('%s', 'now')),
  era INTEGER,
  username1 TEXT,
  username2 TEXT,
  _level TEXT,
  score INTEGER,
  country TEXT,
  platform TEXT,
  _mode INTEGER
);
