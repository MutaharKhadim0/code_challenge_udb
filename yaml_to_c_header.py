import yaml
import json

def escape_c_string(s):
    """Escape string for use in C macros, preserving newlines."""
    if not isinstance(s, str):
        return s  # let numbers through
    lines = s.splitlines()
    escaped_lines = ['"' + line.replace('\\', '\\\\').replace('"', '\\"') + '\\n"' for line in lines]
    return " \\\n".join(escaped_lines)

def encode_value_for_c(value):
    """Convert YAML value into a valid C macro string."""
    if isinstance(value, bool):
        return str(int(value))
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, (dict, list)):
        # Convert dict/list into a JSON string, escaped for C
        json_str = json.dumps(value)
        return '"' + json_str.replace('\\', '\\\\').replace('"', '\\"') + '"'
    elif isinstance(value, str):
        return escape_c_string(value)
    else:
        return f'"{str(value)}"'  # fallback for unknown types

# Input and output
input_yaml = "mock.yaml"
output_header = "instruction.h"

# Load YAML
with open(input_yaml, 'r') as f:
    data = yaml.safe_load(f)

# Write C header
with open(output_header, 'w') as f:
    f.write("// Auto-generated from YAML\n")
    f.write("#ifndef INSTRUCTION_H\n#define INSTRUCTION_H\n\n")

    for key, value in data.items():
        macro = key.upper().replace("-", "_")
        encoded_value = encode_value_for_c(value)
        f.write(f"#define {macro} {encoded_value}\n")

    f.write("\n#endif // INSTRUCTION_H\n")

print(f"✅ C header generated: {output_header}")

