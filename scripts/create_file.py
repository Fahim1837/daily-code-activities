import sys, os
from datetime import datetime, timedelta

RED = "\033[31m" 
GREEN = "\033[32m"
RESET = "\033[0m"  # Reset to default color
template_data = {}

def calculate_week_number(date):
    year_start = datetime(date.year, 1, 1)
    jan1_weekday = year_start.weekday() # What day was Jan 1
    
    days_to_first_sat = (5 - jan1_weekday + 7) % 7
    first_saturday = year_start + timedelta(days=days_to_first_sat)
    
    # First weekday of the new year
    days_since_first_sat = (date - first_saturday).days 
    
    week_number = days_since_first_sat // 7 + 1

    template_data['week_number'] = week_number
    return week_number

def adjust_weekday(date: datetime):
    day_number = date.weekday()
    
    # Make Saturday the first day of the week
    adjusted_weekday = (day_number +2) % 7
    
    # Find Saturday
    first_day = date - timedelta(days=adjusted_weekday)
    # Find Friday
    last_day = date + timedelta(days= 6 - adjusted_weekday)
    
    if (first_day.month == last_day.month):
        template_data['first_day'] = first_day.strftime("%d")
    else:
        template_data['first_day'] = first_day.strftime("%d %B")
    template_data['last_day'] = last_day.strftime("%d %B")
    template_data['year'] = date.year

def create_dir(dirname):
    pass

def create_file(sys_args):
    calculate_week_number(datetime.now())
    adjust_weekday(datetime.now())
    print(template_data)
    create_dir(sys_args[4])
    
    
    

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: create_file.py <commit_id> <commit_message> <commit_description> <git_directory> <server_name>")
        sys.exit(1)

    # Unpack arguments
    sys_args = {
        'commit_id': sys.argv[1],
        'commit_message': sys.argv[2],
        'commit_description': sys.argv[3],
        'git_directory': sys.argv[4],
        'server_name': sys.argv[5],
        # 'current_time': sys.argv[6]
    }
    
    print(f"\n{RED}---------------Python File Running---------------{RESET}")
    create_file(sys_args)