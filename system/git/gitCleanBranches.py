import subprocess, sys, os, re

saveBranches = ["master", "development", "*" ] 

script_dir = os.path.dirname( __file__ )
cd_dir = os.path.join( script_dir, '..', 'change_directory')
sys.path.append( cd_dir )
from cd import cd

if len(sys.argv) <= 1:
	print("No directory given in command line arguments")
	exit(1)

dir = sys.argv[1]

cmd = "git --version"

returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

returned_output = subprocess.check_output(cmd) # returns output as a bytes tring

print('returned value:', returned_value)

print('returned output:', returned_output.decode("utf-8"))

def change_dir(dir):
	print("Changing to: " + dir)
	cd(dir)

def delete_branch(branch_name):
	if (branch_name == ""):
		return print("No branch given")
	cmd = f"git branch -D { branch_name }"
	output = subprocess.check_output(cmd, shell=True)
	print(output.decode("utf-8"))

def get_all_branches():
	output = subprocess.check_output("git branch")
	list = output.decode("utf-8").split("\n")
	return list


def main():
	change_dir(dir)

	branches = get_all_branches()

	for branch in branches:
		remove = True
		for b in saveBranches:
			if (re.search(re.escape(b), branch)):
				print("Matched!")
				remove = False
				break

		if remove == True and branch != "":
			print(branch)
			delete_branch(branch)

main()