import matplotlib.pyplot as plt
from loger_for_diag import loger
import pandas as pd


class Diagrama:
    
    def __init__(self, carts):
        self.carts = carts 

    @loger
    def diagrama(self):
        df = pd.read_csv(self.carts)
        
        value_counts = df.iloc[:, 5].value_counts()
        label = value_counts.index
        size = value_counts.values
        colors = ['gold', 'yellowgreen', 'lightcoral']

        plt.pie(size, labels=label, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()

    def __del__(self):
        print(" ")