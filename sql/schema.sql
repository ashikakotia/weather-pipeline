-- One row per city per day.
CREATE TABLE IF NOT EXISTS raw_daily_weather (
    city             TEXT         NOT NULL,
    date             DATE         NOT NULL,
    temp_max_c       NUMERIC(5,2),
    temp_min_c       NUMERIC(5,2),
    precipitation_mm NUMERIC(6,2),
    loaded_at        TIMESTAMPTZ  NOT NULL DEFAULT now(),
    PRIMARY KEY (city, date)
);