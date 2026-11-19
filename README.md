Weather Pipeline
A daily ETL pipeline that pulls weather data for 5 cities from the
Open-Meteo API, loads it into PostgreSQL,
and analyzes it with SQL.
Plan
Cities: New York, London, Mumbai, Tokyo, Sydney
Daily fields: max temperature, min temperature, total rain
Why: practice API extraction, table design, idempotent loads,
window-function SQL and scheduling on real, free data.
Status
In progress (started on 11/17/2026).


## Data model
`raw_daily_weather`: one row per city per day. Primary key is (city, date),
so loading the same day twice updates the row instead of duplicating it.