from db.sql.cleaning_data.psql_queries_cleaning import DbCleaningCompanyURLWrong

import pandas as pd


def clean_wrong_url():
    conn = DbCleaningCompanyURLWrong()
    company_table = conn.get_company_table()

    domain_similar = []

    t = 1
    number_company_to_check = len(company_table)

    for i in company_table.index:

        if t % 10 == 0:
            print('we have processed ', t, ' domains out of ' + str(number_company_to_check))
        t = t + 1

        domain = company_table.at[i, 'domain']
        main_company_id = company_table.at[i, 'main_company_id']

        similar_domains = conn.get_similar_domain_name(domain)

        if similar_domains.empty:
            continue

        filtered_domain = similar_domains[similar_domains['main_company_id'] != main_company_id]

        if filtered_domain.empty:
            continue

        domain_to_check = list(filtered_domain['domain'])

        domain_similar.append({'domain': domain,
                               'main_company_id': main_company_id,
                               'list_domain_confusing': domain_to_check})

        if t % 10 == 0:
            print('we have processed ', t, ' domains out of ' + str(number_company_to_check))
        t = t + 1

    domain_similar_df = pd.DataFrame(domain_similar)

    domain_similar_df.to_csv('domain_similar_to_check.csv', index=False)

    return domain_similar_df


if __name__ == "__main__":
    df = clean_wrong_url()
    print(df)
