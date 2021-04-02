#include<stdio.h>
#include<time.h>

void swap(int *a , int *b){
   int tmp=*a;
   *a=*b;
   *b=tmp;
}

void Bubble_Sort(int arr[],int n){
   for( int i=0;i<n;i++)
      for( int j=i+1;j<n;j++)
         if(arr[i]>arr[j])
            swap(&arr[i],&arr[j]);
}

void print(int arr[],int n){
    for(int i=0;i < n;i++)
        printf("%d ",arr[i]);   
}

int main(){
   int n;
   scanf("%d",&n);
   int arr[n];
   for( int i=0;i<n;i++)
      scanf("%d",&arr[i]);
   
   Bubble_Sort(arr,n);
   print(arr ,n);
   return 0;
}   
