from pathlib import Path
from datetime import datetime

class Report:
    def __init__(self, total_sales, products_sold, estimated_profits, best_selling, number_customers):
        self.total_sales = total_sales
        self.products_sold = products_sold
        self.estimated_profits = estimated_profits
        self.best_selling = best_selling
        self.number_customers = number_customers

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



            
