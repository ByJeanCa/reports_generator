from pathlib import Path
from datetime import datetime
import random


class Report:
    def __init__(self):
        """Initialize a report with simulated data."""
        self.total_sales = random.randint(1000, 10000)
        self.products_sold = random.randint(50, 200)
        self.estimated_profits = round(self.total_sales * 0.3, 2)
        self.best_selling = random.choice(["Tomato", "cucumber", "rice", "fries", "shampoo", "beer", "Coke"])
        self.customers_served = random.randint(20, 100)

    @staticmethod
    def ensure_reports_dir_exists():
        """Create the reports directory if it does not exist and return its path."""
        reports_dir = Path("./reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        return reports_dir

    def generate_unique_filename(self):
        """Generate a unique filename for the report based on the current date and time."""
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.txt"
        return filename, now

    def format_report_content(self, timestamp):
        """Format the report content as readable text."""
        content = f"""Sales Report
Generated on: {timestamp.strftime("%Y-%m-%d %H:%M:%S")}

Summary:
- Total sales: ${self.total_sales:,.2f}
- Number of products sold: {self.products_sold}
- Estimated earnings: ${self.estimated_profits:,.2f}
- Number of customers served: {self.customers_served}
- Best selling product: {self.best_selling}
"""
        return content

    def save_report(self):
        """Save the report to a file in the reports directory."""
        reports_dir = self.ensure_reports_dir_exists()
        filename, timestamp = self.generate_unique_filename()
        content = self.format_report_content(timestamp)

        # Use Path to build the file path in a portable way
        report_path = reports_dir / filename

        with open(report_path, 'w', encoding='utf-8') as report_file:
            report_file.write(content)

        print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    report = Report()
    report.save_report()