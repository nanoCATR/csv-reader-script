from collections import defaultdict

def generate_report(data) -> None:
    departments = defaultdict(list)
    for employee in data:
        departments[employee["department"]].append(employee)

    for dept, people in departments.items():
        print(dept)
        print(f"{'':<14} {'name':<20} {'hours':<6} {'rate':<6} {'payout'}")
        total_hours = 0
        total_payout = 0
        for person in people:
            name = person["name"]
            hours = person["hours_worked"]
            rate = person["hourly_rate"]
            payout = hours * rate
            total_hours += hours
            total_payout += payout
            print(f"-------------- {name:<20} {hours:<6} {rate:<6} ${payout}")
        print(f"{'':<14} {'':<20} {total_hours:<6} {'':<6} ${total_payout:<6}\n")