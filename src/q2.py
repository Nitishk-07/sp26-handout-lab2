import sys
sys.path.append(".")
import os
import pandas as pd

import kagglehub

path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")

print("Path to dataset files:", path)


class SpamReader:
    def __init__(self, filename: str = 'spam.csv') -> None:
        # Read file from the file into a Pandas dataframe
        # Raise a ValueError if file doesn't exist
        if not os.path.exists(filename):
            self.new_method(filename)

        self.df = pd.read_csv(filename)
        self.df = self.df.dropna(subset=['v1', 'v2'])

    def new_method(self, filename: str) -> None:
        raise ValueError(f"File {filename} does not exist")

    def get_first_five_rows(self) -> pd.DataFrame:
        # Return the first five rows of the dataset as a dataframe
        return self.df.head(5)

    def get_spam(self) -> pd.DataFrame:
        # Return a dataframe with all rows that are marked as spam
        return self.df[self.df['v1'] == 'spam']

    def get_ham(self) -> pd.DataFrame:
        # Return a dataframe with all rows that are not marked as spam
        # Rows that are not spam are ham
        return self.df[self.df['v1'] == 'ham']
