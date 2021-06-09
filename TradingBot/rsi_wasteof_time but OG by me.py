import pandas as pd


def RSI(frame: pd.DataFrame, length=14):
    close = frame["CLOSE"].iloc[:14]

    delta = close.diff()
    delta.name = "DELTA"

    up, down = delta.copy(), delta.copy()

    up.name = "UP"
    down.name = "DOWN"

    up[up < 0] = 0
    down[down > 0] = 0

    _gains = up.sum()
    _losses = abs(down.sum())

    average_gain = _gains / 14
    average_loss = _losses / 14

    RS = average_gain / average_loss

    lis2 = [0 for i in range(14)]
    rsi_first = 100 - (100 / (1 + RS))
    lis2.append(rsi_first)

    rsi_series = pd.Series(lis2)
    rsi_series.name = "RSI_1"

    lis2 = lis2[:-1]
    lis2.append(average_gain)
    prev_avg_gain_s = pd.Series(lis2)
    prev_avg_gain_s.name = "prev_average_gain"

    lis2 = lis2[:-1]
    lis2.append(average_loss)
    prev_avg_loss_s = pd.Series(lis2)
    # prev_avg_loss_s = abs(prev_avg_loss_s)
    prev_avg_loss_s.name = "prev_average_loss"

    CLOSE = frame["CLOSE"].iloc[14:]
    delta = CLOSE.diff()

    up, down = delta.copy(), delta.copy()

    up.name = "UP"
    down.name = "DOWN"

    up[up < 0] = 0
    down[down > 0] = 0

    down = abs(down)

    prev_avg_gain_s[max(prev_avg_gain_s.index) + 1] = None
    prev_avg_loss_s[max(prev_avg_loss_s.index) + 1] = None

    prev_avg_gain_shifted = prev_avg_gain_s.copy().shift(1)
    prev_avg_loss_shifted = prev_avg_loss_s.copy().shift(1)

    avg_g = (prev_avg_gain_shifted * 13 + up) / 14
    avg_l = (prev_avg_loss_shifted * 13 + down) / 14
    #
    # avg_g.name = "AVH_G"
    # avg_l.name = "AVG_L"

    # avg_g_shifted = avg_g.copy().shift(1)
    # avg_l_shifted = avg_l.copy().shift(1)
    #
    # rsi_2 = 100 - (100 / (1 + (avg_g / avg_l)))
    # rsi_2.name = "RSI2"
    # print("s")

    haha = []
    for i in range(16, CLOSE.size):
        new_ob = dict(
            DATARSI=100 - (100 / (1 + (avg_g[i - 1] / avg_l[i - 1])))
        )
        avg_g[i] = ((avg_g[i - 1] * 13) + up[i]) / 14
        avg_l[i] = ((avg_l[i - 1] * 13) + down[i]) / 14
        haha.append(new_ob)
    lala = pd.DataFrame.from_dict(haha).squeeze()
    lala = lala.shift(15)



    #TEMP
    cls = frame["CLOSE"]
    delta = cls.diff()

    up, down = delta.copy(), delta.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    gain = up.ewm(13, min_periods=14).mean()
    loss = down.abs().ewm(13, min_periods=14).mean()

    rs = gain / loss

    RS2 = 100 - (100 / (1 + rs))
    RS2.name = "RS2"

    #-----

    lis2 = [CLOSE, prev_avg_gain_s, prev_avg_loss_s, up, down, rsi_series, prev_avg_gain_shifted, prev_avg_loss_shifted,
            avg_g, avg_l, lala, RS2, frame["TIME"]]

    df = pd.concat(lis2, axis=1, keys=[s.name for s in lis2])
    df.to_csv("test.csv")

    lis = [delta, up, down]

    return pd.concat(lis, axis=1, keys=[s.name for s in lis])
