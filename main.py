import argparse
import sys
from utils.reader import read_csv_file
from reports import payout

REPORTS = {
    "payout": payout.generate_report
}

def main():
    parser = argparse.ArgumentParser(description="Генератор отчётов из CSV файлов")
    parser.add_argument("files", nargs="+", help="CSV файлы")
    parser.add_argument("--report", required=True, choices=REPORTS.keys(), help="Тип отчёта (payout - по зарплатам)")

    args = parser.parse_args()

    try:
        employees = []
        for file_path in args.files:
            employees.extend(read_csv_file(file_path))
        report_func = REPORTS[args.report]
        report_func(employees)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()