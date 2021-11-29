import subprocess

def define_env(env):
  env.variables.git_tag_version = git_tag_version()

def git_tag_version():
  command = ["git", "describe", "--tags", "--match=v*", "--abbrev=0"]
  return subprocess.check_output(command, universal_newlines=True).strip()
