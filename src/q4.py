import pandas as pd
import sys
sys.path.append(".")

"""
This question uses a dataset stored in spam.csv.
The original dataset is available at https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

Implement this class to use Pandas to read the data into a dataframe.
"""

class SpamReader:
    def __init__(self) -> None:
        # Read spam.csv into a dataframe, stored as a private attribute (two underscores)
        pass

    def get_first_five_rows(self) -> pd.DataFrame:
        # Return the first five rows of the dataset as a dataframe
        pass

    # Add three properties to this class:
    # 1: num_rows (the number of rows in the dataset)
    # 2: num_spam (the number of rows labeled as spam)
    # 3: num_ham (the number of rows labeled as ham)
    # (In the security world, messages that are not spam are ham.)

# Factor out any redundant code into a helper method.
# You can ignore the rows that do not follow the correct format.
