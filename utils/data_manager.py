# data_manager.py
import pandas as pd
from utils.debug import Log


class DataManager:
    @staticmethod
    def convert_to_dataframe(data: dict) -> pd.DataFrame:
        try:
            data_frame = pd.DataFrame(data['data'])
            return data_frame
        except Exception as e:
            Log.error(e)
            return None
