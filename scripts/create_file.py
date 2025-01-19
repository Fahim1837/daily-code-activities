import sys, os
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader, TemplateError

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
    template_data['time'] = date.strftime("%I:%M %p")
    template_data['date'] = date.strftime("%d %b")
    
def create_dir(dirname):
    try:
        # Check if the directory already exists
        if not os.path.exists(dirname):
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        
        os.chdir(dirname)
        # print(f"Current working directory is now {os.getcwd()}")

    except OSError as error:
        print(f"Error creating directory '{dirname}': {error}")

def create_md_files(data):
    file_name = f"week-{data['week_number']}.md"
    is_exist = os.path.exists(file_name)
    print(file_name)
    try:
        if not os.path.exists(file_name):
            f = open(file_name, "x")
            content = modify_templates(data, is_exist)
            f.write(content + "\n\n")
            f.close()
            print(f"{file_name} is created and written")
        
        is_exist = os.path.exists(file_name)
        with open(file_name, 'a') as f:
            content = modify_templates(data, is_exist)
            f.write(content + "\n")
            print(f"{file_name} is updated")
        
    except IOError as e:
        print(f"{RED}Something is wrong: {e}{RESET}")
        
def modify_templates(data, is_exist):
    content = ""
    
    # Setup the jinja2 environment
    env = Environment (loader= FileSystemLoader( searchpath= '../templates/') )
    try:
        if not is_exist:
            template = env.get_template('new_file_template.md')
            content = template.render(data)

        else:
            template = env.get_template('existing_file_template.md')
            content = template.render(data)
            
    except TemplateError as e:
        print(f"{RED}Error: The template was not found. {e}{RESET}")
    
    except Exception as e:
        print(f"{RED}An unexpected error occurred: {e}{RESET}")    
    
    return content
    
def create_file(sys_args):
    template_data['commit_id'] = sys_args['commit_id']
    template_data['commit_message'] = sys_args['commit_message']
    template_data['commit_description'] = sys_args['commit_description']
    template_data['current_branch'] = sys_args['current_branch'] 
    template_data['server_name'] = sys_args['server_name']
    
    calculate_week_number(datetime.now())
    adjust_weekday(datetime.now())
    print(template_data)
    create_dir(sys_args['git_directory'])
    create_md_files(template_data)
    # modify_templates(template_data)

    

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: create_file.py <commit_id> <commit_message> <commit_description> <git_directory> <server_name> <current_branch>")
        sys.exit(1)

    # Unpack arguments
    sys_args = {
        'commit_id': sys.argv[1],
        'commit_message': sys.argv[2],
        'commit_description': sys.argv[3],
        'git_directory': sys.argv[4],
        'server_name': sys.argv[5],
        'current_branch': sys.argv[6]
    }
    
    print(f"\n{GREEN}---------------Python File Running---------------{RESET}")
    create_file(sys_args)