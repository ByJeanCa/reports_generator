from pathlib import Path
from datetime import datetime
import random

class Report:
    def __init__(self):
        self.total_sales = random.randint(1000, 10000)
        self.products_sold = random.randint(50, 200)
        self.estimated_profits = round(self.total_sales * 0.3, 2)          
        self.best_selling = random.choice(["Tomato", "cucumber", "rice", "fries", "shampoo", "beer", "Coke"])
        self.number_customers = random.randint(20,100)

    @staticmethod
    def ensure_reports_exists():
        reports_dir = Path("./reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        return reports_dir
    
    def generate_unique_name(self):
        #informe_2023-10-15_14-30-00.txt
        now = datetime.now()
        now = now.strftime("%Y-%m-%d_%H-%M-%S")
        name = (f"report_{now}.txt")
        return name
    

    

hola = Report(1,23, 43, 432, 4322)
print(hola.ensure_reports_exists())



            
