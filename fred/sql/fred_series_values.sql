create table fred_series_values (
    series_id varchar(255) not null,
    date date not null,
    value float,
    primary key (series_id, date),
    constraint fk_series_id
        foreign key (series_id) references fred_series_info (series_id)
);