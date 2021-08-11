create database altsignals-beta;

use altsignals-beta;

CREATE TABLE public.news (
	news_id serial NOT NULL,
	title text NULL,
	summary text NULL,
	full_text text NULL,
	published timestamptz NULL,
	link text NULL,
	contributor text NULL,
	subject text NULL,
	keyword text NULL,
	provider text NULL,
	language text NULL,
	ticker text NULL,
	senti_score numeric NULL,
	senti_method text NULL,
	company text NULL,
	sector text NULL,
	market_cap decimal NULL,
	ticker_source VARCHAR(128),
	CONSTRAINT news_pkey PRIMARY KEY (news_id)
);

CREATE SEQUENCE news_item_seq;

-- store news item and sentiment
CREATE TABLE news_item (
  news_item_id BIGINT DEFAULT NEXTVAL('news_item_seq'),
  title TEXT, -- title
  summary TEXT, -- summary
  published TIMESTAMP with time zone, -- timestamp for publication
  link TEXT, -- url
  provider VARCHAR(128), -- news item provider name
  language VARCHAR(16), -- news item provider name
  PRIMARY KEY(news_item_id)
);

CREATE SEQUENCE entity_company_id_seq;

-- company associate with news / text item
CREATE TABLE entity_company (
  entity_company_id BIGINT DEFAULT NEXTVAL('entity_company_id_seq'),
  name TEXT,-- company name
  ric VARCHAR(16), -- ric, or reuters identifier code
  news_item_id BIGINT NOT NULL,  -- foreign key back to the news
  PRIMARY KEY(entity_company_id),
  FOREIGN KEY (news_item_id) REFERENCES news_item (news_item_id) -- foreign key back to the news item
);

CREATE SEQUENCE topic_id_seq;

-- topic associate with news / text item
CREATE TABLE topic (
  topic_id BIGINT DEFAULT NEXTVAL('topic_id_seq'),
  name VARCHAR(64),-- topic name
  score DECIMAL, -- topic score
  news_item_id BIGINT NOT NULL,  -- foreign key back to the news
  PRIMARY KEY(topic_id),
  FOREIGN KEY (news_item_id) REFERENCES news_item (news_item_id) -- foreign key back to the news item
);

CREATE SEQUENCE sentiment_seq;

CREATE TABLE sentiment (
  sentiment_id BIGINT DEFAULT NEXTVAL('sentiment_seq'),
  score DECIMAL, -- sentiment score
  method VARCHAR(32), -- score method / provider
  news_item_id BIGINT NOT NULL,  -- foreign key back to the news
  PRIMARY KEY(sentiment_id),
  FOREIGN KEY (news_item_id) REFERENCES news_item (news_item_id)  -- foreign key back to the news
);

CREATE SEQUENCE price_move_seq;

-- represents price move around a news item
CREATE TABLE price_move (
  price_move_id BIGINT DEFAULT NEXTVAL('price_move_seq'),
  symbol VARCHAR(16),
  ric VARCHAR(16),
  begin_time TIMESTAMP with time zone, -- timestamp for this bar / quote
  end_time TIMESTAMP with time zone, -- timestamp for this bar / quote
  begin_price DECIMAL, -- begin price
  end_price DECIMAL, -- end price
  price_move DECIMAL, -- low price
  period VARCHAR(16), -- period of the move, pre-market, market or after-market
  frequency VARCHAR(16), -- interval or frequency of the move
  exchange VARCHAR(16), -- exchange
  source VARCHAR(16), -- source / API of price move
  news_item_id BIGINT NOT NULL,  -- foreign key back to the news
  PRIMARY KEY(price_move_id),
  FOREIGN KEY (news_item_id) REFERENCES news_item (news_item_id)  -- foreign key back to the news
);


CREATE SEQUENCE price_bar_seq;

-- represents OHLC quote
CREATE TABLE price_bar (
  price_bar_id BIGINT DEFAULT NEXTVAL('price_bar_seq'),
  ts TIMESTAMP with time zone, -- timestamp for this bar / quote
  s VARCHAR(16), -- symbol for this price
  o DECIMAL, -- open price
  h DECIMAL, -- high price
  l DECIMAL, -- low price
  c DECIMAL, -- close price
  v DECIMAL, -- volume traded for the interval
  ex VARCHAR(16), -- exchange
  source VARCHAR(16), -- source / API of quote
  PRIMARY KEY(price_bar_id)
);

CREATE SEQUENCE entity_id_seq;

-- entity associate with news / text item
CREATE TABLE entity (
  entity_id BIGINT DEFAULT NEXTVAL('entity_id_seq'),
  type VARCHAR(64), -- type of entity
  name TEXT,-- entity name
  ric VARCHAR(16), -- ric, or reuters identifier code
  news_item_id BIGINT NOT NULL,  -- foreign key back to the news
  PRIMARY KEY(entity_id),
  FOREIGN KEY (news_item_id) REFERENCES news_item (news_item_id) -- foreign key back to the news item
);