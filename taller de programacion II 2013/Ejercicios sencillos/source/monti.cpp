#include <stdio.h>
#include <windows.h>
#include <iostream>
#include <conio.h>

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


void presentacion()
{



         cout<<"\n\n\tMMMMMMMM               MMMMMMMM\n";
         cout<<"\tM:::::::M             M:::::::M\n";
         cout<<"\tM::::::::M           M::::::::M\n";
         cout<<"\tM:::::::::M         M:::::::::M\n";
         cout<<"\tM::::::::::M       M::::::::::M\n";
         cout<<"\tM:::::::::::M     M:::::::::::M\n";
         cout<<"\tM:::::::M::::M   M::::M:::::::M\n";
         cout<<"\tM::::::M M::::M M::::M M::::::M\n";
         cout<<"\tM::::::M  M::::M::::M  M::::::M\n";
         cout<<"\tM::::::M   M:::::::M   M::::::M\n";
         cout<<"\tM::::::M    M:::::M    M::::::M\n";
         cout<<"\tM::::::M     MMMMM     M::::::M\n";
         cout<<"\tM::::::M               M::::::M\n";
         cout<<"\tM::::::M               M::::::M\n";
         cout<<"\tM::::::M               M::::::M\n";
         cout<<"\tMMMMMMMM               MMMMMMMM\n";




         gotoxy(40,9);

         cout<<"programa creado por Miguel Rodriguez";
          gotoxy(40,12);
         cout<<"Presione cualquier tecla para continuar";


        getche();
        system("cls");


}


int main()
{
    int s=1;

    presentacion();

while(s==1)
{

     int valor=1,temp,x,y,M[7]={0,0,0,0,0,0,0};
  string numuni,numdec,numcen;



    x=1000000;
    y=0;





    printf("ingrese el numero (de 1 a 9999999) que quiera combertir a letras   \n\n");

    cin>>valor;




while(x>=1)
{

    temp=valor;

    if(valor>=x)
    {

        temp=(temp/x);
        valor=valor-(temp*x);
        M[y]=temp;


    }
    x=(x/10);
    y++;





}


x=0;
while(x<=6)
{
    if(M[x]==1)
    {
       numuni="uno";
       numdec="diesi";
       numcen=" ciento ";

    }
  else if(M[x]==2)
    {
       numuni="dos";
       numdec="veinti";
       numcen=" doscientos ";
    }
    else if(M[x]==3)
    {
       numuni="tres";
       numdec="treintai";
       numcen=" trescientos ";
    }
    else if(M[x]==4)
    {
       numuni="cuatro";
       numdec="cuarentai";
       numcen=" cuatrocientos ";
    }
    else if(M[x]==5)
    {
       numuni="cinco";
       numdec="cincuentai";
       numcen=" quinientos ";
    }
    else if(M[x]==6)
    {
       numuni="seis";
       numdec="sesentai";
       numcen=" seiscientos ";
    }
    else if(M[x]==7)
    {
       numuni="siete" ;
       numdec="setentai";
       numcen=" setecientos ";
    }
    else if(M[x]==8)
    {
       numuni="ocho" ;
       numdec="ochentai";
       numcen=" ochocientos ";
    }
    else if(M[x]==9)
    {
       numuni="nueve" ;
       numdec="noventai";
       numcen=" novecientos ";
    }





    if(x==0 || x==6)
    {


       if(M[x]==0)
       {
           cout<<" ";

       }

       else if(M[x]==1)
       {
           if(x==0)
           {
             cout<<"un millon ";
           }
           else if(x==6 && M[x-1]!=1) cout<<"uno";


       }

       else

       {

        if(x==0)
           {

            cout<<numuni<<" millones ";
           }

         else if(M[x-1]==1)
         {
             if(M[x]==6 || M[x]==7 || M[x]==8 || M[x]==9)
             {
                 cout<<numuni;
             }

         }

         else cout<<numuni;



       }

    }

     if(x==1 || x==4)
    {


       if(M[x]==0)
       {
           cout<<" ";

       }

       else if(M[x]==1 && M[x+1]==0 && M[x+2]==0)
       {

           cout<<"cien";

       }

       else

       {

            cout<<numcen;

       }

    }

if(x==2 || x==5)
    {


       if(M[x]==0)
       {
           cout<<" ";

       }

else if(M[x]==1)
       {
           if(M[x+1]==1 || M[x+1]==2 || M[x+1]==3 || M[x+1]==4 || M[x+1]==5)
           {
               if(M[x+1]==1)
               {
                   cout<<"once";
               }
              else if(M[x+1]==2)
               {
                   cout<<"doce";
               }
             else if(M[x+1]==3)
               {
                   cout<<"trece";
               }
              else if(M[x+1]==4)
               {
                   cout<<"catorce";
               }
             else  if(M[x+1]==5)
               {
                   cout<<"quince";
               }
           }
           else
           {
               cout<<"dies";

           }

       }
else if(M[x]==2 && M[x+1]==0)
       {
           cout<<"veinte";

       }
else if(M[x]==3 && M[x+1]==0)
       {
           cout<<"treinta";

       }
else if(M[x]==4 && M[x+1]==0)
       {
           cout<<"cuarenta";

       }
else if(M[x]==5 && M[x+1]==0)
       {
           cout<<"cincuenta";

       }
else if(M[x]==6 && M[x+1]==0)
       {
           cout<<"sesenta";

       }
else if(M[x]==7 && M[x+1]==0)
       {
           cout<<"setenta";

       }
else if(M[x]==8 && M[x+1]==0)
       {
           cout<<"ochenta";

       }
else if(M[x]==9 && M[x+1]==0)
       {
           cout<<"noventa";

       }

       else


       {

            cout<<numdec;

       }

    }


if(x==3)
    {


       if(M[x]==0)
       {
           if(M[x-1]==0 && M[x-2]==0)
           {
               cout<<" ";

           }



       }

       else if(M[x]==1)
       {
           if(M[x+1]!=0 && M[x+2]!=0 && M[x+3]!=0 && M[x-1]!=1)
          {
              cout<<"un";

          }
          else cout<<" ";

       }

       else

       {
           if(M[x-1]==1 )
           {
               if(M[x]==1 || M[x]==2 || M[x]==3 || M[x]==4 || M[x]==5  ) cout<<" ";
               else {
                cout<<numuni;

               }


           }



           else cout<<numuni;

       }

       if(x==3)
       {
           if(M[x-2]!=0)
           {
                cout<<(" mil ");

           }
         else if(M[x-1]!=0)
           {
                cout<<(" mil ");

           }
          else if(M[x]!=0)
           {
                cout<<(" mil ");

           }

       }

    }

    x++;



}


cout<<"\n\n\n";
cout<<"otro numero?  1:si  0:no";
cin>>s;
system ("cls");

}


         system("PAUSE>null");

        return 0;

}
