# yaml_to_header.py

import textwrap

# Read YAML content
with open("instruction.yaml", "r") as f:
    yaml_content = f.read()

# Escape double quotes and backslashes for C string
escaped_content = yaml_content.replace("\\", "\\\\").replace('"', '\\"')

# Split into lines and add quotes
lines = escaped_content.splitlines()
c_string_lines = ['"' + line + '\\n"' for line in lines]

# Write to header file
with open("instruction2.h", "w") as f:
    f.write("#ifndef INSTRUCTION_H\n#define INSTRUCTION_H\n\n")
    f.write("static const char *instruction_yaml =\n")
    f.write("\n".join(c_string_lines))
    f.write(";\n\n#endif // INSTRUCTION_H\n")

