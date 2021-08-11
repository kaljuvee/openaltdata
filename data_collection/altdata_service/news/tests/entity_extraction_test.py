import data_collection.altdata_service.news.util.entity_extraction as entity_extraction

def test_get_result_diff():
    news_diff = entity_extraction.get_result_diff()
    print('diff_df', news_diff.head())

def test_get_news_update():
    entity_extraction.get_news_update()


def main():
    # test_get_result_diff()
    test_get_news_update()

if __name__ == "__main__":
    main()