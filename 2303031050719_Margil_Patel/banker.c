#include <stdio.h>

#define MAX_PROCESSES 5
#define MAX_RESOURCES 3

int main() {
    int n, m, i, j, k;
    int allocation[MAX_PROCESSES][MAX_RESOURCES], max[MAX_PROCESSES][MAX_RESOURCES], need[MAX_PROCESSES][MAX_RESOURCES];
    int available[MAX_RESOURCES], finish[MAX_PROCESSES] = {0}, safeSequence[MAX_PROCESSES];
    int work[MAX_RESOURCES];

    // User Input: Number of Processes
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    // User Input: Number of Resources
    printf("Enter the number of resources: ");
    scanf("%d", &m);

    // User Input: Allocation Matrix
    printf("Enter Allocation Matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &allocation[i][j]);

    // User Input: Maximum Need Matrix
    printf("Enter Max Matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &max[i][j]);

    // User Input: Available Resources
    printf("Enter Available Resources:\n");
    for (i = 0; i < m; i++)
        scanf("%d", &available[i]);

    // Calculate Need Matrix
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            need[i][j] = max[i][j] - allocation[i][j];

    // Copy available resources to work array
    for (i = 0; i < m; i++)
        work[i] = available[i];

    // Banker's Algorithm Execution
    int count = 0;
    while (count < n) {
        int found = 0;
        for (i = 0; i < n; i++) {
            if (finish[i] == 0) { // If process is not yet finished
                int flag = 1;
                for (j = 0; j < m; j++)
                    if (need[i][j] > work[j]) { // Check if needs can be met
                        flag = 0;
                        break;
                    }

                if (flag) { // If process can execute
                    for (k = 0; k < m; k++)
                        work[k] += allocation[i][k];

                    safeSequence[count++] = i;
                    finish[i] = 1;
                    found = 1;
                }
            }
        }

        if (!found) { // If no process can be safely executed
            printf("System is in an unsafe state!\n");
            return 1;
        }
    }

    // Print Safe Sequence
    printf("System is in a safe state.\nSafe sequence is: ");
    for (i = 0; i < n; i++)
        printf("P%d ", safeSequence[i]);
    printf("\n");

    return 0;
}
