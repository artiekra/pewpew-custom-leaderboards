SELECT * FROM (SELECT * FROM score ORDER BY _timestamp DESC)
  WHERE username1 == :player or username2 == :player GROUP BY _level;
