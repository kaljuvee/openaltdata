CREATE TABLE maincompany (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    date timestamp with time zone
);

ALTER TABLE maincompany ADD CONSTRAINT parsing_maincompany_pkey
  PRIMARY KEY (id);


CREATE TABLE parsing_twitter (
    id bigint NOT NULL,
    tweet_id bigint,
    conversation_id bigint,
    created_at bigint,
    date timestamp without time zone,
    timezone character varying,
    place character varying,
    tweet character varying,
    hashtags character varying,
    cashtags character varying,
    user_id bigint,
    user_id_str character varying,
    username character varying,
    name character varying,
    day smallint,
    hour smallint,
    link character varying,
    retweet boolean,
    nlikes bigint,
    nreplies bigint,
    nretweets bigint,
    quote_url character varying,
    search character varying,
    near character varying,
    geo character varying,
    source character varying,
    user_rt_id character varying,
    user_rt character varying,
    retweet_id character varying,
    reply_to character varying,
    retweet_date timestamp without time zone,
    translate boolean,
    trans_src character varying,
    trans_dest character varying,
    date_update timestamp without time zone,
    company_id bigint
);


CREATE TABLE company (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    ticker character varying(50) NOT NULL,
    domain character varying(150),
    date_updated timestamp with time zone,
    twitter_url character varying(200),
    main_company_id integer,
    eod_symbol character varying(50),
    indeed_url character varying(200),
    static_indeed_url character varying(200),
    instagram_url character varying(200),
    facebook_url character varying(200),
    linkedin_url character varying(200),
    parent_company_id integer,
    is_parent_company boolean NOT NULL,
    webtraffic_hist character varying(30) NOT NULL
);

ALTER TABLE company ADD CONSTRAINT parsing_company_pkey
  PRIMARY KEY (id);
ALTER TABLE company ADD CONSTRAINT parsing_company_main_company_id_852279e5_fk_parsing_m
  FOREIGN KEY (main_company_id) REFERENCES maincompany(id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE company ADD CONSTRAINT company_parent_company_id_ecf5ca6e_fk_company_id
  FOREIGN KEY (parent_company_id) REFERENCES company(id) DEFERRABLE INITIALLY DEFERRED;

CREATE INDEX company_parent_company_id_ecf5ca6e ON public.company USING btree (parent_company_id);
CREATE INDEX parsing_company_main_company_id_852279e5 ON public.company USING btree (main_company_id);


create table announcement_calendar(
    compute_datetime timestamp,
    calendar json
);