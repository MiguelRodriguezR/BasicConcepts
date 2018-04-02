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
var Humano = tierra.Humano;
class Persona extends Humano {
    constructor() {
        super();
        this.colorPiel = "blanco";
    }
    saludar() {
        return "Hola, " + this.saludo;
    }
    darNombre(nombre) {
        this.saludo = nombre;
    }
    darEdad() {
        return this.edad;
    }
    metodo2() {
        return [this.darEdad()];
    }
}
var mario = new Persona();
mario.darNombre("Camilo");
console.log(mario.saludar());
console.log(mario.darColor());
