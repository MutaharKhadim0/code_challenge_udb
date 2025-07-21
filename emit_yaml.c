// emit_yaml.c
#include <stdio.h>

#include "instruction.h"

int main() {
   FILE *f = fopen("instruction.yaml", "w");
    if (f == NULL) {
        perror("Error opening file");
        return 1;
    }
    fprintf(f,"---\n");
    fprintf(f,"$schema: \"%s\"\n", $SCHEMA);
    fprintf(f,"kind: \"%s\"\n", KIND);
    fprintf(f,"name: \"%s\"\n", NAME);
    fprintf(f,"long_name: \"%s\"\n", LONG_NAME);
    fprintf(f,"description: |\n%s\n", DESCRIPTION);
    fprintf(f,"defined_by: \"%s\"\n", DEFINEDBY);
    fprintf(f,"assembly: \"%s\"\n", ASSEMBLY);
    fprintf(f,"encoding: %s\n", ENCODING);
    fprintf(f,"access: %s\n", ACCESS);
    fprintf(f,"data_independent_timing: %d\n", DATA_INDEPENDENT_TIMING);
    fprintf(f,"operation: |\n%s\n", OPERATION());
    fprintf(f,"sail: |\n%s\n", SAIL());
    fprintf(f,"cert_normative_rules: %s\n", CERT_NORMATIVE_RULES);
    fprintf(f,"cert_test_procedures: %s\n", CERT_TEST_PROCEDURES);
    fprintf(f,"...\n");
    fclose(f);
    return 0;
}

