# messy.py
import pandas as pd,numpy as np
from typing import List,Dict,Any
import matplotlib.pyplot as plt

class dataProcessor:
    def __init__(self,input_file:str,    output_file:str='processed.csv'):
        self.input=input_file
        self.output_file=output_file
        self.data=None
    
    def Load_data(self):
        """loads data from csv file"""
        self.data=pd.read_csv(self.input)
        return self.data
    
    def process(self,columns_to_process:List[str]=[],aggfunc:str='mean')->pd.DataFrame:
        if len(columns_to_process)==0: return self.data
        processed_data={}
        for col in columns_to_process:
         if col in self.data.columns:
          processed_data[col]=getattr(self.data[col],aggfunc)()
         else:
            print(f"Warning: Column {col} not found")
        return pd.DataFrame(processed_data,index=[0])

    def visualize_data(self,   column:str,   PlotType:str='bar'   )->None:
        if self.data is None:raise ValueError('No data loaded')
        plt.figure(figsize=(10,     5))
        if PlotType=='bar':
            self.data[column].value_counts().plot(kind='bar')
        elif     PlotType=='hist':
            self.data[column].hist()
        plt.title(f'Visualization of {column}')
        plt.show()

def main():
    processor=dataProcessor('data.csv')
    df = processor.Load_data()
    processed=processor.process(['age','salary'],aggfunc='mean')
    processor.visualize_data('age','hist')

if __name__=='__main__':
    main()
