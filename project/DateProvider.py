import pandas as pd
import Datatool


def get_data(freq: int):
    """將binance 的文字檔資料轉換,並且將其保存下來

    Args:
        freq (int): 5
    """
    # 讀取資料(UTC原始資料)
    df = pd.read_csv("project\BTCUSDT-Minute-Trade.txt")
    df["Datetime"] = df["Date"] + " " + df["Time"]
    df["Datetime"] = df['Datetime'].apply(Datatool.Datatool.changetime)

    df.set_index("Datetime", inplace=True)
    df.drop(['Date', 'Time'], axis=1, inplace=True)

    df = df.resample(rule=f'{freq}min', label="right", closed='right').agg({'Open': 'first',
                                                                     'High': 'max',
                                                                      'Low': 'min',
                                                                      'Close': 'last',
                                                                      'TotalVolume': 'sum'})

    # 處理成台灣時間之資料
    df.to_csv(f"project\BTCUSDT-{freq}Minute-Trade.txt")



if __name__ == '__main__':
    get_data(30)