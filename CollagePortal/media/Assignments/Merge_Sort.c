#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX 10000000

void merge(int arr[], int lower_limit,int second,int upper_limit){
    int tmp[upper_limit + 1];
    
    int i = lower_limit , j = second , l = 0;
    while(i < second && j <= (upper_limit)){
        if(arr[i] <= arr[j]){
            l++;
            tmp[l] = arr[i];
            i++; 
        }
        else{
            l++;
            tmp[l] = arr[j];
            j++;
        }
    }
    
    if(i >= second){
        while(j <= upper_limit){
            l++;
            tmp[l] = arr[j];
            j++;
        }
    }
    else{
        while(i < second){
            l++;
            tmp[l] = arr[i];
            i++;
        }
    }
    
    for(int x=1 ; x <= l; x++){
        arr[lower_limit + x - 1] = tmp[x];
    }
    
}

void merge_sort(int arr[], int lower_limit, int upper_limit){
    int size = upper_limit - lower_limit + 1;
    if(size <= 1)
        return;
    
    int mid = lower_limit + (size / 2) -1 ;
    merge_sort(arr, lower_limit, mid);
    merge_sort(arr, mid+1, upper_limit);
    merge(arr, lower_limit, mid+1, upper_limit);
}

void print(int arr[],int n){
    for(int i=0; i < n ;i++){
        printf("%d ",arr[i]);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    
    if(n < 1 || n > MAX){
        printf("Size of array must be within [1,10000]");
        exit(0);
    }
    
    for(int i=0;i < n;i++){
        scanf("%d", &arr[i]);
        
        if(arr[i] < 1 || arr[i] > MAX){
            printf("Number must be within [1,1000000]");
            exit(0);
        }
    }
    
    merge_sort(arr,0,n-1);
    print(arr,n);
    return 0;
}
