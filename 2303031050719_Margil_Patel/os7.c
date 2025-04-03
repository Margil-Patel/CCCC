#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main(){
    pid_t pid = fork();

    if(pid<0){
        printf("failed");
    }
    if(pid == 0){
        printf("Child process id: %d, parent process id: %d",getpid(),getppid());
    }
    else{
        printf("Parent id: %d, child id: %d",getpid(),pid);
    }
}