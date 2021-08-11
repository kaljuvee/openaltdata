ALTER TABLE entity_company
ADD COLUMN sector VARCHAR(64),
ADD COLUMN market_cap DECIMAL


ALTER TABLE news ADD COLUMN new_ticker varchar(64) DEFAULT NULL;
UPDATE news SET new_ticker = ticker;
ALTER TABLE news DROP ticker;
ALTER TABLE news RENAME new_ticker TO ticker;


ALTER TABLE entity_company
DROP COLUMN fax

UPDATE entity_company
SET column1 = value1, column2 = value2, ...
WHERE condition;

UPDATE news
SET ticker_source = 'TRIT'
WHERE ticker_source is null