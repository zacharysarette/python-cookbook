import sys, os
   
def cd(dir):
	# initial directory
	cwd = os.getcwd()
		
	try:
			print("Switching from --> ", os.getcwd())
			os.chdir(dir)
				
	# Caching the exception    
	except:
			print("Something wrong with specified directory. Exception --> ")
			print(sys.exc_info())
							
	# handling with finally          
	# finally:
	# 		print()
	# 		print("Restoring the path")
	# 		os.chdir(cwd)
	# 		print("Current directory is -->", os.getcwd())