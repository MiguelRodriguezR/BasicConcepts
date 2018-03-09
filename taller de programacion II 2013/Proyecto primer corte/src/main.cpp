////////////////////////////////////////////////////////////////
//                                                            //
//     PROGRAMA CREADO, DESARROLLADO Y DISEÑADO POR :         //
//      			MIGUEL RODRIGUEZ 				    	  //
//                                                            //
////////////////////////////////////////////////////////////////



# include <cstdlib>
# include <windows.h>
# include <conio.h>
# include <iostream>
# include <stdlib.h>
# include <stdio.h>
# include <fstream>
# include <string.h> 
# include <time.h> 

#define arriba 72
#define abajo 80
#define esc 27
#define enter 13
#define borrar system("cls")


using namespace std;


int opmenu=1;
char tecla;
int px=50,py=12;
int limitepu=0,limitepd=0,limitantep;
int PT;
long contrasenia,contra;
fstream c1;
fstream c2;
fstream aa_clientes;
fstream aa_productos;
fstream a_clientes;
fstream a_productos;
tm calendario;
int contproduct=0,contclient=0;


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
gotoxy(9,8);cout<<"//             UNIVERSIDAD DE NARI";printf("%c",165);cout<<"O";cout<<"                          //";
gotoxy(9,9);cout<<"//                                                            //";
gotoxy(9,10);cout<<"//                                                            //";
gotoxy(9,11);cout<<"//     PROGRAMA CREADO, DESARROLLADO Y DISEÑADO POR :         //";
gotoxy(9,12);cout<<"//                 MIGUEL RODRIGUEZ                     	  //";
gotoxy(9,13);cout<<"//                                                            //";
gotoxy(9,14);cout<<"//      Presione ESC en cualquier momento para salir          //";
gotoxy(9,15);cout<<"//                                                            //";
gotoxy(9,16);cout<<"////////////////////////////////////////////////////////////////";
 	
 	getche();
 	
 	
 	
 }   


void captura_fecha_hora()
{
	
	time_t reloj;
	
	time(&reloj);
	calendario=*localtime(&reloj);
	
	
	
	
	
}

void mostrar_fecha_hora()

{
   short hora,minutos,segundos,dia,mes;
   
   int anio;
   
   anio=calendario.tm_year+1900;
   mes=calendario.tm_mon+1;
   dia=calendario.tm_mday;
   
   system("cls");
   
   
  gotoxy(2,0); cout<<"FECHA: "<<dia<<"/"<<mes<<"/"<<anio;	
	
	
	
	
	
	
	
}








    
    
void pint_puntero(){
	
	gotoxy(px,py);printf("%c",17);
	
}   

struct FECHA
{
int Dia;
int Mes;
int anio;	
	
};

struct HORA
{
 int  hora;
 int  minuto;
 int  segundo;	
	
	
	
	
};





struct CLIENTE{
       
       char identificacion[30],nombre[40],apellido[40];
       int cantidad_productos_comprados; 
        FECHA fecha_compra [100];
          HORA hora_compra [100];
       
          char CODIGO_P_COMPRADOS[100][100]; 
         

        
       
       
       
       
       };
       
       CLIENTE cliente[100];
       
       
struct PRODUCTO{

       
       char codigo[40],nombre[40];
       int tamanio;
       float precio;
       
       
       
       
       
       };
       
       PRODUCTO producto[100]; 
       
       
 void guardar()
{
	
    int i;
    a_clientes.open("clientes.dat",ios::out);
	for(i=1;i<=contclient;i++){
                        
      a_clientes.write((char*)& cliente[i],sizeof(CLIENTE));
   
                       }
      a_clientes.close();                 
                       
	
	a_productos.open("productos.dat",ios::out);
	for(i=1;i<=contproduct;i++){
	
	  a_productos.write((char*)& producto[i],sizeof(PRODUCTO));
	  
	                           }
	  a_productos.close();
	
	
	
	
}          

