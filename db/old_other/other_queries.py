query1 = """
insert into tmp_webtraffic_aggregates 
select site, year, month, sum(total_visits) 
from webtraffic quarter_group by site, year, month;
"""

query2 = """
insert into tmp_company_id_traffic 
select year, month,  company_detail.company_id as company_id, total_visits 
from tmp_webtraffic_aggregates 
join company_detail on company_detail.domain = tmp_webtraffic_aggregates.site;
"""
query3 = """
insert into tmp_company_id_aggregate 
select company_id, year, month, sum(total_visits) as total_visits 
FROM altdata.tmp_company_id_traffic 
group by company_id, month, year;
"""

queryX = """
SELECT DISTINCT
    c.ticker,
    c.company_id,
    s.filing_date,
    s.quarter_group,
    s.sales_reported,
    e.datetime,
    ROUND(e.estimation),
    SUM(w.total_visits)
FROM
    daily_sales_estimation e
        LEFT JOIN
    reported_sales s ON s.company_id = e.company_id
        AND s.quarter_group = e.quarter_group
        LEFT JOIN
    company_detail d ON d.company_id = e.company_id
        LEFT JOIN
    company c ON c.company_id = e.company_id
        LEFT JOIN
    tmp_webtraffic_aggregates2 w ON w.site = d.domain
        AND (w.year + 2000) = e.year_estimation
        AND w.quart = e.quarter_estimation
WHERE
    (e.quarter_group , e.datetime) IN (SELECT 
            e.quarter_group, MAX(e.datetime)
        FROM
            daily_sales_estimation e
        WHERE
            e.company_id = '464'
                AND e.quarter_group >= '16q3'
                AND e.quarter_group <= '19q4'
        GROUP BY e.quarter_group)
        AND c.ticker = 'TRIP US'
GROUP BY c.ticker , c.company_id , s.filing_date , s.quarter_group , s.sales_reported , e.datetime , ROUND(e.estimation)
ORDER BY s.filing_date;
"""
print(queryX)