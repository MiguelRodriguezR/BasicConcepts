// function holaMundo(nombre : string):string{
//   return "Hola Mundo Soy: "+nombre;
// }
//
// var nombre : string = "Miguel";
// let resultado : string = holaMundo(nombre);
//
// document.getElementById("container").innerHTML=resultado;
//import "./modulos";
//ss

import Humano = tierra.Humano;
class Persona extends Humano{
    saludo: string;
    public edad: number;

    constructor(){
      super();
      this.colorPiel = "blanco";
    }

    saludar():string {
        return "Hola, " + this.saludo;
    }

    public darNombre(nombre:string){
      this.saludo =nombre;

    }

    darEdad():number{
      return this.edad;
    }

    metodo2():Array<number>{
      return [this.darEdad()];
    }
}

var mario = new Persona();
mario.darNombre("Camilo");
console.log(mario.saludar());
console.log(mario.darColor());