void cargar()
{

contclient=0;
contproduct=0;


aa_clientes.open("clientes.dat",ios::in);

if(aa_clientes){
while(!aa_clientes.eof())

{
	
contclient=contclient+1;
 aa_clientes.read((char*)& cliente[contclient],sizeof(CLIENTE));
   
 	
	
} 

contclient=contclient-1;

}
else cout<<"el archivo no existe";
aa_clientes.close();	


aa_productos.open("productos.dat",ios::in);

if(aa_productos){
while(!aa_productos.eof()){
	
 contproduct=contproduct+1;
 aa_productos.read((char*)& producto[contproduct],sizeof(PRODUCTO));
   
 	
	
} 

contproduct--;

}
else cout<<"el archivo no existe";
aa_productos.close();	



}
       
 int buscar_producto(char codig[])
 {
 
 int encontrado;
 encontrado=0;
 int i;
 i=1;
 while(i<=contproduct && encontrado==0)
 {
   if (strcmp(producto[i].codigo,codig)==0)
   {
     encontrado=i;                              
   }          
    else 
    i=i+1;        
  }
 
 return (encontrado);
  
}

int buscar_cliente(char codig[])
 {
 
 int encontrado;
 encontrado=0;
 int i;
 i=1;
 while(i<=contclient && encontrado==0)
 {
   if (strcmp(cliente[i].identificacion,codig)==0)
   {
     encontrado=i;                              
   }          
    else 
    i=i+1;        
  }
 
 return (encontrado);
  
}
       
       
       
void marco(){
     
   //lineas horizontales
         int i;

         for(i=2;i<78;i++){



                gotoxy(i,1); printf("%c",205);
                gotoxy(i,23); printf("%c",205);


                }
                
                
    //lineas verticales

             for(i=1;i<23;i++){



                gotoxy(2,i); printf("%c",186);
                gotoxy(77,i); printf("%c",186);




                           }
                           
      //esquinas                     


                gotoxy(2,1); printf("%c",201);
                gotoxy(77,23); printf("%c",188);
                gotoxy(77,1); printf("%c",187);
                gotoxy(2,23); printf("%c",200);

              
     
     
     
     
     
     }  
     

                                          





	



