-- Events
-- ~~~~~~~
--
-- Data on all events in the current VRC season.

CREATE TABLE data_events (
    sku STRING PRIMARY KEY,             -- ID code for the event (to be referenced by matches)
    name STRING NOT NULL,               -- Name of the event
    venue STRING NOT NULL,              -- Location of the event (school name normally)
    city STRING NOT NULL,               -- City the event took place in
    region STRING NOT NULL,             -- Province/state the event took place in
    country STRING NOT NULL,            -- Country the event took place in
    start_date STRING NOT NULL,         -- Date/time the event started (ISO 8601)
    end_date STRING NOT NULL            -- Date/time the event ended (ISO 8601)
);
