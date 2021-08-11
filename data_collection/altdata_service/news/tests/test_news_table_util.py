import unittest
import sys
import io
import data_collection.altdata_service.news.util.news_table_util as news_table_util
import re
import pandas as pd
from db.dbutil.news.db_queries_news_data import psql_db_news_data_gcp


class TestNewsTableUtil(unittest.TestCase):
    def test_delete_duplicates(self):
        duplicates = [
            ('Test Title', 'Test Summary1', '2100-01-01 00:00:00', 'Test Link1', 'TEST.TICKER', 0),
            ('Test Title', 'Test Summary2', '2100-01-01 00:00:00', 'Test Link2', 'TEST.TICKER', 0),
            ('Test Title', 'Test Summary3', '2100-01-01 00:00:00', 'Test Link3', 'TEST.TICKER', 0),
            ('Test Title', 'Test Summary4', '2100-01-01 00:00:00', 'Test Link4', 'TEST.TICKER', 0)
        ]

        duplicates_df = pd.DataFrame(duplicates,
                                     columns=['title', 'summary', 'published', 'link', 'ticker', 'senti_score'])

        # Inserting test duplicates into database
        psql_db_news_data_gcp().insert_into_news_table(duplicates_df)

        # Memorize the default stdout stream
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        news_table_util.delete_duplicates()

        sys.stdout = old_stdout  # Put the old stream back in place
        what_was_printed = buffer.getvalue()  # Return a str containing the entire contents of the buffer.

        # Deleting all test data
        psql_db_news_data_gcp().delete_test_data_from_table()

        # Get the number of deleted rows
        match = re.search('Deleting (.+?) duplicate rows...', what_was_printed)

        number_of_deleted_rows = 0
        if match:
            number_of_deleted_rows = int(match.group(1))

        self.assertEqual(3, number_of_deleted_rows)


if __name__ == '__main__':
    unittest.main()
