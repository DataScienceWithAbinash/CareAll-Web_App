create table oldies(
    id integer primary key autoincrement,
    refno integer,
    name text not null,
    gender text not null,
    age integer not null,
    location text not null,
    mobno not null,
    cct text not null,
    ratings integer,
    reviws text
)