void menu(){
     
     if(opmenu==1)//principal
     {
     	
       captura_fecha_hora()	;
     	
       borrar;
       mostrar_fecha_hora() ; 
       marco();           
       limitantep=1;
       px=50;
       py=12;  
	   pint_puntero(); 
	   
	   
	   
	   
     
     gotoxy(32,10);cout<<"-----PERFUMES-----";
     gotoxy(32,12);cout<<"     cliente";
     gotoxy(32,13);cout<<"  administrador";
     opmenu=0;
     
     }
     
     if(opmenu==2)//cliente
     {
       borrar;
       marco();           
       limitantep=2; 
      px=55;    
      py=12;  
	   pint_puntero();         
      gotoxy(32,10);cout<<"  Que Desea Hacer?" ;
      gotoxy(32,12);cout<<" comprar un producto" ;
      gotoxy(32,13);cout<<"    menu anterior    " ;  
           
                  
         opmenu=0;         
                  
                  
                  }
                  
     if(opmenu==3)//administrador
     {
         
        
        
 
            limitantep=3; 
                  
  
        if(contra==contrasenia)
        {
              borrar;
              marco(); 
              
              
               px=59;
               py=12; 
			   pint_puntero();                   
               gotoxy(25,10);cout<<"     Que Desea Hacer?" ;
               gotoxy(25,12);cout<<"    cambiar productos" ;
               gotoxy(25,13);cout<<"mirar informacion de los clientes" ;
               gotoxy(25,14);cout<<"     cambiar contraseña" ;
			   gotoxy(25,15);cout<<"     porcentaje de ventas" ; 
               gotoxy(25,16);cout<<"       menu anterior    " ; 
               opmenu=0;                
                               
                               
                               
                               }
                               
          else
          {
          	
              borrar;
              marco();   
              gotoxy(32,10);cout<<"  contraseña incorrecta " ;
              getche();
              opmenu=1;
              
              
              
              }                     
        
        
        
        
        
                  
                  
                  
                  }        
     
     if (opmenu==4)//modificar producto
     {
     	
     	 borrar;
       marco();           
       limitantep=4;
       px=50;
       py=12;   
	   pint_puntero();   
     
       gotoxy(32,10);cout<<"Que Desea Hacer?" ;
      gotoxy(32,12);cout<<" crear producto" ;
      gotoxy(32,13);cout<<"modificar producto" ;
      gotoxy(32,14);cout<<" eliminar producto" ;
      gotoxy(32,15);cout<<"  menu anterior    " ;  
      opmenu=0; 
     	
     	
     	
     	
     	
     	
     	
     	
     	
     	
     	
     }
     
     if (opmenu==5)//nuevo producto
     {
      	
      		 borrar;
             marco();           
             px=50;
             py=12; 
             char codigo[100];
             
             
             gotoxy(32,10);cout<<"ingrese el codigo del producto ";
             cin>>codigo;
             if(buscar_producto(codigo)==0)
             {
             	contproduct++;
                strcpy (producto[contproduct].codigo,codigo);
                borrar;marco();
                gotoxy(32,10); cout<<"ingrese nombre producto ";
                 cin.get();
                 cin.getline(producto[contproduct].nombre,40);
                 borrar;marco(); 
                gotoxy(32,10); cout<<"ingrese tamanio producto ";
                 cin>>producto[contproduct].tamanio;
                  borrar;marco();
                gotoxy(32,10); cout<<"ingrese precio producto ";
                 cin>>producto[contproduct].precio;
                 
                 guardar();

             	
             }
             
    	else {
    	gotoxy(32,10);cout<<"ese codigo ya existe ";
    	system("pause>null");
    	     }
        
      	
      	      opmenu=4;
      	
      }
      
     if (opmenu==6)//cambiar precio a producto
     {
           	borrar;
            marco();           
            px=50;
            py=12; 
            char codigo[100];
            int posicion;
            gotoxy(32,10);cout<<"ingrese el codigo del producto";
            cin>>codigo;
            posicion=buscar_producto(codigo);
            if (posicion!=0)
            {borrar;marco();
           gotoxy(32,10); cout<<"Nombre producto: "<<producto[posicion].nombre;
           gotoxy(32,11); cout<<"Tamanio Producto: "<<producto[posicion].tamanio;
           gotoxy(32,12); cout<<"Precio Producto: "<<producto[posicion].precio;
           gotoxy(32,13); cout<<"Indique el nuevo precio: ";
           cin>>producto[posicion].precio;
           guardar();
           
            }
            else {borrar;marco();
             	gotoxy(32,10);cout<<"ese codigo no existe ";
            }
            
            
            
            
      	opmenu=4;
      	
      }
      
     if (opmenu==7)//lista de productos para cliente
     {
      		borrar;
            marco(); 
			limitantep=7; 
	        px=73;
            py=4;
               
                gotoxy (5 ,3);cout<<"NOMBRE";
				gotoxy (31,3);cout<<"PRECIO";
				gotoxy (61,3);cout<<"TAMA";printf("%c",165);cout<<"O";
            
            pint_puntero(); 
            int x,y;
			for (x=1;x<=contproduct;x++)
			{
				
				gotoxy (5 ,x+3);cout<<producto[x].nombre;
				gotoxy (31,x+3);cout<<"$ ";cout<<producto[x].precio;
				gotoxy (61,x+3);cout<<producto[x].tamanio;cout<<" ml";
				
				
				
				
				
			}
			gotoxy (31 ,contproduct+4);cout<<"atras";
			
			
      	
      	opmenu=0;
      	
      	
      }
     
     if (opmenu==8)//eliminar producto
     {
      		borrar;
            marco();
            char codigo[100];
            int posicion;
            int x;
      	
        gotoxy(25,10);cout<<"codigo del producto que desea eliminar ";
        cin>>codigo;
        posicion=buscar_producto(codigo);
            if (posicion!=0)
            {borrar;marco();
            char option;
           gotoxy(32,10); cout<<"Nombre producto: "<<producto[posicion].nombre;
           gotoxy(32,11); cout<<"Tamanio Producto: "<<producto[posicion].tamanio;
           gotoxy(32,12); cout<<"Precio Producto: "<<producto[posicion].precio;
           gotoxy(32,13); cout<<"quiere eliminar este producto? S/N ";
           cin>>option;
           switch(option){
           	
           	case 'S':
           		
           		
           		for(x=posicion;x<=contproduct;x++)
           		{
           			
           		strcpy(	producto[x].codigo,producto[x+1].codigo);
				strcpy(	producto[x].nombre,producto[x+1].nombre);
				producto[x].precio=producto[x+1].precio;
				producto[x].tamanio=producto[x+1].tamanio;
					       		}
					       		
					     contproduct--; 
					     guardar();
						 
						 
						 opmenu=4; 		
           		
           		
           		break;
           		
           		
           	case 'N' :
           		
           		opmenu=4;
           		
           		break;
           	
           	
           	
           	
           }
           
            }
            else {borrar;marco();
             	gotoxy(32,10);cout<<"ese codigo no existe ";
             	opmenu=4;
            }
      	
      	
      	
      	
      	
      }
     
     if (opmenu==9)//nuevo cliente y registro de producto
     {
     	
      	
            borrar;
             marco();           
             int posicion,ce,x;
             char identificacion[100],ne[100];
             gotoxy(32,10);cout<<"ingrese su cedula porfavor ";
             cin>>identificacion;
             
             
             
             
             if(buscar_cliente(identificacion)==0)
             {
     	       contclient++; 
     	       strcpy(cliente[contclient].identificacion,identificacion);
     	       borrar;marco();
     	       cin.get();
                gotoxy(32,10); cout<<"ingrese su nombre ";
                 cin.getline(cliente[contclient].nombre,40);
                 borrar;marco(); 
                gotoxy(32,10); cout<<"ingrese su apellido ";
                  cin.getline(cliente[contclient].apellido,40);
                 
     	      
     	
     	
     	
     	   }
     	   posicion=buscar_cliente(identificacion);
     	   
     	   cliente[posicion].cantidad_productos_comprados++;
     	   
     	  ce=cliente[posicion].cantidad_productos_comprados;
     	  
     	  strcpy (ne,producto[py-3].codigo);
     	  
     	  strcpy (cliente[posicion].CODIGO_P_COMPRADOS[ce],ne);
     	  
     	  captura_fecha_hora();
     	  
     	  
     	  
     	  
     	  cliente[posicion].fecha_compra[ce].anio=calendario.tm_year+1900;
     	  cliente[posicion].fecha_compra[ce].Mes=calendario.tm_mon+1;
     	  cliente[posicion].fecha_compra[ce].Dia=calendario.tm_mday;
     	     
     	  cliente[posicion].hora_compra[ce].hora=calendario.tm_hour;
     	  cliente[posicion].hora_compra[ce].minuto=calendario.tm_min;
     	  cliente[posicion].hora_compra[ce].segundo=calendario.tm_sec;
     	  
     	  
     	   borrar;
             marco();
             
     	  gotoxy(32,10);cout<<" Producto Añadido al Cliente ";
     	  
     	  gotoxy(32,11);cout<<" Nombre: "<<cliente[posicion].nombre;
     	  
     	  gotoxy(32,12);cout<<" apellido: "<<cliente[posicion].apellido; 
     	  
     	  gotoxy(32,13);cout<<"codigo Poducto : "<<cliente[posicion].CODIGO_P_COMPRADOS[ce];
     	  
     	  gotoxy(32,14);cout<<"fecha de compra : "<<cliente[posicion].fecha_compra[ce].Dia<<"/"<<cliente[posicion].fecha_compra[ce].Mes<<"/"<<cliente[posicion].fecha_compra[ce].anio;
     	  
     	  gotoxy(32,15);cout<<"hora de compra : "<<cliente[posicion].hora_compra[ce].hora<<":"<<cliente[posicion].hora_compra[ce].minuto;
     	  
     	  
     	  guardar();
     	  	
     	  	
     	  	
     	  
     	  
     	  	
     	  	
											
     	              
     	  
			 
     	
     	  
     	   
     	   
              system("PAUSE>null");
      	
      	      opmenu=2;
     	
     }
     
     if (opmenu==10)//mIrar informacion cliente
	 {
     		borrar;
            marco(); 
			limitantep=10; 
	        px=73;
            py=4;
            pint_puntero(); 
            int x,y;
                gotoxy (4 ,3);cout<<"IDENTIFICACION";
				gotoxy (20,3);cout<<"NOMBRE";
				gotoxy (38,3);cout<<"APELLIDO";
				gotoxy (54,3);cout<<"PRODUCTOS COMPRADOS";
            
			for (x=1;x<=contclient;x++)
			{
				gotoxy (4 ,x+3);cout<<cliente[x].identificacion;
				gotoxy (20,x+3);cout<<cliente[x].nombre;
				gotoxy (38,x+3);cout<<cliente[x].apellido;
				gotoxy (61,x+3);cout<<cliente[x].cantidad_productos_comprados;
				
				
				
			}
			gotoxy (31 ,contclient+4);cout<<"atras";
     	
     	
     	
     	opmenu=0;
     	
     	
     	
     	
     	
     	
     	
     }
	 if (opmenu==11)//informacion individual cliente
	 {
	 	borrar;
        marco();
        int x,z,l=1;
        
                gotoxy (4,3);cout<<"IDENTIFICACION : ";cout<<cliente[py-3].identificacion;
				gotoxy (4,4);cout<<"NOMBRE : ";cout<<cliente[py-3].nombre;
				gotoxy (4,5);cout<<"APELLIDO : ";cout<<cliente[py-3].apellido;
				gotoxy (4,6);cout<<"PRODUCTOS COMPRADOS : ";cout<<cliente[py-3].cantidad_productos_comprados;
				gotoxy (3,9);cout<<"LISTA PRODUCTOS COMPRADOS POR EL CLIENTE";
				gotoxy (5,11);cout<<"CODIGO ";
				gotoxy (24,11);cout<<"NOMBRE";
				gotoxy (48,11);cout<<"FECHA";
				gotoxy (61,11);cout<<"HORA";
				
				for(x=1;x<=cliente[py-3].cantidad_productos_comprados;x++)
				{
					for(z=1;z<=contproduct;z++)
					{
					
					
                         if (strcmp(cliente[py-3].CODIGO_P_COMPRADOS[x],producto[z].codigo)==0)
                          {
                          	if(l+12<=20)
                          	{
                          	
                          	
                              gotoxy (5,l+12);cout<<cliente[py-3].CODIGO_P_COMPRADOS[x];
							  gotoxy (24,l+12);cout<<producto[z].nombre; 
							  gotoxy (48,l+12);cout<<cliente[py-3].fecha_compra[x].Dia<<"/"<<cliente[py-3].fecha_compra[x].Mes<<"/"<<cliente[py-3].fecha_compra[x].anio; 
							  gotoxy (61,l+12);cout<<cliente[py-3].hora_compra[x].hora<<":"<<cliente[py-3].hora_compra[x].minuto<<":"<<cliente[py-3].hora_compra[x].segundo; 
							  
							  l++;
							  
						    }
						    
						    else
						    {
						    	system("pause>null");
						    	
						    	borrar;
						    	marco();
						    	gotoxy (4,3);cout<<"IDENTIFICACION : ";cout<<cliente[py-3].identificacion;
			                  	gotoxy (4,4);cout<<"NOMBRE : ";cout<<cliente[py-3].nombre;
				                gotoxy (4,5);cout<<"APELLIDO : ";cout<<cliente[py-3].apellido;
				                gotoxy (4,6);cout<<"PRODUCTOS COMPRADOS : ";cout<<cliente[py-3].cantidad_productos_comprados;
				                gotoxy (3,9);cout<<"LISTA PRODUCTOS COMPRADOS POR EL CLIENTE";
				                gotoxy (5,11);cout<<"CODIGO ";
				                gotoxy (24,11);cout<<"NOMBRE";
				                gotoxy (48,11);cout<<"FECHA";
			                	gotoxy (61,11);cout<<"HORA";
				                
				                l=1;
						    	
						    	
						    	
						    	
						    	
						    	
						    }
						                               
                          }
						  
				    }		      
					
					
					
				}
				
				system("pause>null");
				
				
				
				opmenu=10;
				
        
	 	
	 	
	 	
	 	
	 	
	 	
	 	
	 	
	 }
	 
	 if (opmenu==12)//listado de productos
	 {
	 	
	 	borrar;
            marco(); 
			limitantep=12; 
	        px=73;
            py=4;
               
                gotoxy (5 ,3);cout<<"NOMBRE";
				gotoxy (31,3);cout<<"PRECIO";
				gotoxy (61,3);cout<<"TAMA";printf("%c",165);cout<<"O";
            
            pint_puntero(); 
            int x,y;
			for (x=1;x<=contproduct;x++)
			{
				
				gotoxy (5 ,x+3);cout<<producto[x].nombre;
				gotoxy (31,x+3);cout<<"$ ";cout<<producto[x].precio;
				gotoxy (61,x+3);cout<<producto[x].tamanio;cout<<" ml";
				
				
				
				
				
			}
			gotoxy (31 ,contproduct+4);cout<<"atras";
			
			
      	
      	opmenu=0;
	 	
	 	
	 	
	 	
	 }
	 if (opmenu==13)//informacion producto individual
	 {
	 	borrar;
        marco();
        int conta=0,x,y,z;
        
                gotoxy (4,3);cout<<"CODIGO : ";cout<<producto[py-3].codigo;
				gotoxy (4,4);cout<<"NOMBRE : ";cout<<producto[py-3].nombre;
				gotoxy (4,5);cout<<"TAMAÑO : ";cout<<producto[py-3].tamanio;
				
				for(x=1;x<=contclient;x++)
				{
					for(y=1;y<=cliente[x].cantidad_productos_comprados;y++)
					{
						
							if (strcmp(cliente[x].CODIGO_P_COMPRADOS[y],producto[py-3].codigo)==0)
                          {
                          	conta++;
							
							
							
							
					        }
					
					
						
						
						
					}
					
					
					
				}
				
				gotoxy (4,6);cout<<"CANTIDAD DE VENTAS : ";cout<<conta;
				
				int total=0;
				
				for(x=1;x<=contclient;x++)
				{
					
					total=total+cliente[x].cantidad_productos_comprados;
					
				}
				float porcentaje;
				porcentaje=(conta*100)/total;
				gotoxy (4,7);cout<<"PORCENTAJE DE VENTAS: ";cout<<porcentaje<<" % ";
				system("pause>null");
				
        
        opmenu=12;
	 	
	 	
	 	
	 }
     
     }
     
     
  void limitante(){
        
        if(limitantep==1)
       {
         
         if(py==12)
         {
          limitepu=1;
          limitepd=0;
          }
          
          if(py==13)
         {
          limitepu=0;
          limitepd=1;
          }
       } 
        //////////////////////////
        if(limitantep==2)
       {
                           
                           
         
         if(py==12)
         {
          limitepu=1;
          limitepd=0;
          
          }
          if(py>12 && py<13)
          {
               limitepu=0;
               limitepd=0;     
                   
                   
                   }
          
          
          
          if(py==13)
         {
         limitepu=0;
          limitepd=1;
          }
        
         
                   
         
       
       }
       
       
       /////////////////////////////////////////
       
        if(limitantep==3)
       {
                           
                           
         
         if(py==12)
         {
          limitepu=1;
          limitepd=0;
          
          }
          if(py>12 && py<16)
          {
               limitepu=0;
               limitepd=0;     
                   
                   
                   }
          
          
          
          if(py==16)
         {
         limitepu=0;
          limitepd=1;
          }
        
         
                   
         
       
       }
       
       
         if(limitantep==4)
       {
                           
                           
         
         if(py==12)
         {
          limitepu=1;
          limitepd=0;
          
          }
          if(py>12 && py<15)
          {
               limitepu=0;
               limitepd=0;     
                   
                   
                   }
          
          
          
          if(py==15)
         {
         limitepu=0;
          limitepd=1;
          }
        
         
                   
         
       
       }
       
         if(limitantep==7)
         {
         	if(py==4)
         {
          limitepu=1;
          limitepd=0;
          
          }
          
          if(py>4 && py<contproduct+4)
          {
               limitepu=0;
               limitepd=0;     
                   
                   
                   }
                   
            if(py==contproduct+4)
         {
          limitepu=0;
          limitepd=1;
          
          }       
         	
         	
         	
         	
         }
         if(limitantep==10)
         {
         	if(py==4)
         {
          limitepu=1;
          limitepd=0;
          
          }
          
          if(py>4 && py<contclient+4)
          {
               limitepu=0;
               limitepd=0;     
                   
                   
                   }
                   
            if(py==contclient+4)
         {
          limitepu=0;
          limitepd=1;
          
          }       
         	
         	
         	
         	
         }
         if(limitantep==12)
         {
         	if(py==4)
         {
          limitepu=1;
          limitepd=0;
          
          }
          
          if(py>4 && py<contproduct+4)
          {
               limitepu=0;
               limitepd=0;     
                   
                   
                   }
                   
            if(py==contproduct+4)
         {
          limitepu=0;
          limitepd=1;
          
          }       
         	
         	
         	
         	
         }
       
       }   
     
 void puntero()
     {
               
               
               
                 
               
               if(kbhit()){
                           
                           tecla=getch();
                           switch(tecla){
                                         
                                    case arriba:
                                         
                                         if (limitepu==0)
                                         {
                                         
                                         gotoxy(px,py);cout<<" ";
                                         py--;
                                         gotoxy(px,py);printf("%c",17);
                                          
                                          }
                      
                      
                                     break;
                                     
                                         
                                     
                                     
                                    case abajo:
                                         
                                         if (limitepd==0)
                                         {
                                         
                                         gotoxy(px,py);cout<<" ";
                                         py++;
                                         gotoxy(px,py);printf("%c",17);
                                         
                                         }
                                         
                      
                                     break;   
      
                                     
                                     case enter:
                                          
                                          switch(limitantep)
                                          {
                                             case 1:                 
                                               switch(py)
                                               {
                                                   case 12:
                                                        
                                                      
                                                        
                                                        opmenu=2;
                                                        
                                                        break;
                                                        
                                                     case 13:
                                                          
                                                            borrar;
                                                            marco();           
        
         
                                                            gotoxy(32,10);cout<<"  digite la contraseña " ;
                                                            cin>>contra;
                                                             opmenu=3;
                                                          
                                                          break;
                                                              
                                                         
                                                         
                                                         }           
                                                          
                                                          
                                                          
                                                           
                                                                                               
                                                  break;
                                                  
                                                  case 2:
                                                       
                                                       switch(py)
                                               {
                                               	
                                               	      case 12:
                                               	      	opmenu=7;
                                               	      	limitantep=4;
                                               	      	break;
                                                   	
                                                       case 13:
                                                       opmenu=1;
                                                       break;
                                                       
                                                       } 
                                                       
                                                       break;
                                                       
                                                       
                                                   case 3:
                                                        switch(py)
                                                        {
                                                        	
                                                        	
                                                        	
                                                        	case 12:
                                                        		
                                                        		opmenu=4;
                                                        		
                                                        		break;
                                                        		
                                                        	case 13:
															
															   opmenu=10;
															   
															   break;
															   
															   	
                                                        		
                                                        	
                                                        	
                                                                  
                                                            case 14:
                                                                 
                                                                 
                                                                 borrar;
                                                                 marco(); 
                                                         gotoxy(32,10);
                                                     
 /////////////////////////////////////////////////GUARDA ARCHIVO CONTRASEÑA/////////////////////////////////////////////////////////////////////////////
                                                        
                                                                   
                                                          cout<<"digite la nueva contraseña ";
                                                                        cin>>contrasenia;
                                                                        
                                                                        
      
                                                                   c2.open("contra.dat",ios::out);
                                                                 c2<<contrasenia;
                                                                    c2.close();
                                                                    
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                                                                    
                                                                   opmenu=1;
                                                                   
                                                                   
                                                                   
                                                               break;  
                                                               
                                                               
                                                               case 15:
                                                               	opmenu=12;
                                                               	break;
															   
															        
                                                             
                                                            case 16:
                                                              opmenu=1;
                                                               break;    
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             }    
                                                             
                                                             break;
                                                             
                                                     case 4:
													     switch(py)
														 {
														 	
														 	    case 12:
														 	    	
														 	    	opmenu=5;
														 	    	
														 	    	break;
														 	    	
														 	    case 13:
																 
																    opmenu=6;
																    
																    
																	break; 
																	
																case 14:
																
																     opmenu=8;
																	 
																	 break;		
														 	
														 	
														 	
														 		case 15:
                                                        		
                                                        		opmenu=3;
                                                        		
                                                        		break;
                                                        		
                                                        		
                                                        		 
                                                        		
														 	
														 	
														 }  
														 
														 break;
														 
														 case 7:
														 	
													   if(py==contproduct+4)
													   {
													   	
													   	opmenu=2;
													   	
													   	
													   	
													   }
													   
													   else 
													   {
													   	
													   opmenu=9;								   	
													   	
													   }
														
														
														 
														 
														break ; 
														
														
														case 10:
															
															 if(py==contclient+4)
													   {
													   	
													   	opmenu=3;
													   	
													   	
													   	
													   }
													   else 
													   {
													   	
													   	opmenu=11;
													   	
													   }
															
															
															
															
															break;
															
															
														case 12:
															if(py==contproduct+4)
															{
													   	
													   	opmenu=3;
													   	     }
													   	     
													   	     else 
													   {
													   	
													   	opmenu=13;
													   	
													   }
													   	
													   	
													   	
													   
															
														
														
														
														break;	
														
                                                       
                                                       
                                                       }    

                              
                              
                              }
                }        
                              
                              
    }

    
    

     
     
     
     
     
     
     int main(){
     	
     	
     	presentacion();
         
         
           c1.open("contra.dat",ios::in);
                   c1>>contrasenia;
                   
                   c1.close();
                   
                    
                  
                         
                  
         
         cargar();
         
         
         
         
         marco();
        
        
       
         while(tecla != esc)
 { 
         
          menu();
          puntero();
          limitante();
         
         
         
         }  
         
         guardar();
         
         
         
         
          
         
         }  
