CREATE ROLE srv_landing;

CREATE schema landing AUTHORIZATION srv_landing;

ALTER ROLE srv_landing set search_path TO landing;

ALTER USER srv_landing PASSWORD 'XXX'

ALTER USER srv_landing login;


