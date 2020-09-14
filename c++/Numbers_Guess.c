#include<stdio.h>
//#include<time.h>
#include<conio.h>
#include<stdlib.h>
void drawline(void)
{
	int i;
	for(i=0;i<50;i++)
	printf("_");
}
int main()
{
	int num,counttrials=0,guess;
	drawline();
	printf("\t\t\t\tNUMBER GUESSING GAME\n");
	drawline();
	printf("Rules : \n1.Computer will generate a randomn number between 0 to 50.\n");
	printf("2.You have to guess it.\n3.There will be hints to help you.\n4.You will have 7 trials only.\n");
	drawline();
	//srand(time(NULL));
	num=rand()%50;
	while(1)
	{
		printf("Enter your guess : ");
		scanf("%d",&guess);
		printf("\t\t\t\t\t\tRemaining Trials : %d\n",6-counttrials);
		counttrials++;
		if(guess>num)
		printf("Your guess is greater than the number.\n\n");
		else if(guess<num)
		printf("Your guess is smaller than the number.\n\n");
		else if(guess==num)
		{
			printf("Congrats ! You guessed the number %d.\n",num);
			break;
		}
		if(counttrials>=7)
		{counttrials++;
		break;
	}
	}
	drawline();
	if(counttrials>7)
	{
	    printf("You failed !\nThe number was %d. \nBetter Luck Next Time.\n",num);
	}
	printf("\n\n\t\t\t\t\t\t\tCr. Vinayak kushwaha");
	getch();
	return 0;
}