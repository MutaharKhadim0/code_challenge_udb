YAML to C Header and Back Conversion
====================================

This project demonstrates a two-way conversion between YAML files and C header files using Python and C programs.

Tools and Flow
--------------

1. yaml_to_c_header.py
   - Converts mock.yaml into instruction.h (C header file).

2. emit_yaml.c
   - Converts instruction.h into instruction.yaml (YAML file).

3. yaml_to_c_header2.py
   - Converts instruction.yaml into instruction2.h (C header file).

4. emit_yaml2.c
   - Converts instruction2.h into reconstructed_instruction.yaml (YAML file).

Note:
-----
instruction.yaml and reconstructed_instruction.yaml are identical, confirming successful round-trip conversion.

Files Overview
--------------

- mock.yaml: Initial YAML input file.
- instruction.h: C header file generated from mock.yaml.
- instruction.yaml: YAML file generated from instruction.h.
- instruction2.h: C header file generated from instruction.yaml.
- reconstructed_instruction.yaml: YAML file generated from instruction2.h.

C Executables:
--------------

- emit_yaml: Compiled executable from emit_yaml.c
- emit_yaml2: Compiled executable from emit_yaml2.c

Compilation Commands:
---------------------

gcc emit_yaml.c -o emit_yaml
gcc emit_yaml2.c -o emit_yaml2

Execution Flow:
---------------

1. Run:
   python3 yaml_to_c_header.py
   → generates instruction.h

2. Run:
   ./emit_yaml
   → generates instruction.yaml

3. Run:
   python3 yaml_to_c_header2.py
   → generates instruction2.h

4. Run:
   ./emit_yaml2
   → generates reconstructed_instruction.yaml

Author: Mutahar Khadim
Date: 21/07/2025
