# To read the data from the database or live stream

import os
import sys
from src.exception import CustomExceptions
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split


# To create class variables.
from dataclasses import dataclass

