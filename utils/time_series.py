import pandas
import pandas as pd
import numpy as np
class BasicTSTransformer:
    def __init__(self, ts: pandas.core.series.Series):
        self.ts = ts
    def pct_change(self) -> pandas.core.series.Series:
        transformed = self.ts.pct_change()
        transformed.fillna(0.0,inplace = True)
        return transformed
    def log_returns(self) -> pandas.core.series.Series:
        transformed: pandas.core.series.Series= np.log(self.ts/self.ts.shift(1))
        transformed.fillna(0.0,inplace = True)
        return transformed