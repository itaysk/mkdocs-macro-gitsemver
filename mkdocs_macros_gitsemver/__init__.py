import subprocess

def define_env(env):
  env.variables.git_semver = git_semver()

def git_semver():
  command = ["git", "describe", "--tags", "--match=v*", "--abbrev=0"]
  return subprocess.check_output(command, universal_newlines=True).strip()
