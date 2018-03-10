#include<stdio.h>
#include<math.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>
#define PI 3.14159265

using namespace std;


void gotoxy(int x, int y)
{


         HANDLE hCon;
         COORD dwPos;

         dwPos.X = x;
         dwPos.Y = y;

         hCon = GetStdHandle(STD_OUTPUT_HANDLE);
         SetConsoleCursorPosition(hCon,dwPos);



    }


 
int main()
{
	
system ("color f0"); 
	
	
	
	int x=2, y;
	for(float i=0; i<=360; i+=5)
	{
		y = ceil(sin(i/180*PI)*20)/2;
		gotoxy(x, 12-y);printf("o");
		x++;
	}
	getch();
 
	return 0;
}
