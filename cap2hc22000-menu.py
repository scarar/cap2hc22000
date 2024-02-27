#!/usr/bin/env python3
## This will detect the .cap files inside the directery and convert ALL or a specific file and create a directery called converted_files that will 
## have the converted .hc22000 files inside. 
## Invision By:
## Scarar
import subprocess
import sys
import os
import glob

def convert_cap_to_hc22000(cap_file_path, output_dir):
    output_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(cap_file_path))[0] + ".hc22000")
    command = ["hcxpcapngtool", "-o", output_file_path, "-E", "essidlist", "-I", "identitylist", "-U", "usernamelist", cap_file_path]

    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful. Output file: {output_file_path}")
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

def convert_all_cap_files(directory, output_dir):
    cap_files = glob.glob(os.path.join(directory, '*.cap'))
    if not cap_files:
        print("No .cap files found in the directory.")
        return

    for cap_file in cap_files:
        convert_cap_to_hc22000(cap_file, output_dir)

def main():
    print("Choose an option:")
    print("1. Convert all .cap files in the current directory")
    print("2. Convert a specific .cap file")
    choice = input("Enter your choice (1/2): ")

    output_dir = "converted_files"
    os.makedirs(output_dir, exist_ok=True)

    if choice == '1':
        convert_all_cap_files(".", output_dir)
    elif choice == '2':
        cap_file = input("Enter the path to the .cap file: ")
        if os.path.exists(cap_file) and cap_file.endswith(".cap"):
            convert_cap_to_hc22000(cap_file, output_dir)
        else:
            print("Invalid file. Please make sure the file exists and has a .cap extension.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
