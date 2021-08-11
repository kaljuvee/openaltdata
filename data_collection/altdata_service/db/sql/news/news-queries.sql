select distinct published, title, summary, link, provider, company, senti_score
from news n
order by published desc limit 200

-- Get news by BEST scores
select distinct n.published as date, n.title as headline, n.link, c.name as company, c.ric as ticker, s.score as signal
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id
order by s.score asc, n.published desc limit 10


-- LEGACY
INSERT INTO news (published, title, summary, link, provider, company, ticker, senti_score, senti_method)
SELECT distinct n.published, n.title, n.summary, n.link, n.provider, c.name as company, c.ric as ticker, s.score as senti_score, s.method as senti_method
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id

select distinct n.published, n.title, n.summary, n.link, n.provider, c.name as company, c.ric as ticker, s.score as senti_score, s.method as senti_method
into news
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id


-- Get news by BEST scores
select distinct n.published as date, n.title as headline, n.link, c.name as company, c.ric as ticker, s.score as signal
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id
order by s.score asc, n.published desc limit 10

-- Get news by WORST scores
select distinct n.published as date, n.title as headline, n.link, c.name as company, c.ric as ticker, s.score as signal
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id
order by s.score asc, n.published desc limit 10

-- Get SENTIMENT MAP data
select distinct n.published as date, c.ric as ticker, n.link, s.score as signal
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id
order by n.published desc limit 100

-- Get topics, RIC for a news item for topic types
select distinct n.published, n.title, c.ric, t.name, t.score as topic_score
from news_item n, entity_company c, topic t
where n.news_item_id = c.news_item_id and
n.news_item_id = t.news_item_id and
t.name in ('Law_Crime', 'Health_Medical_Pharma', 'Technology_Internet')

-- Get sentiment, RIC for a news item
select distinct n.news_item_id, n.published, n.link, n.title, n.summary, c.ric, s.score, s.method as score_method
from news_item n, entity_company c, sentiment s
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id
order by news_item_id

-- Get sentiment, RIC for a news item
select distinct n.news_item_id, n.published, n.link, n.title, n.summary, c.ric, s.score, s.method as score_method, pm.price_move
from news_item n, entity_company c, sentiment s, price_move pm
where n.news_item_id = c.news_item_id and
n.news_item_id = s.news_item_id and
n.news_item_id = pm.news_item_id
order by news_item_id