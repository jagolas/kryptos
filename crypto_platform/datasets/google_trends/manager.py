import pandas as pd

from pytrends.request import TrendReq
from logbook import Logger

log = Logger('GoogleTrendDataManager')

pytrends = TrendReq(hl='en-US', tz=360)


class GoogleTrendDataManager(object):

    def __init__(self, keywords):

        self.kwds = keywords
        self.trends = TrendReq(hl='en-US', tz=360)

        self.trends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')

        df = self.trends.interest_over_time()
        df.index = pd.to_datetime(df.index, unit='s')
        self.df = df

    def current_data(self, date):
        return self.df.loc[date]

    def kw_by_date(self, kwd, date):
        series = self.df.loc[date]
        val = series.get(kwd)
        return val

