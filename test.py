import os
import pandas_datareader as pdr

SPY = pdr.get_data_tiingo('SPY', api_key='2280379fbc6af748da8dc346c3c46189e670e9fc')
print(SPY)

import sys
print('\n'.join(sys.path))
