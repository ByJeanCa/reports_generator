from pathlib import Path
from datetime import datetime
import random

class Report:
    def __init__(self):
        self.total_sales = random.randint(1000, 10000)
        self.products_sold = random.randint(50, 200)
        self.estimated_profits = round(self.total_sales * 0.3, 2)          
        self.best_selling = random.choice(["Tomato", "cucumber", "rice", "fries", "shampoo", "beer", "Coke"])
        self.customers_served = random.randint(20,100)

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
        return name, now
    
    def format_report_content(self):
        name, now = self.generate_unique_name()
        content = f""" Sales report gerated on {now}
        Summary: Total sales: ${self.total_sales}
            - Number of products sold: {self.products_sold}
            - Estimated earnings: ${self.estimated_profits}
            - Number of clients served: {self.customers_served}"""
        
        return name,content
    
    def save_report(self):
        reports_dir = self.ensure_reports_exists()
        name, content = self.format_report_content()

        reports_dir = (f"{reports_dir}/{name}")

        with open (reports_dir, 'w', encoding='utf-8') as report_file:
            report_file.write(content)

    

    

hola = Report()

hola.save_report()



            
