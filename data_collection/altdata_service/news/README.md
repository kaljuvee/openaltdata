# Overview - News / NLP Signal Pipeline

1. **Fetch news** - read in news source via an RSS feed (Feedparser) (**news_download.py**)
2. **Extract entitities** - perform named entity recognition (NER) on the unstructured text (Open Calais) (**entity_extraction.py**)
3. **Sentiment analysis** - extract sentiment on the news item (Texblob) (**sentiment_assignment.py**)

TODO:
4. **Historical EOD prices** - fetch historical prices (Eodhistoricaldata.com) (**price_download.py**)
5. **Analyse signal** - correlate sentiment with price movement (**signal_analysis.py**)
6. **Backtesting** - back test for PnL performance (Pyfinance) (**sentiment_backtest.py**)

# Build

Install dependencies:

```
export PYTHONPATH=$(pwd):$PYTHONPATH
cd ./data_collection/altdat_service/news
pip3 install -r requirements.txt

```

# Run

Run signal pipeline:

```
cd <to project root>
python3 ./data_collection/altdata_service/news/news_pipeline.py
```

# Resources

* [Markdown Examples](https://guides.github.com/features/mastering-markdown/#examples)
