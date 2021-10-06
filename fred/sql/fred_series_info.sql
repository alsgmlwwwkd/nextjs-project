create table fred_series_info (
    series_id varchar(255) not null,
    realtime_start date,
    realtime_end date,
    title varchar(255),
    observation_start date,
    observation_end date,
    frequency varchar(32),
    frequency_short varchar(32),
    units varchar(255),
    units_short varchar(32),
    seasonal_adjustment varchar(255),
    seasonal_adjustment_short varchar(32),
    last_updated timestamp,
    popularity int,
    notes text,
    primary key (series_id)
);