var tierra;
(function (tierra) {
    var Humano = (function () {
        function Humano() {
        }
        Humano.prototype.darColor = function () {
            return "mi color es: " + this.colorPiel;
        };
        return Humano;
    }());
    tierra.Humano = Humano;
})(tierra || (tierra = {}));
