"""This script creates .env.sample files for all .env files found in the current directory and its subdirectories."""

import os

def process_env_file(env_file_path):
    """Process a single .env file and create corresponding .env.sample file."""
    sample_file = env_file_path + ".sample"
    
    # Get all the lines from the .env file
    with open(env_file_path, "r") as f:
        lines = f.readlines()

    # Write the lines to the .env.sample file
    with open(sample_file, "w") as f:
        for line in lines:
            if not line.startswith("#") and line.strip() != "":
                # Replace everything past the = with "ENTER_YOUR_VALUE_HERE"
                line = line.split("=", 1)[0].strip() + " = 'ENTER_YOUR_VALUE_HERE'\n"
            f.write(line)

def find_and_process_env_files(start_path):
    """Recursively find and process all .env files."""
    env_files_found = False
    
    for root, _, files in os.walk(start_path):
        for file in files:
            if file == ".env":
                env_file_path = os.path.join(root, file)
                print(f"Processing {env_file_path}")
                process_env_file(env_file_path)
                env_files_found = True
    
    if not env_files_found:
        print("No .env files found in the directory tree.")

if __name__ == "__main__":
    start_directory = os.getcwd()
    find_and_process_env_files(start_directory)