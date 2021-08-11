# Pipeline

* **Signal pipeline** - data_collection -> aggregation -> predictive model -> api service
* **Backtesting pipeline** - data_collection -> aggregation -> predictive model -> backtesting

# Project Structure

* **run** - contains various ad hoc scripts to manage services and runs, such as 'start_service.sh' and 'kill_service.sh'
* **frontend** - UI / front end related libraries
* **[api](https://github.com/mosaiccap/altcap/tree/master/api)** - services for API end points
  * **prediction_service** - serves results of predictive models including input scatter plot charts and our signal estimates and scores
  * **marketdata_service** - serves market data such as prices / real time stock chart
  * **news_service** - serves news and news sentiment
  * **model_service** - serves results from a model run
  * **backtesting_service** - serves results of a backtesting result
* **data_collection** - services background data collection, such as market / financial data and scrapers / parsers
  * **financial** - contains components to collect relevant market data from Bloomberg, Yfinance, Google Finance EODHistoricalData including prices and  fundamentals
  * **altdata** - collects web traffic from SimilarWeb, Twitter, Google Trends, Facebook, Instagram and News
* **model** - all key predictive modelling code, including single-factor OLS or more advanced multi-factor models if any, independent of underlying data used
  * **aggregation** - aggregation utilities to aggregate various data sources for model inputs
* **backtesting** - all backtesting modelling 
  * **zipline** - back testing using zipline engine
  * **internal** - internal back testing engine efforts
* **db** - includes database connectors and sql
  * **dbutil** - data base connectors
  * **sql** - key SQL code such as DDL scripts and re-usable queries
* **notifications** - alll code for external notification services such as email, SMS and social
* **config** - global configuration code
* **tests** - all unit and integration tests
* **devops** - all devops, pipeline orchestration and CI/CD code
  * **monitoring** - monitoring scripts and tools
  * **cicd** - CI/CD scripts and tools
* **data** - sample test data such as pickle and csv files
* **doc** - Python doclib results and other relevant documentation such as Swagger for JSON APIs
* **samples** - illustrative samples / prototyping coding and dashboard / visualisation results
* **archive** - archived code that we have not yet allocated or deleted

# News Pipeline - Example
## Build

Install dependencies:

```
export PYTHONPATH=$(pwd):$PYTHONPATH
cd ./data_collection/altdata_service/news
pip3 install -r requirements.txt

```

## Run

Run news signal data_collection pipeline:

```
cd <to project root>
python3 ./data_collection/altdata_service/news/news_pipeline.py
```
