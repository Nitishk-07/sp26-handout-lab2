import pandas as pd
import sys
sys.path.append(".")

"""
Please use the dataset provided in spam.csv.
The original dataset is available at https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Please ignore the rows that do not follow the correct format.

Implement this class to use Pandas to read the data into a dataframe.
There are comments, but you should replace them with proper documentation.
"""

class SpamReader:
    def __init__(self, filename: str = 'spam.csv') -> None:
        # Read file from the file into a Pandas dataframe
        # Raise a ValueError if file doesn't exist
        pass

    def get_first_five_rows(self) -> pd.DataFrame:
        # Return the first five rows of the dataset as a dataframe
        pass

    def get_spam(self) -> pd.DataFrame:
        # Return a dataframe with all rows that are marked as spam
        pass

    def get_ham(self) -> pd.DataFrame:
        # Return a dataframe with all rows that are not marked as spam
        # Rows that are not spam are ham
        pass
