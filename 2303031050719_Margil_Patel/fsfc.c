#include <stdio.h>

int main() {
    int n, i;
    
    // User Input: Number of Processes
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    int pid[n], bt[n], wt[n], tat[n];
    float total_wt = 0, total_tat = 0;

    // User Input: Burst Times
    printf("Enter burst time for each process:\n");
    for (i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d", &bt[i]);
        pid[i] = i + 1; // Assign Process ID
    }

    // Calculate Waiting Times
    wt[0] = 0; // First process has no waiting time
    for (i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
        total_wt += wt[i];
    }

    // Calculate Turnaround Times
    for (i = 0; i < n; i++) {
        tat[i] = wt[i] + bt[i];
        total_tat += tat[i];
    }

    // Display Results in Tabular Format
    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");
    printf("------------------------------------------------------\n");
    for (i = 0; i < n; i++) {
        printf("%d\t%d\t\t%d\t\t%d\n", pid[i], bt[i], wt[i], tat[i]);
    }

    // Display Average Waiting Time & Turnaround Time
    printf("\nAverage Waiting Time: %.2f", total_wt / n);
    printf("\nAverage Turnaround Time: %.2f\n", total_tat / n);

    return 0;
}
