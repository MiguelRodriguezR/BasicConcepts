# include <iostream>
# include <stdio.h>
# include <cstdlib>
# include <conio.h>

using namespace std;
int cont=0;

struct ciudad{

char nombre [40];
int poblacion;
ciudad *psiguiente;	
	
	
	
};

ciudad *pprimer;
ciudad *pultimo;

void aniadir()
{

 if (cont==0)
{

 pprimer=new(ciudad);
 cout<<"Nombre : ";
 cin>>pprimer->nombre;
 cout<<"Poblacion : ";
 cin>>pprimer->poblacion;
 pprimer->psiguiente=NULL;
 pultimo=pprimer;
 cont++;
}

else
{
	
	pultimo->psiguiente=new(ciudad);
	pultimo=pultimo->psiguiente;
	cout<<"Nombre : ";
	cin>>pultimo->nombre;
	cout<<"Poblacion : ";
	cin>>pultimo->poblacion;
   	pultimo->psiguiente=NULL;
   	cont++;
	
	
	
}
	
	
	
	
} 

void consultar()
{
	system("cls");
	
	for(int x=0;x<cont;x++)
	{
		if(x==0)
		{
		cout<<pprimer->nombre;
		cout<<endl<<pprimer->poblacion;
		pultimo=pprimer->psiguiente;
		cout<<endl<<endl;
	    }
	    else
	    {
	    	cout<<pultimo->nombre;
	    	cout<<endl;
	    	cout<<pultimo->poblacion;
	    	pultimo=pultimo->psiguiente;
	    	cout<<endl<<endl;
	    	
	    }
		
	}
	
	getche();
	
	
}

int main(){

int op;	
	
while(op!=0)
{
system ("cls");	
	
cout<<"eliga una pocion"<<endl;
cout<<"1. aniadir ciudad";
cout<<endl<<"2. consultar ciudades";
cout<<endl<<"0. salir"<<endl;
cin>>op;

switch (op)
{
	case 1:
	
	aniadir();
	
	break;
		
	case 2:
	
	consultar();
		
	break;	
}

	
}
	
system("pause");	
	
return 0;	
	
}
