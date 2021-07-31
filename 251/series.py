import string

import pandas as pd
import numpy as np


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    d = [1, 2, 3, 4, 5]
    return pd.Series(data=d, name="Fred")


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    d = [i for i in np.arange(0, 1.001, 0.001)]
    return pd.Series(d)


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    alphabet = dict(zip(string.ascii_lowercase, range(1, 27)))
    return pd.Series(data=alphabet)


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    alphabet = dict(zip(range(101, 127), string.ascii_uppercase))
    return pd.Series(data=alphabet)
