// emit_yaml.c
#include <stdio.h>
#include "instruction2.h"

int main() {
    FILE *fp = fopen("reconstructed_instruction.yaml", "w");
    if (fp == NULL) {
        perror("Failed to open file");
        return 1;
    }

    fprintf(fp, "%s", instruction_yaml);
    fclose(fp);
    printf("YAML content written to reconstructed_instruction.yaml\n");

    return 0;
}

