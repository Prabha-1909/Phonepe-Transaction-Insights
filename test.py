repo_url="https://github.com/PhonePe/pulse.git"
destination="C:\PHONEPE\data"

from git import Repo
Repo.clone_from(repo_url, destination)