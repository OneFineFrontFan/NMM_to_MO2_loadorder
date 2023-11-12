input_file_path = 'NMM_loadorder.txt'
output_file_path = 'MO2_loadorder.txt'

with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

lines = lines[2:]

modified_lines = [line.split('=')[0] + '\n' for line in lines]

with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)

print(f"Processing complete. Modified lines written to {output_file_path}")
