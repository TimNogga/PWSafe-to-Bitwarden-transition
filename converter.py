def transform_line_to_csv(line):
    # Splitting the line by tabs
    parts = line.strip().split("\t")

    # Mapping the input parts to the desired CSV format
    name = parts[0]
    username = parts[1] if len(parts) > 1 else ""
    password = parts[2] if len(parts) > 2 else ""
    uri = parts[3] if len(parts) > 3 else ""
    notes = parts[4] if len(parts) > 4 else ""

    # Assuming default values for the other columns
    folder = ""
    favorite = "0"
    _type = "login"
    fields = ""
    reprompt = "0"
    totp = ""

    # Special handling if it's a "note" type
    if len(parts) == 2 and "note" in name.lower():
        _type = "note"
        notes = username  # Notes is the second column for "note" type
        username = ""  # No username for "note" type

    # Constructing the CSV line
    csv_line = f'"{folder}","{favorite}","{_type}","{name}","{notes}","{fields}","{reprompt}","{uri}","{username}","{password}","{totp}"'
    return csv_line


input_file = "/Users/timnogga/Downloads/Pwsafedata.txt" #your txt file from pwsafe data which you can as stated in the readme
output_file = "/Users/timnogga/Downloads/Pwsafedata_converted.csv"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Writing the header to the output file
    header = 'folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp\n'
    outfile.write(header)

    for line in infile:
        csv_line = transform_line_to_csv(line)
        outfile.write(csv_line + '\n')

print(f"Passwords have been converted and saved to {output_file}.")
