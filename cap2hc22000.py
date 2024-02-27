#!/usr/bin/env python3

import subprocess
import sys
import os

def convert_cap_to_hc22000(cap_file_path, output_file_path=None):
    if output_file_path is None:
        base_name = os.path.splitext(cap_file_path)[0]
        output_file_path = f"{base_name}.hc22000"
    elif not output_file_path.endswith(".hc22000"):
        output_file_path += ".hc22000"

    command = ["hcxpcapngtool", "-o", output_file_path, "-E", "essidlist", "-I", "identitylist", "-U", "usernamelist", cap_file_path]

    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful. Output file: {output_file_path}")
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cap_to_hc22000.py <input .cap file> [output .hc22000 file]")
        sys.exit(1)

    cap_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else None

    convert_cap_to_hc22000(cap_file, output_file)
