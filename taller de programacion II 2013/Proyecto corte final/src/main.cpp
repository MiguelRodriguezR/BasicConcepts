////////////////////////////////////////////////////////////////
//                                                            //
//     PROGRAMA CREADO, DESARROLLADO Y DISEÑADO POR :         //
//      MIGUEL RODRIGUEZ Y ANGELA TIMARAN                     //
//                                                            //
////////////////////////////////////////////////////////////////




#include <winbgim.h>
#include <windows.h>
#include <conio.h>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>

#define esc 27

using namespace std;


fstream a_historial;
fstream a_conhistorial;
int clickmousex,clickmousey,contn=0,error=0,tecla,punpos=1,mode=0,punposx,punposy,concan=0,negan=0,temhisbin,conhistorial=1,contadorest=0,ipunto=0,operador[100],digito,contoperador=1,cifrai,contel=0;
float digitos[100],ans=0,temporal=0,ansf,cifraf,tempo1=0,tempo2=0,tempoel=0,tempoel1=0,digitosel[100],matrizest[100];
char digitartab[100];
void esperar_click();
int prim,seg,ansi;
int tempneg;

struct HISTORIAL 
{
float	h_digitos[100];
float	h_ans;
int  	h_operador[100];
float	h_digitosel[100];
int 	h_contoperador;
int     h_mode;
	
	
};

HISTORIAL historial[100];





