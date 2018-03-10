# include <windows.h>
# include <conio.h>
# include <iostream>
# include <stdlib.h>
# include <stdio.h>

#define arriba 72
#define izquierda 75
#define derecha 77
#define abajo 80
#define esc 27
#define borrar system("cls")

using namespace std;

int cuerpo[200][2];
int n=1;
int tam=3;
int x=10, y=12;
int dir=3;
int xc=30,yc=15;
int punto=0;
int xcg,ycg;
int p=0;
int p1x=40,p2x=60;
int contadorete=0;

char tecla;
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

         cout<<"juego desarrollado por Miguel Rodriguez";
          gotoxy(40,12);
         cout<<"Presione cualquier tecla para continuar";


        getche();
        system("cls");









     }




    void pintar()
    {
         //lineas horizontales
         int i;

         for(i=2;i<78;i++){



                gotoxy(i,3); printf("%c",205);
                gotoxy(i,23); printf("%c",205);


                }


         //lineas verticales

             for(i=4;i<23;i++){



                gotoxy(2,i); printf("%c",186);
                gotoxy(77,i); printf("%c",186);




                           }


                gotoxy(2,3); printf("%c",201);
                gotoxy(77,23); printf("%c",188);
                gotoxy(77,3); printf("%c",187);
                gotoxy(2,23); printf("%c",200);






         }



void guardarposicion()
{
   cuerpo [n][0]  = x;
   cuerpo [n][1]  = y;
   n++;
   if(n==tam) n=1;



     }

void   pintarcuerpo()
{
     int i;
     for(i=1;i<tam;i++)
     {

           gotoxy(cuerpo[i][0],cuerpo[i][1]); printf("*");





                         }




       }


void borrarcuerpo()
{
     int i;


           gotoxy(cuerpo[n][0],cuerpo[n][1]); printf(" ");














     }


     void teclear()
     {

        if(kbhit()){


             tecla=getch();
             switch(tecla){
                 case arriba:
                      if(dir!=2)
                      {
                      dir=1;
                      }
                      break;

                  case abajo:
                       if(dir!=1)
                      {
                       dir=2;
                       }
                      break;
                  case derecha:
                       if(dir!=4)
                      {
                       dir=3;
                       }
                      break;
                  case izquierda:
                       if(dir!=3)
                      {
                       dir=4;
                       }
                      break;


                      }










                    }



                     if(dir==1)
                       {
                        y--;
                        }
                       if(dir==2)
                       {
                       y++;
                       }
                       if(dir==3)
                       {

                        x++;

                        }
                       if(dir==4)
                       {
                        x--;
                        }




          }

   void comida()
   {


        contadorete++;

        if (contadorete >=8 &&  p1x>=60)
        {
               gotoxy(p1x,1); printf(" ");
               p1x--;
               if(p1x==60)
               {
                          gotoxy(xcg,ycg); printf(" ");
                          xcg=72;
                          ycg=1;



                          }

                          contadorete=0;


                        }



        gotoxy(xc,yc); printf("%c",4);



         if(x==xcg&&y==ycg)
                {
                      punto+=80;
                      xcg=72;
                      ycg=1;

                                  }
       if(x==xc&&y==yc){

                  xc=(rand()%73)+4;
                  yc=(rand()%19)+4;
                  tam++;
                  gotoxy(xc,yc); printf("%c",4);
                  p++;

                  }

         if (p==6)
         {

               for(p1x=60;p1x<=72;p1x++)
               {
                                        gotoxy(p1x,1); printf("%c",22);

                                        }




               xcg=(rand()%73)+4;
                  ycg=(rand()%19)+4;
                  tam++;
                  gotoxy(xcg,ycg); printf("%c",5);
                  p=0;





                  }






        }


   bool gameover()
   {
        if(y==3 || y==23 || x==2 || x==77)
        {
                return true;



                }
         for(int j = tam-1;j>0;j--)
         {


             if(cuerpo[j][0]==x && cuerpo[j][1]==y)
             {
                     return true;

                                }


                 }
        return false;


        }

    void pintargameover()

    {
         borrar;
         gotoxy(31,11); printf("JUEGO TERMINADO");
         gotoxy(33,13); printf("PUNTOS %d",punto);





         }

     void puntos()
     {
          if(x==xc&&y==yc)

          {
                          punto+=20;


          }
          gotoxy(3,1);printf("puntos %d",punto);






          }



int main()

{

    presentacion();

        pintar();
         while(tecla != esc && !gameover ())
 {
        puntos();
        comida();
        borrarcuerpo();
        guardarposicion();
        pintarcuerpo();
        teclear();
        Sleep(80-tam);




             }


             pintargameover();









 system("PAUSE>null");
 return 0;



}

