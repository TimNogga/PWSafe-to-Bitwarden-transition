# PWSafe Vault Converter to CSV

This tool provides a straightforward method to convert PWSafe vault data to a CSV format that's easily importable into Bitwarden or other password management systems. The provided Python script reads a tab-delimited file exported from PWSafe and produces a CSV file.

## Prerequisites

- Python (Version 3.x recommended)

## Instructions

1. **Export your PWSafe data**: 
    - Open your PWSafe application.
    - Navigate to the export option (this might differ based on the specific version of PWSafe you're using).
    - Ensure you're exporting the data as a tab-delimited text file.

2. **Place the exported file in a known location**. For this guide, I've used `/Users/timnogga/Downloads/Pwsafedata.txt` as the path to the exported file.

3. **Run the provided script**:
    - Save the above Python script to a file, e.g., `converter.py`.
    - Run the script: 
      ```
      python converter.py
      ```

4. **Check the output**:
    - After running the script, you'll find the converted data in the path you specify. For this guide, I've used `/Users/timnogga/Downloads/Pwsafedata.csv` as the path to the converted file.
    - Review the CSV file to ensure all data is correctly formatted. Please be cautious not to expose this file, as it contains sensitive data.

5. **Import the CSV to your desired password manager**:
    - Depending on your password manager, navigate to the import option.
    - Upload the converted CSV file.

## Script Explanation

The provided script follows these steps:

1. **Read each line of the PWSafe exported file**: This file is expected to be tab-delimited, with columns typically in the order of name, username, password, URL, and notes.

2. **Transform each line**: Each line from the input file is transformed to match the desired CSV format, which includes columns like folder, favorite, type, name, notes, fields, reprompt, login_uri, login_username, login_password, and login_totp.

3. **Handle 'note' type entries**: The script identifies 'note' type entries and treats them differently, ensuring they match the desired format.

4. **Write to CSV**: The converted line is then written to a new CSV file.

By following this approach, the script ensures your PWSafe data is correctly and consistently converted to the desired CSV format.

---

