#include<stdio.h>

struct student{
	int age;
	int class;
	char name[12];
	};
	void main(){
	student s1;
	
	printf("Enter the name:");
	scanf("%s",&s1.name);
	
	printf("Enter your age:");
	scanf("%d",&s1.age);
	
	printf("Enter your class");
	scanf("%d",&s1.class);
	
	printf("Student deatiles is :");
	printf("The student name is ",s1.name);
	printf("The student ID is ",s1.age);
	printf("The student class is ",s1.class);
	}