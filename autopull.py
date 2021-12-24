import git
import subprocess
import os
from threading import Timer
repo = git.Repo('write here your repository folder path')
def pull():
    repo.remotes.origin.pull()
    current = repo.head.commit
    repo.remotes.origin.pull()
    Timer(1800, pull).start()
   
pull()

    
