class Calculadora:
    def __init__(self, nome):
        self.nome = nome;

    def somar(self, num1, num2):
        return num1 + num2;

    def multiplicar(self, num1, num2):
        return num1 * num2;

    def subtrair(self, num1, num2):
        return num1 - num2;

    def dividir (self, num1, num2):
        return num1 / num2;

calc = Calculadora("Calc");

resultado = calc.multiplicar(24,33);
calc.somar(1,5);

####################################################################
