//capturador de fecha y hora

#include <cstdlib>
#include <iostream>
#include <time.h>

using namespace std;

tm calendario;

void captura_fecha_hora();
void mostrar_fecha_hora();

int main()

{
	int x=1;
	while(x)
	{
	
	
	captura_fecha_hora();
	mostrar_fecha_hora();
	
    }
	
	
	cout<<endl; system("pause>null");
	
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
   
   hora=calendario.tm_hour;
   minutos=calendario.tm_min;
   segundos=calendario.tm_sec;
   
   system("cls");
   
   
   cout<<hora<<" "<<minutos<<" "<<segundos<<" "<<endl;	
	
	
	
	
	
	
	
}
