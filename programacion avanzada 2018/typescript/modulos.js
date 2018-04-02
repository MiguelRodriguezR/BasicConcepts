var tierra;
(function (tierra) {
    class Humano {
        constructor() {
        }
        darColor() {
            return "mi color es: " + this.colorPiel;
        }
    }
    tierra.Humano = Humano;
})(tierra || (tierra = {}));
