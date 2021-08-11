from data_collection.altdata_service.news.util.news_sentiment import main as news_sentiment
from notifications.alters_errors.slack_error_alerts import slack_send_message_alert
from data_collection.altdata_service.news.news_download import main as news_download

import traceback
import inspect


if __name__ == "__main__":
    try:
        news_download()
        # entity_extraction()
        # sentiment_assignment()
        # this is the target script - news download to be retired

        # news_sentiment()
        # update_detail()

    except Exception as e:
        this_function_name = inspect.currentframe().f_code.co_name
        error_message = str("".join(traceback.TracebackException.from_exception(e).format()))
        text = """the {PIPELINE_NAME} pipeline is broken. \n The error is {ERROR_MESG}""".format(
            PIPELINE_NAME=str('news'), ERROR_MESG=str(error_message))
        slack_send_message_alert(message_alert=text, channel='news_pipeline')

