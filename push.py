from subprocess import call
import sys

files = open("upload.txt", "r").read().split('\n')

for f in files:
  print(f)
  call(["git", "add", f])
  call(["git", "commit", "-m", "update file: " + f])
  call(["git", "push", "origin", "master"])