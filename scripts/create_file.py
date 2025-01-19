import sys
RED = "\033[31m"   # Red text
GREEN = "\033[32m" # Green text
RESET = "\033[0m"  # Reset to default color

def create_file(sys_args):
    pass
    

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: create_file.py <commit_id> <commit_message> <commit_description> <git_directory> <server_name> <current_time>")
        sys.exit(1)

    # Unpack arguments
    sys_args = {
        'commit_id': sys.argv[1],
        'commit_message': sys.argv[2],
        'commit_description': sys.argv[3],
        'git_directory': sys.argv[4],
        'server_name': sys.argv[5],
        'current_time': sys.argv[6]
    }
    
    print(f"\n{RED}---------------Python File Running---------------{RESET}")
    create_file(sys_args)