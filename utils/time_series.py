import pandas
import pandas as pd
import numpy as np
class BasicTSTransformer:
    def __init__(self):
        pass
    def pct_change(self, ts) -> pandas.core.series.Series:
        transformed = ts.pct_change()
        transformed.fillna(0.0,inplace = True)
        return transformed
    def log_returns(self, ts) -> pandas.core.series.Series:
        transformed: pandas.core.series.Series= np.log(ts/ts.shift(1))
        transformed.fillna(0.0,inplace = True)
        return transformed
    def exponential_smoothing(self, ts:pd.core.series.Series, look_back: int) -> pandas.core.series.Series:
        if look_back <= 0 :
            raise ValueError("look_back must be a positive integer")
        a:float = 2/(look_back+1)
        transformed: pandas.core.series.Series = ts.copy()
        for i in range(len(transformed)):
            transformed[i] = a * transformed[i] + (1-a)*transformed[i-1]
        return transformed
    def direction(self, ts: pd.core.series.Series) ->pd.core.series.Series:
        rets: pd.core.series.Series = self.pct_change(ts)
        return rets > 0 
    def inverse_logistic(self, ts:pd.core.series.Series) -> pd.core.series.Series:
        if any((ts<=0) | ts>=1):
            raise ValueError("All values must be within (0,1)")
        return np.log(ts/(1-ts))

class Indicators:
    def __init__(self):
        pass
    def smoothed_rsi(self,ts: pd.core.series.Series, look_back: int):
        if look_back <1 :
            raise ValueError("look_back must be greater than 1")
        
        up_sum, dn_sum = 10**(-7) + 1,10**(-7) + 1
        for i in range(1,look_back):
            diff = ts[i] - ts[i-1]
            if diff > 0:
                up_sum += diff
            else:
                dn_sum += diff
        up_sum = up_sum/(look_back - 1)
        dn_sum = dn_sum / (look_back - 1)
        transformed = ts.copy()
        for i in range(look_back, len(ts)):
            diff = ts[i] - ts[i-1]
            if diff > 0:
                up_sum = ((look_back - 1 )* up_sum + diff )/look_back
                dn_sum = (look_back -1) * dn_sum/look_back
            else:
                dn_sum = ((look_back - 1 )* dn_sum - diff )/look_back
                up_sum = (look_back -1) * up_sum/look_back
            transformed[i] = 100 * (up_sum)/(up_sum + dn_sum)
        return transformed



        