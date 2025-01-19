# Get the current Git branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Get the commit id
commit_id=$(git log -1 --format="%h")

# Get the last git commit message
commit_message=$(git log -1 --pretty=format:"%s")

#Get the commit description
commit_description=$(git log -1 --pretty=format:"%B")

# Find the directory containing the .git folder
git_directory=$(git rev-parse --show-toplevel | sed 's#.*/##')

# Get the current time
# current_time=$(LC_TIME=C date "+%A %B %d, %Y %I:%M%p %z %Y")

# Get the server name
remote_url=$(git remote get-url origin)

if [[ $remote_url == *"github.com"* ]]; then
  server_name="github"
elif [[ $remote_url == *"bitbucket.org"* ]]; then
  server_name="bitbucket"
elif [[ $remote_url == *"gitlab.com"* ]]; then
  server_name="gitlab"
elif [[ $remote_url == *"amazonaws.com"* ]]; then
  server_name="aws"
else
  server_name="Unknown or self-hosted"
fi


# Print the results
echo "Commit Number: $commit_id"
echo "Commit Message: $commit_message"
echo "Commit Description: $commit_description"
echo "Git Directory: $git_directory"
echo "Server Name: $server_name"

# Call the Python script with the collected data
cd ~/Programming/Fahim/Daily\ Code\ Activites/daily-code-activities/
echo $PWD
# workon daily-code-activities
python ./scripts/create_file.py "$commit_id" "$commit_message" "$commit_description" "$git_directory" "$server_name" "$current_branch"


echo $PWD
git add .
git commit -m "$commit_message"
git push origin main