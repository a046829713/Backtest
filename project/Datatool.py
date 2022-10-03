from datetime import datetime
import pytz
from pytz import timezone

class Datatool():
    @staticmethod
    def changetime(input_time:str):
        """
            將輸入的時間(UTC時區) 改成台灣時間

        Args:
            input_time (str): '2019/9/25 08:01:00'
        """

        utc = pytz.utc
        tw = timezone('Asia/Taipei')

        utctime = utc.localize(datetime.strptime(input_time, "%Y/%m/%d %H:%M:%S"))
        newtime = utctime.astimezone(tw).replace(tzinfo=None)
        return newtime