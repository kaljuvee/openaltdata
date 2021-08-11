# DB Parameters for connection
# this is private sensible data do not publish it
import os.path
import os


# DB parameters to access the Postgre DB
def postgre_access_google_cloud():
    if os.environ.get('ALTCAP') == 'DEV':
        host = '35.228.179.179'
        database = 'altcap-dev'
        port = '5432'
        user = 'altcap_usr'
        password = 'M@ch1neTallinn'
        return host, port, database, user, password
    else:
        host = '35.228.179.179'
        database = 'altcap-beta'
        port = '5432'
        user = 'altcap_usr'
        password = 'M@ch1neTallinn'
        return host, port, database, user, password


def postgre_access_google_cloud_altcap_api():
    if os.environ.get('ALTCAP') == 'DEV':
        host = '35.228.179.179'
        database = 'altcap_api_dev'
        port = '5432'
        user = 'altcap_usr'
        password = 'M@ch1neTallinn'
        return host, port, database, user, password
    else:
        host = '35.228.179.179'
        database = 'altcap_api'
        port = '5432'
        user = 'altcap_usr'
        password = 'M@ch1neTallinn'
        return host, port, database, user, password


def postgre_access_google_cloud_news():
    if os.environ.get('ALTCAP') == 'DEV':
        host = '35.228.179.179'
        database = 'altsignals-beta'
        port = '5432'
        user = 'altsignals'
        password = 'altdata2$2'
        return host, port, database, user, password

    else:
        host = '35.228.179.179'
        database = 'altsignals-beta'
        port = '5432'
        user = 'altsignals'
        password = 'altdata2$2'
        return host, port, database, user, password


def big_query_access():
    if os.environ.get('ALTCAP') == 'DEV':
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ROOT_DIR, 'dbutil', 'big_query_credentials.json')
        bigquery_uri = f'bigquery://fedoraltdata/altcap_big'
        # bigquery_uri = 'bigquery://'
        return path, bigquery_uri

    else:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ROOT_DIR, 'dbutil', 'big_query_credentials.json')
        bigquery_uri = f'bigquery://fedoraltdata/altcap_big'
        # bigquery_uri = 'bigquery://'
        return path, bigquery_uri
