from typing import List
import pandas as pd
import numpy as np
from pydantic import BaseModel

file_path = '../presidents_election_full.csv'

class Candidate(BaseModel):
    age: int 
    name: str
    electee: bool

class Election(BaseModel):
    year: int
    candidates: List[Candidate]

    @classmethod
    def from_loc(cls, loc: pd.Series): 
        return cls(
            year=loc.get('election_year', 0),
            candidates=[
                Candidate(
                    age=loc.get('president_age', 0),
                    name=loc.get('president', 'name'),
                    electee=True
                ),
                Candidate(
                    age=loc.get('competitor_age', 0),
                    name=loc.get('competitor', 'name'),
                    electee=False
                )
            ]
        )

class ElectionEvaluator:
    def __init__(self, file_path: str) -> None:
        data = pd.read_csv(file_path)  # Import CSV 
        self.df = pd.DataFrame(data=data)
        self.__set_age_summation()
        self.__set_candidate_count()
        self.__set_average_age()
        self.__set_total_age()
        self.__set_age_indexes()
        self.elections = self.__create_elections()
    
    def __set_age_summation(self): 
        self.age_summation = int(np.sum([self.df.get('president_age').sum(), self.df.get('competitor_age').sum()]))

    def __set_candidate_count(self): 
        self.candidate_count = int(np.sum([len(self.df.get('president')), len(self.df.get('competitor'))]))

    def __set_average_age(self): 
        self.average_age = round(np.divide(self.age_summation, self.candidate_count))

    def __set_total_age(self):
        columns = ('president_age', 'competitor_age')
        self.df['total_age'] = self.df.loc[:, columns].sum(axis=1)
    
    def __set_age_indexes(self):
        self.max_age_sum_index = self.df.get('total_age').idxmax()
        self.min_age_sum_index = self.df.get('total_age').idxmin()
        self.youngest_president_index = self.df.get('president_age').idxmin()
        self.oldest_president_index = self.df.get('president_age').idxmax()
        self.youngest_competitor_index = self.df.get('competitor_age').idxmin()
        self.oldest_competitor_index = self.df.get('competitor_age').idxmax()

    def __create_elections(self) -> List[Election]:
        return [Election.from_loc(self.df.iloc[i]) for i in range(len(self.df))]

    def get_summary(self):
        summary = {
            'age_summation': self.age_summation,
            'candidate_count': self.candidate_count,
            'average_age': self.average_age,
            'max_age_sum_index': self.max_age_sum_index,
            'min_age_sum_index': self.min_age_sum_index,
            'youngest_president_index': self.youngest_president_index,
            'oldest_president_index': self.oldest_president_index,
            'youngest_competitor_index': self.youngest_competitor_index,
            'oldest_competitor_index': self.oldest_competitor_index
        }
        return summary

    def get_elections(self) -> List[Election]:
        return self.elections
    
    @staticmethod
    def get_loc_from_index(df: pd.DataFrame, index: int) -> pd.Series:
        return df.iloc[index]

    def print_election_details(self):
        print(f"Oldest Election Year: {self.get_loc_from_index(self.df, self.max_age_sum_index).get('election_year')}")
        print(f"Oldest Competitor: {self.get_loc_from_index(self.df, self.oldest_competitor_index).get('competitor')} - Age: {self.get_loc_from_index(self.df, self.oldest_competitor_index).get('competitor_age')}")
        print(f"Oldest President: {self.get_loc_from_index(self.df, self.oldest_president_index).get('president')} - Age: {self.get_loc_from_index(self.df, self.oldest_president_index).get('president_age')}")
        print(f"Youngest President: {self.get_loc_from_index(self.df, self.youngest_president_index).get('president')} - Age: {self.get_loc_from_index(self.df, self.youngest_president_index).get('president_age')}")
        print(f"Average Candidate Age: {self.average_age}")
