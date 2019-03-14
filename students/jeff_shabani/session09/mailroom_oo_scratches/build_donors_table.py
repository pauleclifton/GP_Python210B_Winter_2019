import gc
import json
import numpy as np
import pandas as pd

from collections import namedtuple
from pathlib import Path

pd.options.display.float_format = '{:0,.2f}'.format
pd.set_option('display.max.columns', 25)
desired_width = 400
pd.set_option('display.width', desired_width)

read = pd.read_excel

donors = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': [75, 125, 19],
          'Ashley Lashbrooke': [10000, 15000]}

