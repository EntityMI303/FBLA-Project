import os

# Get folder path from user input
folder_path = input("Enter the full path to the folder: ").strip()
fileCount = 0

# Check if the path exists
if not os.path.exists(folder_path):
	print("Error: The folder does not exist.")
else:
	for file in os.listdir(folder_path):
		if file.lower().endswith(".pdf"):
			print("PDF File:", file)
			fileCount += 1
	print("Total PDF Files:", fileCount)