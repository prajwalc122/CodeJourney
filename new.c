#include<stdio.h>
#include<String.h>

struct student{
	int id;
	float salary;
	String name;
	};

int main(){
	struct student s1;
	struct student s2;
	
	strcpy(s1.name,"Prajwal_c");
	s1.id=122;
	s1.salary=22.332;
	
	printf("%s",s1.name);
	printf("%d",s1.id);
	printf("%f",s1.salary);
	return 0;
	}
	
	