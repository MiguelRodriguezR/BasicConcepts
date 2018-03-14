// function holaMundo(nombre : string):string{
//   return "Hola Mundo Soy: "+nombre;
// }
//
// var nombre : string = "Miguel";
// let resultado : string = holaMundo(nombre);
//
// document.getElementById("container").innerHTML=resultado;
//import "./modulos";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Humano = tierra.Humano;
var Persona = (function (_super) {
    __extends(Persona, _super);
    function Persona() {
        var _this = _super.call(this) || this;
        _this.colorPiel = "blanco";
        return _this;
    }
    Persona.prototype.saludar = function () {
        return "Hola, " + this.saludo;
    };
    Persona.prototype.darNombre = function (nombre) {
        this.saludo = nombre;
    };
    Persona.prototype.darEdad = function () {
        return this.edad;
    };
    Persona.prototype.metodo2 = function () {
        return [this.darEdad()];
    };
    return Persona;
}(Humano));
var mario = new Persona();
mario.darNombre("Camilo");
console.log(mario.saludar());
console.log(mario.darColor());
