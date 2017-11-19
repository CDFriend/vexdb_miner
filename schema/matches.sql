-- Matches
-- ~~~~~~~~~
--
-- Data on all matches in the current VRC season.

CREATE TABLE data_matches (
    event_sku STRING NOT NULL,          -- SKU for the event the match happened during
    red1 STRING NOT NULL,               -- First red player in the match
    red2 STRING NOT NULL,               -- Second red player in the match
    red3 STRING,                        -- Third red player in the match (apparently that happens sometimes)
    red_sit STRING,                     -- Red player sitting out, if an alliance match
    blue1 STRING NOT NULL,              -- First blue player in the match
    blue2 STRING NOT NULL,              -- Second blue player in the match
    blue3 STRING,                       -- Third blue player in the match, if applicable
    blue_sit STRING,                    -- Blue player sitting out if an alliance match
    red_score INTEGER NOT NULL,         -- Final score for red
    blue_score INTEGER NOT NULL,        -- Final score for blue
    date_time STRING NOT NULL           -- Scheduled date/time for the match (ISO 8601)
);