void graficar_calculadora()
{
int g=2;
settextstyle(4,0,1);
//outtextxy(20,10,"CASPIO");
rectangle(20,30,530,200);



        
	
outtextxy(10,10,"?");	
		
		


outtextxy(470,10,"his");
outtextxy(240,10,"bin");
outtextxy(345,10,"dec");
outtextxy(125,10,"est");

if(mode==1)outtextxy(20,220,"bin");
else if (mode==0) outtextxy(20,220,"dec");
else if (mode==2) outtextxy(20,220,"est");



rectangle(460,10,530,30);
rectangle(335,10,405,30);
rectangle(220,10,300,30);
rectangle(115,10,185,30);
setcolor(COLOR(128,128,128));



if(mode!=2)
{




for(int y=250;y<=300;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

for(int y=320;y<=370;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

setcolor(WHITE);

for(int y=390;y<=440;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);

	line(350,y,411,y);
	
	
	
}



setcolor(COLOR(210,105,30));
for(int y=390;y<=440;y++)
{
	
	
	line(460,y,520,y);
	
}

setcolor(WHITE);

for(int y=460;y<=510;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

for(int y=530;y<=580;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

for(int y=600;y<=650;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

// division x/x
setbkcolor(COLOR(128,128,128));
settextstyle(5,0,1);
outtextxy(50,252,"-1");
settextstyle(5,0,4);
outtextxy(26,260,"X");

// radicacion cuadrada

line(140,275,145,290);
line(145,290,145,260);
line(145,260,180,260);
for(int y=270;y<=285;y++)
{
	line(155,y,170,y);
	
}

// radicacion electiva

line(250,275,255,290);
line(255,290,255,260);
line(255,260,290,260);
for(int y=270;y<=285;y++)
{
	line(265,y,280,y);
	
}
for(int y=260;y<=265;y++)
{
	line(245,y,252,y);
	
}

// elevacion 2

setbkcolor(COLOR(128,128,128));
settextstyle(5,0,1);
outtextxy(390,255,"2");
settextstyle(5,0,4);
outtextxy(365,260,"X");

// elevacion electiva

outtextxy(475,260,"X");
for(int y=255;y<=265;y++)
{
	line(505,y,515,y);
	
}

// LOGARITMO


outtextxy(25,325,"Log");

// logaritmo natural


outtextxy(140,325,"Ln");

// seno

outtextxy(250,325,"sin");

// coseno

outtextxy(357,325,"cos");

// tangente

outtextxy(467,325,"tan");

setcolor(BLACK);
setbkcolor(WHITE);
settextstyle(1,0,4);

// numeros

outtextxy(35,395,"7");
outtextxy(145,395,"8");
outtextxy(255,395,"9");
outtextxy(35,465,"4");
outtextxy(145,465,"5");
outtextxy(255,465,"6");
outtextxy(35,535,"1");
outtextxy(145,535,"2");
outtextxy(255,535,"3");

// signos
settextstyle(1,0,1);
setbkcolor(COLOR(210,105,30));

outtextxy(465,400,"AC");

setbkcolor(WHITE);
settextstyle(1,0,4);

outtextxy(365,465,"x");
outtextxy(485,465,"/");
outtextxy(486,465,"/");
outtextxy(487,465,"/");

outtextxy(365,535,"+");
outtextxy(480,535,"-");

outtextxy(35,605,"0");
outtextxy(155,605,".");
outtextxy(255,605,"e");
settextstyle(1,0,1);
outtextxy(360,615,"ans");
settextstyle(1,0,4);
outtextxy(480,605,"=");



}


else
{
	


setcolor(WHITE);

for(int y=390;y<=440;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);


	
	
	
}



setcolor(COLOR(210,105,30));
for(int y=390;y<=440;y++)
{
	
	
	line(460,y,520,y);
	
}

setcolor(WHITE);

for(int y=460;y<=510;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

for(int y=530;y<=580;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

for(int y=600;y<=650;y++)
{
	line(20,y,80,y);
	line(130,y,190,y);
	line(240,y,300,y);
	line(350,y,410,y);
	line(460,y,520,y);
	
	
	
	
}

setcolor(BLACK);



setbkcolor(WHITE);



// numeros

outtextxy(35,395,"7");
outtextxy(145,395,"8");
outtextxy(255,395,"9");
outtextxy(35,465,"4");
outtextxy(145,465,"5");
outtextxy(255,465,"6");
outtextxy(35,535,"1");
outtextxy(145,535,"2");
outtextxy(255,535,"3");

// signos
settextstyle(1,0,1);
setbkcolor(COLOR(210,105,30));

outtextxy(465,400,"AC");

setbkcolor(WHITE);
settextstyle(1,0,4);


outtextxy(365,465,"x");
line(365,465,390,465);
outtextxy(475,465,"x");
settextstyle(3,0,1);
outtextxy(505,465,"2");
settextstyle(1,0,4);
line(475,465,505,465);

outtextxy(365,535,"S");
settextstyle(3,0,2);
outtextxy(390,540,"x");
settextstyle(1,0,4);
outtextxy(470,535,"S");
settextstyle(3,0,2);
outtextxy(495,540,"x");
settextstyle(3,0,1);
outtextxy(503,530,"2");
settextstyle(1,0,4);

outtextxy(35,605,"0");
outtextxy(155,605,".");

settextstyle(1,0,1);
outtextxy(250,625,"add");
outtextxy(360,615,"Ds");
outtextxy(460,615,"  V");
settextstyle(1,0,4);



	
}











}



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
 	
 	
gotoxy(9,6);cout<<"////////////////////////////////////////////////////////////////";
gotoxy(9,7);cout<<"//                                                            //"; 
gotoxy(9,8);cout<<"//             UNIVERSIDAD DE NARIÑO                          //";
gotoxy(9,9);cout<<"//                                                            //";
gotoxy(9,10);cout<<"//                                                            //";
gotoxy(9,11);cout<<"//     PROGRAMA CREADO, DESARROLLADO Y DISEÑADO POR :         //";
gotoxy(9,12);cout<<"//      MIGUEL RODRIGUEZ Y ANGELA TIMARAN                     //";
gotoxy(9,13);cout<<"//                                                            //";
gotoxy(9,14);cout<<"//      Presione ESC en cualquier momento para salir          //";
gotoxy(9,15);cout<<"//                                                            //";
gotoxy(9,16);cout<<"////////////////////////////////////////////////////////////////";
 	
 	getche();
 	system("cls");
 	
 	
 }   









void CIFRA(float cifra)
{

	
	
	char cifracom[10];
	itoa(cifra,cifracom,10);
	tecla=0;
	
	if (ipunto==1)
	
	{
		
	
	 cifra=cifra/pow(10,punpos);
	 temporal=temporal/10; 
	 punpos++;
	 
     
	 }
	 
	   
		if (tempoel==1)
		{
			
				outtextxy(contn+25,30,cifracom);
				 tempoel1=tempoel1*10;  	
         	contn=contn+15;
         	clickmousex=0;  
		
         	concan++;
         	tempoel1=tempoel1+cifra;
         	
			
			
		}
	 
	 
	
	else if (ipunto==0)
	
	{
		
		if(mode==1 && cifra==2)
		{
		
		outtextxy(contn+25,40,"0");
        }
	else outtextxy(contn+25,40,cifracom);
	
      	
    }
    else
    {
    	cifrai=cifra;
    	cifraf=cifra-cifrai;
    	cifraf=cifraf*pow(10,punpos);
        itoa(cifraf,cifracom,10);	
    	outtextxy(contn+25,40,cifracom);
    }
    
    if(tempoel==0)
    {
    
    	
	
		
	
		
    
    temporal=temporal*10;  	
	contn=contn+15;
      	clickmousex=0;  
		
      	concan++;
      	temporal=temporal+cifra;
      	
      	
    
    }
	
      	
      	
      	
      	
	
	
	
}

void RESULTADO()
{
	prim=1;
	seg=2;
	int guardigitos[100];
	int auxmd;
	if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
            
            
            
            
            
            
   
            
	
	
	
	digitos[contoperador]=temporal;
		historial[conhistorial].h_contoperador=contoperador;
	for(int conm=1;conm<=contoperador;conm++)
	{
		historial[conhistorial].h_digitos[conm]=digitos[conm];
		historial[conhistorial].h_digitosel[conm]=digitosel[conm];
		historial[conhistorial].h_operador[conm]=operador[conm];
		historial[conhistorial].h_mode=mode;
	}
	
	
	if(mode==1)
	{
		
		int valor=0;
		int temp;
		int M[100];
		int varx=1000000,vary=1;
		
		for(int x=1;x<=contoperador;x++)
		{
			valor=digitos[x];
		    varx=1000000;
		    vary=1;
			
			while(varx>=1)
             {

   			 temp=valor;

   			 if(valor>=varx)
    		{

      			  temp=(temp/varx);
       			 valor=valor-(temp*varx);
      			  M[vary]=temp;
      			  
                   vary++;
                  

   			 }
   					 varx=(varx/10);
   					





			}
			int contay=0;
			temp=0;
			
			for(int y=vary-1;y>=1;y--)
			{
				if(M[y]==2)M[y]=0;
				if(M[y]==1)M[y]=2;
				
				temp=temp+pow(M[y],contay);
				if(y==vary-1 && M[y]==0)temp=0;
				contay++;
				
			
				
				
				
			}
			
			
			digitos[x]=temp;
			
			
			
			
		}
		
			
		
		
		
		
		
		
		
	}
	
	
	
	
	
	
	
	
	
	char anscomb[100];
	
	
if(operador[1]>0)
{
	
	
	
	for(int re=1;re<=contoperador;re++)
	{
		
		
			if(operador[re]==14)
		{
			
			
			
			digitos[re]=pow(digitos[re],digitosel[re+1]);
			
			
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	     
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitosel[co]=digitosel[co+1];
	   	    	
	   	     }
	   	    
	   	    
	   	    contoperador--;
			
			
	 }
		
		
		  
		if(operador[re]==13)
		{
		//	ltoa(digitos[re],anscomb,10);
        
        
    	   // outtextxy(300,158,anscomb); 
			
			digitos[re]=pow(digitos[re],2);
			
		//	ltoa(digitos[re],anscomb,10);
        
        
    	  //  outtextxy(300,138,anscomb); 
			
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
			
			
		}
		
		
		
		
		if(operador[re]==12)
		   {
		   	
		   	tempo2=1/digitos[re];
		   	int one=0;
		   	float two=0;
		   	
		   	
		   	
		   	if(digitos[re+1]<=-1)
			   {
			   	
			   	one=two=digitos[re];
		     	one=one/2;
		   	    two=two/2;
			   
			   	
			   if(one==two){
			   	
			   error=1;
		         }
			   
			   
			   }
			   
			if(digitos[re+1]<=-1 && error==0)
			{
				one=digitos[re+1];
				digitos[re+1]=digitos[re+1]*-1;
				
			}   
			   
		   	digitos[re]=pow(digitos[re+1],tempo2);
		   	
		   	if(one<=-1 && error==0)
			{
				digitos[re+1]=one;
				digitos[re]=digitos[re]*-1;
				
				
			}   
		   	
		   	//	ltoa(digitos[re],anscomb,10);
        
        
    	   // outtextxy(300,158,anscomb); 
		   	
		   	
		   	ans=digitos[re];
		   	
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }
		
			if(operador[re]==11)
		   {
		   	
		   	
		   	
		   	digitos[re]=pow(digitos[re+1],0.5);
		   	
		   	if(digitos[re+1]<=0)error=1;
		   	
		   	//	ltoa(digitos[re],anscomb,10);
        
        
    	   // outtextxy(300,158,anscomb); 
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }
		
		if(operador[re]==10)
		{
		//	ltoa(digitos[re],anscomb,10);
        
        
    	   // outtextxy(300,158,anscomb); 
			
			digitos[re]=pow(digitos[re],-1);
			
		//	ltoa(digitos[re],anscomb,10);
        
        
    	  //  outtextxy(300,138,anscomb); 
			
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
			
			
		}
	
	
		if(operador[re]==5)
		   {
		   	
		   	
		   	
		   	digitos[re]=log10(digitos[re+1]);
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	    
	   	    if(digitos[re+1]<=0)error=1;
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }
		  
		   	
		   	
		   	if(operador[re]==6)
		   	{
		   	
		   	digitos[re]=log(digitos[re+1]);
		   	
		   		   	
		   	ans=digitos[re];
		   	if(digitos[re+1]<=0)error=1;	
		   	
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }
		   if(operador[re]==7)
		   {
	   	    
		   	
		   	
		   	
		   	digitos[re]=sin(digitos[re+1]);
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }  
	   	   if(operador[re]==8)
		   {
		  
		   	
		   	
		   	
		   	digitos[re]=cos(digitos[re+1]);
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }  
		   if(operador[re]==9)
		   {
			
		   	
		   	
		   	
		   	digitos[re]=tan(digitos[re+1]);
		   	
		   	
		   	ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }  			
		
		   	
		   	
		   	
      }
	
	

	  	for(int re=1;re<=contoperador;re++)
		  {
		      
		  
		  
		if(operador[re]==3)	
    	{
    		
    		while(operador[re]==3)
    		{
    		
    		
    	
    		
    		
	   	   digitos[re]=digitos[re]*digitos[re+1];
	   	    ans=digitos[re];
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   	    
	   	    
	   	    
	   }
	   	    
	   	   }
	   	
	   	
	   	if(operador[re]==4)	
	   	
	   	{
	   		
	   		
	   		while(operador[re]==4)
    		{
    		
    		
    	
    		
    		
    		
	   	   digitos[re]=digitos[re]/digitos[re+1];
	   	    ans=digitos[re];
	   	    if (digitos[re+1]==0)error=1;
	   	    
	   	     
	   	    
	   	    for(int co=re;co<contoperador;co++)
	   	    {
	   	    	
	   	    	operador[co]=operador[co+1];
	   	    
	   	    	
	   	    	
	   	    }
	   	    
	   	     for(int co=re+1;co<contoperador;co++)
	   	    {
	   	    	
	   	    	digitos[co]=digitos[co+1];
	   	    	
	   	     }
	   	    
	   	    contoperador--;
	   		
	   		
	   	     }
	   	}
	   	
	   
		   	
		   	
		   	
		   	
		   }	
	   	
    
    
	

    for(int re=1;re<=contoperador;re++)
    {
    	
    	
    	if(operador[re]==1)
    	{
    		
    		
    		if(digitos[1]==0) digitos[1]=ans;
    		
    		
    		
    		ans=digitos[prim]+digitos[seg];
    		digitos[prim]=ans;
    		seg++;
    		
    		
    		
    		
    	}
    	
    	if(operador[re]==2)
    	{
    		
    		
    		
    		if(digitos[1]==0) digitos[1]=ans;
    		
    	
    		
    		ans=digitos[prim]-digitos[seg];
    		digitos[prim]=ans;
    		seg++;
    		
    		
    		
    		
    	}
    	
    	
    	
    	
    	
    	
    	
    	
    	
    }
    
}

else ans=digitos[1];


int ansold;



if(mode==1)
        {
        	
        	ansold=ans;
        	int ansbini;
        	float ansbinf;
        	int matbin[100],posicionbin=1;
        	int negans=0;
        	
        	if(ans<0)
        	{
        	  ans=ans*-1;
			  negans=1;	
        		
        	}
        	
        	ansbini=ansbinf=ans;
        	
        	
        	
        	while(ansbini!=1)
        	{
        		ansbinf=ansbini;
        		ansbini=ansbini/2;
        		ansbinf=ansbinf/2;
        		if(ansbinf==ansbini)matbin[posicionbin]=0;
        		else matbin[posicionbin]=1;
        		
        		posicionbin++;
        		
        	}
        	
        	int posicionbin2=posicionbin;
        	
        	matbin[posicionbin]=1;
        
        	ans=0;
        	
        	for(int x=posicionbin;x>=1;x--)
        	{
        	
        	   
        		ans=ans+(matbin[x]*pow(10,posicionbin2-1));
        	    posicionbin2--; 
            }
            
            
            if(negans==1)ans=ans*-1;
            
        }
     
    

    
        while(clickmousex>=460 && clickmousex<=520 && clickmousey>=600 && clickmousey<=650)  
		 
        {
           if(error==1)
		{
		
		ans=NULL;
		outtextxy(35,176,"ERROR");
		error=0;
		
	    }
       else
       {
       
        ltoa(ans,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=ans;
    	ansf=ans-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
         
     }
    	esperar_click();
    	
        }
        
        
        
        
        
        
        
       
        cleardevice();
      	contoperador=1;
      	historial[conhistorial].h_ans=ans;
      	
      	
      	
      	int i;
    a_historial.open("historial.dat",ios::out);
	for(i=0;i<=conhistorial;i++){
                        
      a_historial.write((char*)& historial[i],sizeof(HISTORIAL));
   
                       }
      a_historial.close(); 
      
      
      
      a_conhistorial.open("contadorh.dat",ios::out);
                   a_conhistorial<<conhistorial;
                   
                    a_conhistorial.close();
      	
      	
      	
      	
      	
      	
      	
      	
		conhistorial++;
      	temporal=0;
      	tempoel1=0;
      	concan=0;
      	contn=0;  
		
      	graficar_calculadora();
      	setbkcolor(BLACK);
	    setcolor(WHITE);
      	ipunto=0;
      	clickmousex=0;
      	rectangle(20,30,530,200);
		
     	
	
	clickmousex=0;  
	
	
	

	
	
	
	
	
	
	
	
}


void recibir_comandos()
{
	setbkcolor(BLACK);
	setcolor(WHITE);
	settextstyle(1,0,1);
	
	
	if(clickmousey>=10 && clickmousey<=30)
	
	{
		
		if(clickmousex>=10 && clickmousex<=20)
		{
			
			system("Manualcalculadora.pdf");
			clickmousex=0;
			
		}

	
		if(clickmousex>=460 && clickmousex<=520)
		{
			
			 
			cleardevice();
			int yepru=80;
			int xepru=10;
			
			settextstyle(1,0,2);
			outtextxy(30,20,"HISTORIAL DE OPERACIONES");
			settextstyle(1,0,1);
			char anscomb[100];
			int entero;
			float flotante;
			
			for(int ko=0;ko<conhistorial;ko++)
			{
				xepru=10;
				
				for(int kp=1;kp<=historial[ko].h_contoperador;kp++)
				{
					
					
					
					if(historial[ko].h_operador[kp]==11 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"sqrt");
			           xepru=xepru+60;
						
						
					}
					
					if(historial[ko].h_operador[kp]==5 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"log");
			           xepru=xepru+45;
						
						
					}
					
					if(historial[ko].h_operador[kp]==6 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"ln");
			           xepru=xepru+30;
						
						
					}
					
						if(historial[ko].h_operador[kp]==7 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"sin");
			           xepru=xepru+45;
						
						
					}
					
						if(historial[ko].h_operador[kp]==8 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"cos");
			           xepru=xepru+45;
						
						
					}
					
						if(historial[ko].h_operador[kp]==9 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"tan");
			           xepru=xepru+45;
						
						
					}
					
					
					
					if(historial[ko].h_operador[kp-1]!=13 && historial[ko].h_operador[kp]!=11 && historial[ko].h_operador[kp]!=5 && historial[ko].h_operador[kp]!=6 && historial[ko].h_operador[kp-1]!=10 && historial[ko].h_operador[kp-1]!=14 && historial[ko].h_operador[kp]!=7 && historial[ko].h_operador[kp]!=8 && historial[ko].h_operador[kp]!=9)
					{
				
					 
					if(historial[ko].h_digitos[kp]<0)
					{
						tempneg=historial[ko].h_digitos[kp];
						historial[ko].h_digitos[kp]=historial[ko].h_digitos[kp]*-1;
						outtextxy(xepru,yepru,"-");
						xepru=xepru+15;
						
					}
				     
				     
				     	if(historial[ko].h_mode==1)
				{
				
					int ansc=historial[ko].h_digitos[kp];
					int xmaxy=10000000,ymini,tempanc;
					
					
					
					while(xmaxy>=1)
{

    					tempanc=ansc;

    				if(ansc>=xmaxy)
   					 {

      					  tempanc=(tempanc/xmaxy);
      				
     			          if(tempanc==2)historial[ko].h_digitos[kp]=historial[ko].h_digitos[kp]-(2*xmaxy);
       					  ansc=ansc-(xmaxy*tempanc);
							tempanc=ansc; 	


   						 }
   						 xmaxy=(xmaxy/10);
   						





}
					
					
				}
				     
				     
				     
					entero=historial[ko].h_digitos[kp];
					
					
					
					
					ltoa(entero,anscomb,10);
			     	outtextxy(xepru,yepru,anscomb);
			     	
			     	
			     	
			     	
			     	
			     	
			     	
			     	
			     	if(historial[ko].h_digitos[kp]>=10000 && historial[ko].h_digitos[kp]<=99999)xepru=xepru+75;
			        if(historial[ko].h_digitos[kp]>=1000 && historial[ko].h_digitos[kp]<=9999)xepru=xepru+60;
			        if(historial[ko].h_digitos[kp]>=100 && historial[ko].h_digitos[kp]<=999)xepru=xepru+45;
			     	if(historial[ko].h_digitos[kp]>=10 && historial[ko].h_digitos[kp]<=99)xepru=xepru+30;
			     	if(historial[ko].h_digitos[kp]>=0 && historial[ko].h_digitos[kp]<=9)xepru=xepru+15;
			     	
			     	
			     	
			     	if(historial[ko].h_digitos[kp]-entero!=0)
			     	{
			     		flotante=historial[ko].h_digitos[kp]-entero;
			     		flotante=flotante*1000;
			     		entero=flotante;
			     			ltoa(entero,anscomb,10);
			     			outtextxy(xepru,yepru,".");
			     	        xepru=xepru+15;
			     	       outtextxy(xepru,yepru,anscomb);
			     	       xepru=xepru+45;
			     		
			     	}
			     	
			     	
			     	if (tempneg>0)historial[ko].h_digitos[kp]=tempneg;
			     	
			     	
			        }
			     	
			     	
					if(historial[ko].h_operador[kp]==12 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"*sqrt");
			           xepru=xepru+75;
						
						
					}
					
						if(historial[ko].h_operador[kp]==1 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"+");
			           xepru=xepru+15;
						
						
					}
					
					if(historial[ko].h_operador[kp]==13 && kp!=historial[ko].h_contoperador)
					{
						
						
			           outtextxy(xepru,yepru-10,"2");
			           
			           xepru=xepru+15;
			           
			          
			           
			           
						
						
					}
					
					if(historial[ko].h_operador[kp]==14 && kp!=historial[ko].h_contoperador)
					{
						
						
						
						
						
						
						
						ltoa(historial[ko].h_digitosel[kp+1],anscomb,10);
			           outtextxy(xepru,yepru-10,anscomb);
			           if(historial[ko].h_digitosel[kp+1]>=10000 && historial[ko].h_digitosel[kp+1]<=99999)xepru=xepru+75;
			           if(historial[ko].h_digitosel[kp+1]>=1000 && historial[ko].h_digitosel[kp+1]<=9999)xepru=xepru+60;
			           if(historial[ko].h_digitosel[kp+1]>=100 && historial[ko].h_digitosel[kp+1]<=999)xepru=xepru+45;
			     	   if(historial[ko].h_digitosel[kp+1]>=10 && historial[ko].h_digitosel[kp+1]<=99)xepru=xepru+30;
			        	if(historial[ko].h_digitosel[kp+1]>=0 && historial[ko].h_digitosel[kp+1]<=9)xepru=xepru+15;
			           
			           
			          
			           
			          
			           
			           
						
						
					}
					
					if(historial[ko].h_operador[kp]==10 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru-10,"-1");
			           xepru=xepru+30;
			           
			          
			           
			           
						
						
					}
					
					
					if(historial[ko].h_operador[kp]==3 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"x");
			           xepru=xepru+15;
						
						
					}
					if(historial[ko].h_operador[kp]==4 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"/");
			           xepru=xepru+15;
						
						
					}
					
					if(historial[ko].h_operador[kp]==2 && kp!=historial[ko].h_contoperador)
					{
			           outtextxy(xepru,yepru,"-");
			           xepru=xepru+15;
						
						
					}
				
			     	
			    	
					
					
					
				}
				
				if(historial[ko].h_ans==NULL)
				{
					
					outtextxy(xepru,yepru,"=");
					xepru=xepru+15;
					outtextxy(xepru,yepru,"ERROR");
					
					
					
				}
				
				else
				{
				
				
				outtextxy(xepru,yepru,"=");
				xepru=xepru+15;
				
				
				
			
				
				
				ltoa(historial[ko].h_ans,anscomb,10);
				
				
				
				outtextxy(xepru,yepru,anscomb);
				entero=historial[ko].h_ans;
				if(historial[ko].h_ans<0)
				{
				outtextxy(xepru,yepru,"-");
				historial[ko].h_ans=historial[ko].h_ans*(-1);	
					
				}
				    if(historial[ko].h_ans>=100000 && historial[ko].h_ans<=999999)xepru=xepru+90;
				    if(historial[ko].h_ans>=10000 && historial[ko].h_ans<=99999)xepru=xepru+75;
			        if(historial[ko].h_ans>=1000 && historial[ko].h_ans<=9999)xepru=xepru+60;
			        if(historial[ko].h_ans>=100 && historial[ko].h_ans<=999)xepru=xepru+45;
			     	if(historial[ko].h_ans>=10 && historial[ko].h_ans<=99)xepru=xepru+30;
			     	if(historial[ko].h_ans>=0 && historial[ko].h_ans<=9)xepru=xepru+15;
			     	
			     if(entero<0)historial[ko].h_ans=historial[ko].h_ans*(-1);	
				
				if(historial[ko].h_ans-entero!=0)
			     	{
			     		flotante=historial[ko].h_ans-entero;
			     		flotante=flotante*1000;
			     		entero=flotante;
			     		if(entero<0)entero=entero*-1;
			     		
			     		
			     		
			     			ltoa(entero,anscomb,10);
			     			outtextxy(xepru,yepru,".");
			     			xepru=xepru+15;
			     	       outtextxy(xepru,yepru,anscomb);
			     	       xepru=xepru+45;
			     		
			     	}
			     	
			     }
				if(historial[ko].h_mode==1) outtextxy(xepru+15,yepru,"(bin)");
				
				yepru=yepru+30;
				
					
			}
			
			
			
		
			while(clickmousey>=10 && clickmousey<=30 && clickmousex>=460 && clickmousex<=520)  
		 
        {
        
    	esperar_click();
    	
        }
		clickmousex=0;	
		cleardevice();
		graficar_calculadora();	
			 		
			
			
			
		}
		
		if(clickmousex>=240 && clickmousex<=300)
		{
		
		clickmousex=0;
		mode=1;	
		outtextxy(20,220,"bin");
		cleardevice();
	    graficar_calculadora();
			
			
		}
		
		
		
		
		
		
		rectangle(335,10,405,30);
		
		if(clickmousex>=335 && clickmousex<=405)
		{
			
			clickmousex=0;
	     	mode=0;	
	    	outtextxy(20,220,"dec");
	    	cleardevice();
	    	graficar_calculadora();
			
		}
		
		
		if(clickmousex>=125 && clickmousex<=185)
		{
		
			clickmousex=2;
	     	mode=2;	
	    	outtextxy(20,220,"est");
	    	cleardevice();
	    	graficar_calculadora();
		
		
	    }
		
	}
	
	
	if(clickmousey>=250 && clickmousey<=300)
	{
		if(clickmousex>=20 && clickmousex<=80)
		{
			
			ipunto=0;
            punpos=1;
            operador[contoperador]=10;
            if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
            digitos[contoperador]=temporal;
        
            if(contoperador!=1) digitos[contoperador]=temporal;
            temporal=0;
            contoperador++;
            
           
            
            outtextxy(contn+25,30,"-1");
            rectangle(20,30,530,200);
         	contn=contn+30;
         	clickmousex=0;   	
        	concan++;
			
			
			
			
			
			
		}
		
			if(clickmousex>=130 && clickmousex<=190)
		{
			
			ipunto=0;
            punpos=1;
            operador[contoperador]=11;
            if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
            if(contoperador!=1) digitos[contoperador]=temporal;
            temporal=0;
            contoperador++;
            
           
            
           outtextxy(contn+25,40,"sqrt");
            rectangle(20,30,530,200);
         	contn=contn+60;
         	clickmousex=0;   	
        	concan++;
			
			
			
			
			
			
		}
		
		if(clickmousex>=240 && clickmousex<=300)
		{
			
			ipunto=0;
            punpos=1;
            operador[contoperador]=12;
            if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
            
            digitos[contoperador]=temporal;
        
            if(contoperador!=1) digitos[contoperador]=temporal;
            temporal=0;
            contoperador++;
            
           
            
           outtextxy(contn+25,40,"*sqrt");
            rectangle(20,30,530,200);
         	contn=contn+75;
         	clickmousex=0;   	
        	concan++;
			
			
			
			
			
			
		}
		
		if(clickmousex>=350 && clickmousex<=410)
		{
			
			ipunto=0;
            punpos=1;
            operador[contoperador]=13;
            
            if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
            digitos[contoperador]=temporal;
        
            if(contoperador!=1) digitos[contoperador]=temporal;
            temporal=0;
            contoperador++;
            
           
            
            outtextxy(contn+25,30,"2");
            rectangle(20,30,530,200);
         	contn=contn+15;
         	clickmousex=0;   	
        	concan++;
			
			
			
			
			
			
		}
		
		if(clickmousex>=460 && clickmousex<=520)
		{
			
			ipunto=0;
            punpos=1;
            operador[contoperador]=14;
            
            if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
            
            digitos[contoperador]=temporal;
        
            if(contoperador!=1) digitos[contoperador]=temporal;
            temporal=0;
            
            
            if(tempoel==0)
			{
			contoperador++;
			tempoel=1;
			tempoel1=0;
			
		    }
            else
            {
            char anscomb[10];
            
			
			 tempoel=0;
			 digitosel[contoperador]=tempoel1;
			 //ltoa(contoperador,anscomb,10);
        
        
    	   // outtextxy(300,158,anscomb); 
			 
			 
		    }
			 
            rectangle(20,30,530,200);
         	clickmousex=0;   	
        	concan++;
			
			
			
			
			
			
		}
		
		
		
		
		
		
	}
	
	
	if(clickmousey>=320 && clickmousey<=370)
	{
		
		 if(clickmousex>=20 && clickmousex<=80 && contn<=480)
      {
      	ipunto=0;
        punpos=1;
        operador[contoperador]=5;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        if(contoperador!=1) digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"log");
      	contn=contn+45;
      	clickmousex=0;   	
      	concan++;
      	
      	
      }
      
      	 if(clickmousex>=130 && clickmousex<=190 && contn<=480)
      {
      	ipunto=0;
        punpos=1;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        operador[contoperador]=6;
        
        if(contoperador!=1) digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"ln");
      	contn=contn+30;
      	clickmousex=0;   	
      	concan++;
      	
      	
      }
      
      if(clickmousex>=240 && clickmousex<=300 && contn<=480)
      {
      	ipunto=0;
        punpos=1;
        operador[contoperador]=7;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        if(contoperador!=1) digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"sin");
      	contn=contn+45;
      	clickmousex=0;   	
      	concan++;
      	
      	
      }
      
      if(clickmousex>=350 && clickmousex<=410 && contn<=480)
      {
      	ipunto=0;
        punpos=1;
        operador[contoperador]=8;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        if(contoperador!=1) digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"cos");
      	contn=contn+45;
      	clickmousex=0;   	
      	concan++;
      	
      	
      }
      
      if(clickmousex>=460 && clickmousex<=520 && contn<=480)
      {
      	ipunto=0;
        punpos=1;
        operador[contoperador]=9;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        if(contoperador!=1) digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"tan");
      	contn=contn+45;
      	clickmousex=0;   	
      	concan++;
      	
      	
      }
		
		
		
		
		
	}
	
     if(clickmousey>=390 && clickmousey<=440)
{	 
	
      if(clickmousex>=30 && clickmousex<=80 && contn<=480)
      {
      	
      	if(mode!=1)
      	CIFRA(7);
      	
      	
      }
      if(clickmousex>=130 && clickmousex<=190 && contn<=480)
      {
      	if(mode!=1)
      	CIFRA(8);
      	
      	
      }
      if(clickmousex>=240 && clickmousex<=300 && contn<=480)
      {
      	if(mode!=1)
      	CIFRA(9);
      	
      	
      }
      if(clickmousex>=350 && clickmousex<=400 && contn>=15)
      {
      	
      	
      	
      	clickmousex=0;
      
      	
      	
      }
       if(clickmousex>=460 && clickmousex<=520 && contn>=15)
      {
      	cleardevice();
      	contoperador=1;
      	temporal=0;
      	concan=0;
      	tempoel=0;
      	tempoel1=0;
      	contn=0;   
      	graficar_calculadora();
      	setbkcolor(BLACK);
	    setcolor(WHITE);
      	ipunto=0;
      	clickmousex=0;
      	rectangle(20,30,530,200);
      	contadorest=0;
      	
      }
     
	
}
     if(clickmousey>=460 && clickmousey<=510)
{    

     if(clickmousex>=30 && clickmousex<=80 && contn<=480)
      {
      	if(mode!=1)
      	CIFRA(4);
      	
      	
      }
      if(clickmousex>=130 && clickmousex<=190 && contn<=480)
      {
      	if(mode!=1)
      	CIFRA(5);
      	
      	
      }
      if(clickmousex>=240 && clickmousex<=300 && contn<=480)
      {
      	if(mode!=1)
      	CIFRA(6);
      	
      	
      }
      
       if(clickmousex>=350 && clickmousex<=410 && contn<=460)
      {
      	if(mode!=2)
      	{
      	
      	
        ipunto=0;
        punpos=1;
        operador[contoperador]=3;
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        
        digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"x");
      	contn=contn+15;
      	clickmousex=0;   	
      	concan++;
        
          }
          
          
          else{
          	
          	float response,ansf;
          	char anscomb[100];
          	int ansi;
          	
          	cleardevice();
          	graficar_calculadora();
          	settextstyle(1,0,1);
          	setbkcolor(BLACK);
        	setcolor(WHITE);
          	clickmousex=0;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		response=response+matrizest[x];
          	
          		
          		
          		
          		
          		
          	}
          	
          	response=response/contadorest;
			  
			  
		ltoa(response,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=response;
    	ansf=response-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
          	
          	
          	
          	
          	
          }
        
      	
      	
      }
      
      if(clickmousex>=460 && clickmousex<=520 && contn<=460)
      {
      	
      		if(mode!=2)
      	{
      	
        ipunto=0;
        punpos=1;
        operador[contoperador]=4;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        
        digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"/");
      	contn=contn+15;
      	clickmousex=0;   	
      	concan++;
      
        
         }
      	
      	
      	
      	 else{
      	 	
      	 	cleardevice();
          	graficar_calculadora();
          	settextstyle(1,0,1);
          	setbkcolor(BLACK);
	setcolor(WHITE);
          	clickmousex=0;
          	
          	float response=0,ansf;
          	char anscomb[100];
          	int ansi;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		response=response+pow(matrizest[x],2);
          		
          		
          		
          		
          		
          		
          	}
          	
          	response=response/contadorest;
			  
			  
		ltoa(response,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=response;
    	ansf=response-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
          	
          	
          	
          	
          	
          }
        
      	
      	
      }
      	 


}
     if(clickmousey>=530 && clickmousey<=580)
     {
     
	 	
	 	if((clickmousex>=30 && clickmousex<=80 && contn<=480) || (tecla==49 && contn<=480))
      {
      	CIFRA(1);
      	
      	
      }
      if(clickmousex>=130 && clickmousex<=190 && contn<=480)
      {
      	if(mode!=1)
      	CIFRA(2);
      	
      	
      }
      if(clickmousex>=240 && clickmousex<=300 && contn<=480)
      {
      	if(mode!=1)
        CIFRA(3);
      	
      	
      }
      
      if(clickmousex>=350 && clickmousex<=410 && contn<=460)
      {
      	
      	if(mode!=2)
      	{
      	
      	
        ipunto=0;
         punpos=1;
        operador[contoperador]=1;
        
        if(negan==1)
            {
            	temporal=temporal*-1;
            	negan=0;
            	
            }
        
        
        digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"+");
      	contn=contn+15;
      	clickmousex=0;   	
      	concan++;
      
        }
        
        else{
          	
          	float response,ansf;
          	char anscomb[100];
          	int ansi;
          	
          	cleardevice();
          	graficar_calculadora();
          	settextstyle(1,0,1);
          	setbkcolor(BLACK);
        	setcolor(WHITE);
          	clickmousex=0;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		response=response+matrizest[x];
          	
          		
          		
          		
          		
          		
          	}
          	
          	//response=response/contadorest;
			  
			  
		ltoa(response,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=response;
    	ansf=response-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
          	
          	
          	
          	
          	
          }
        
      	
      	
      }
      
       if(clickmousex>=460 && clickmousex<=520 && contn<=460)
      {
      	
      	if(mode!=2)
      	{
      	
      	if(temporal==0)
      	{
      	
		  negan=1;
		   ipunto=0;
          punpos=1;	
          outtextxy(contn+25,40,"-");
       	contn=contn+15;
      	clickmousex=0;   
      		
      	}
      	
      	else
      	{
      	
        ipunto=0;
         punpos=1;
        operador[contoperador]=2;
        digitos[contoperador]=temporal;
        temporal=0;
        contoperador++;
        
        outtextxy(contn+25,40,"-");
      	contn=contn+15;
      	clickmousex=0;   	
      	concan++;
      
        }
        
        
      	
      	
      }
      	 
      	 
      	 else{
          	
          	float response,ansf;
          	char anscomb[100];
          	int ansi;
          	
          	cleardevice();
          	graficar_calculadora();
          	settextstyle(1,0,1);
          	setbkcolor(BLACK);
        	setcolor(WHITE);
          	clickmousex=0;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		response=response+pow(matrizest[x],2);
          	
          		
          		
          		
          		
          		
          	}
          	
          	//response=response/contadorest;
			  
			  
		ltoa(response,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=response;
    	ansf=response-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
          	
          	
          	
          	
          	
          }
	 	
	 	
	 }
	 	
	 	
     }


     if(clickmousey>=600 && clickmousey<=650)
     {
     	
     		if(clickmousex>=20 && clickmousex<=80 && contn<=480)
      {
      	
      	if(mode==1)CIFRA(2);
      	
      	else CIFRA(0);
      	
      	
      }
      
      
      	
     		if(clickmousex>=130 && clickmousex<=190 && contn<=480 && ipunto==0)
      {
      	
      	if(mode!=1)
      	{
      	
      	ipunto=1;
      	outtextxy(contn+25,40,".");
      	contn=contn+15;
      	clickmousex=0;   	
      	concan++;
        }
      	
      	
      }
      
      
      if(clickmousex>=240 && clickmousex<=300 && contn<=480  )
      {
      	if(mode!=1 && mode!=2)
      	{
      	
      	CIFRA(2.7182);
      	contn=contn-15;
      	outtextxy(contn+25,40,"e");
      	contn=contn+15;
       }
       
       if(mode==2)
       {
       	
       
       	contadorest++;
       	matrizest[contadorest]=temporal;
       	cleardevice();
      	contoperador=1;
      	temporal=0;
      	concan=0;
      	tempoel=0;
      	tempoel1=0;
      	contn=0;   
      	graficar_calculadora();
      	setbkcolor(BLACK);
	    setcolor(WHITE);
      	ipunto=0;
      	punpos=1;
      	clickmousex=0;
      	rectangle(20,30,530,200);
       	
       	
       	
       	
       }
       
       
      	
      	
      }
      
      
      
         
      
      if(clickmousex>=350 && clickmousex<=410 && contn<=480)
      {
      	
      	if(mode!=2)
        {
      	
      
      	outtextxy(contn+25,40,"ans");
      	contn=contn+45;
      	clickmousex=0;  
		
      	concan++;
      	temporal=temporal+ans;
         
        }
        
        else
        {
        	
        	
        	
        	
        	float response,ansf,matrizresponse[100];
          	char anscomb[100];
          	int ansi;
          	
          	cleardevice();
          	graficar_calculadora();
          	settextstyle(1,0,1);
          	setbkcolor(BLACK);
        	setcolor(WHITE);
          	clickmousex=0;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		response=response+matrizest[x];
          	
          		
          		
          		
          		
          		
          	}
          	
          	response=response/contadorest;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		matrizresponse[x]=matrizest[x]-response;
          		
          	
          		
          		matrizresponse[x]=pow(matrizresponse[x],2);
          	
          		
          	
          		
          		
          		
          	}
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          	
          	
          	response=response+matrizresponse[x];
          	
	       	}
	       	response=response/contadorest;
	       	
	       	response=pow(response,0.5);
			  
		ltoa(response,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=response;
    	ansf=response-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
          	
          	
        	
        	
        	
        	
        }
         
      	
      	
      }
      
      
      
      	
     		if(clickmousex>=460 && clickmousex<=520 )
      {
      	if(mode!=2)
      	{
      	
      	
      	RESULTADO();
      	
         }
         
         
         else
         {
         	
         		
        	float response,ansf,matrizresponse[100];
          	char anscomb[100];
          	int ansi;
          	
          	cleardevice();
          	graficar_calculadora();
          	settextstyle(1,0,1);
          	setbkcolor(BLACK);
        	setcolor(WHITE);
          	clickmousex=0;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		response=response+matrizest[x];
          	
          		
          		
          		
          		
          		
          	}
          	
          	response=response/contadorest;
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          		
          		matrizresponse[x]=matrizest[x]-response;
          		
          	
          		
          		matrizresponse[x]=pow(matrizresponse[x],2);
          	
          		
          	
          		
          		
          		
          	}
          	
          	
          	for(int x=1;x<=contadorest;x++)
          	{
          	
          	
          	response=response+matrizresponse[x];
          	
	       	}
	       	response=response/contadorest;
	       	
	       //	response=pow(response,0.5);
			  
		ltoa(response,anscomb,10);
        
        
    	outtextxy(30,158,anscomb); 
    	ansi=response;
    	ansf=response-ansi;
    	ansf=ansf*1000;
    	if(ansf<0) ansf=ansf*-1;
    	
    	ltoa(ansf,anscomb,10);
    	if(ansf!=0 )
    	{
    	
    	outtextxy(28,176,".");
    	outtextxy(35,176,anscomb);
    	
         }
          	
          	
         	
         	
         	
         	
         	
         	
         }
         
         
      }
      
      	 
     	
     }
     	
     	
     	
     }
     

	 


int main()
{

presentacion();	 

initwindow(550,670);
graficar_calculadora();




conhistorial=-1;
                    
                    
                    
                    
  
 
a_historial.open("historial.dat",ios::in);

if(a_historial){
while(!a_historial.eof())

{
	
conhistorial=conhistorial+1;
a_historial.read((char*)& historial[conhistorial],sizeof(HISTORIAL));
   
 	
	
} 

//conhistorial=conhistorial-1;

}

a_historial.close();




  
  
                    




while(tecla!=esc)
{

esperar_click();
recibir_comandos();
}

}

void esperar_click()
{

const int DELAY = 50; // Milliseconds of delay between checks

//while (!ismouseclick(WM_LBUTTONDOWN))


 if(kbhit()){
tecla=getch();

}


if(ismouseclick(WM_LBUTTONDOWN))
{

int x, y;
delay(DELAY);
getmouseclick(WM_LBUTTONDOWN, x, y);
clickmousex=x;
clickmousey=y;
punposx=x;
punposy=y;
clearmouseclick(WM_LBUTTONDOWN);



}
}
