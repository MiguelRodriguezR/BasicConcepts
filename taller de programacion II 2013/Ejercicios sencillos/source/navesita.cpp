# include <windows.h>
# include <iostream>
# include <conio.h>


# define izquierda 75
# define derecha 77

using namespace std;


    char A1[]={' ',' ',' ','*',' ',' ',' ',0};
    char A2[]={' ','=','=','||','=','=',' ',0};
    char A3[]={' ',' ',' ','||',' ',' ',' ',0};
    char A4[]={' ',' ','||',' ','||',' ',' ',0};
    char A5[]={' ','<','||',' ','||','>',' ',0};
    
    char EX1[]={' ',' ',' ','*',' ',' ',' ',0};
    char EX2[]={' ',' ','*','*','*',' ',' ',0};
    char EX3[]={' ',' ','*','*','*',' ',' ',0}; 
    char EX4[]={' ',' ',' ','*',' ',' ',' ',0};
    
    char BOAV[]={' ',' ',' ',' ',' ',' ',' ',0};
    
    int numvid=3,corazones=3,ix=40,iy=19,y=8,x=12,yy=12,xx=17,x1=58,y1=6,x2=70,y2=9;
    
    int i,v;
    
    int repeticion=0,nivel=1;
    
    bool condicion=false;
    
    
    void gotoxy (int x,int y)
    
    {
         
         
         HANDLE hCon;
         COORD dwPos;
         
         dwPos.X = x;
         dwPos.Y = y;
         
         hCon = GetStdHandle(STD_OUTPUT_HANDLE);
         SetConsoleCursorPosition(hCon,dwPos);
    
    
    
    }
    
    
    
    void vidas(int vi)
    {
         
         gotoxy(2,1); printf("VIDAS %d",vi);
         
         
     }  
     
     void barrasalud (int n)
     
     {
          gotoxy(72,1); printf(" ");
          gotoxy(73,1); printf(" ");
          gotoxy(74,1); printf(" ");
          gotoxy(75,1); printf(" ");
          gotoxy(76,1); printf(" ");
          
          for(v=0;v<n;v++)
          {
                          
                          gotoxy(72+v,1);
                          printf("%c",3);
                          gotoxy(76,1); printf(" "); 
                          gotoxy(77,1); printf(" ");
                          gotoxy(78,1); printf(" ");
                          gotoxy(79,1); printf(" ");   
             
                          
                          
                          
                          
          }
                      
     } 
     
     void Explocion(void)
     
     {
          
          gotoxy(ix,iy); puts(EX1);
          gotoxy(ix,iy+1); puts(EX2);
          gotoxy(ix,iy+2); puts(EX3);
          gotoxy(ix,iy+3); puts(EX4);
          
          Sleep(380);
          
           gotoxy(ix,iy); puts(A1);
          gotoxy(ix,iy+1); puts(A2);
          gotoxy(ix,iy+2); puts(A3);
          gotoxy(ix,iy+3); puts(A4);
          gotoxy(ix,iy+4); puts(A5);
          
          
          
     } 
     
     void jugar(void)
     
     {
          //**************** asteroidesss**************
          
          
           gotoxy(x,y); printf("%c",2);
           gotoxy(xx,yy); printf("%c",2);
           gotoxy(x1,y1); printf("%c",2);
           gotoxy(x2,y2); printf("%c",2);
           
           Sleep(70);
           gotoxy(x+1,y-1);   printf(" ");
           gotoxy(x,y);   printf(" ");
            gotoxy(xx+1,yy-1); printf(" ");
           gotoxy(xx,yy); printf(" ");
           gotoxy(x1+1,y1-1); printf(" ");
           gotoxy(x1,y1); printf(" ");
           gotoxy(x2+1,y2-1); printf(" ");
           gotoxy(x2,y2); printf(" ");
           
           if(y>20)
           {
                   
                  y=4;
                  x=(rand()%70)+6;
                  
           } 
            if(yy>20)
           {
                   
                  yy=4;
                  xx=(rand()%70)+6;
                   
           }        
            if(y1>20)
           {
                   
                  y1=4;
                  x1=(rand()%70)+6;
                   
           }        
            if(y2>20)
           {
                   
                  y2=4;
                  x2=(rand()%70)+6;
                   
           }    
           
           
           //*********avion***********
           
           
           if(kbhit())
           
           
           {
                 unsigned char tecla= getche();
                 switch (tecla)
                 {
                        case izquierda:
                             
                             if(ix>=4)
                             {
                               gotoxy(ix,iy); puts(BOAV);
                               gotoxy(ix,iy+1); puts(BOAV);
                               gotoxy(ix,iy+2); puts(BOAV);
                               gotoxy(ix,iy+3); puts(BOAV);
                               gotoxy(ix,iy+4); puts(BOAV);
                               
                               ix-=2;   
                               
                               gotoxy(ix,iy); puts(A1);
                               gotoxy(ix,iy+1); puts(A2);
                               gotoxy(ix,iy+2); puts(A3);
                               gotoxy(ix,iy+3); puts(A4);
                               gotoxy(ix,iy+4); puts(A5);   
                             }
                             
                           break;
                           
                           case derecha:
                                
                              if(ix<=70)
                               {
                               gotoxy(ix,iy); puts(BOAV);
                               gotoxy(ix,iy+1); puts(BOAV);
                               gotoxy(ix,iy+2); puts(BOAV);
                               gotoxy(ix,iy+3); puts(BOAV);
                               gotoxy(ix,iy+4); puts(BOAV);
                               
                               ix+=2;   
                               
                               gotoxy(ix,iy); puts(A1);
                               gotoxy(ix,iy+1); puts(A2);
                               gotoxy(ix,iy+2); puts(A3);
                               gotoxy(ix,iy+3); puts(A4);
                               gotoxy(ix,iy+4); puts(A5);   
                             }
                             
                             break;   
                        
                 } //fin switch           
                      
                      
                      
           } // fin if   
           
           //**********golpes asteroides************
           
           
           if((x>ix+1&&x<ix+5&&y==iy-1)||(xx>ix+1&&xx<ix+5&&yy==iy-1)||(x1>ix+1&&x1<ix+5&&y1==iy-1)||(x2>ix+1&&x2<ix+5&&y2==iy-1)) 
           {
                                                                                                                                   
              corazones --;
              barrasalud(corazones);
              printf("/a");                                                                                                                     
                   
                   
                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
            }    
            
                               
                               
           if(corazones==0)
           {
                           
                  numvid--;
                  vidas(numvid);
                  Explocion();
                  corazones=3;
                  barrasalud(corazones);         
                           
                           
           }                                                                                                                                                                    
           
           y++;
           yy++;
           y1++;
           y2++;
             
           
           
          
          
          
     }         
           
     
     
     int main()
     
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
         
         vidas(numvid);
         barrasalud(corazones);
         Explocion();
         while(numvid>0)
         {
                        
         jugar();
         
         }
         getche();
         
         
         
         
     }  
    
