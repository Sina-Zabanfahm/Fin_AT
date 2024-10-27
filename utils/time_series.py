import pandas
import pandas as pd
import numpy as np
class BasicTSTransformer:
    def __init__(self, ts: pandas.core.series.Series):
        self.ts = ts
    def pct_change(ts) -> pandas.core.series.Series:
        transformed = self.ts.pct_change()
        transformed.fillna(0.0,inplace = True)
        return transformed
    def log_returns(self) -> pandas.core.series.Series:
        transformed: pandas.core.series.Series= np.log(self.ts/self.ts.shift(1))
        transformed.fillna(0.0,inplace = True)
        return transformed
    def exponential_smoothing(self, look_back: int) -> pandas.core.series.Series:
        if look_back <= 0 :
            raise ValueError("look_back must be a positive integer")
        a:float = 2/(look_back+1)
        transformed: pandas.core.series.Series = self.ts.copy()
        for i in range(len(transformed)):
            transformed[i] = a * transformed[i] + (1-a)*transformed[i-1]
        return transformed