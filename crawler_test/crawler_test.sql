create table crawler_test (
    news_id: varchar(255) not null,
    title: varchar(255),
    publisher: varchar(32),
    created_at: date,
    summary: varchar(255),
    href: varchar(255),
    primary key (news_id)
)