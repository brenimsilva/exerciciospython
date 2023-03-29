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

class Televisao:
    def __init__(self) -> None:
        self.ligada = False;
        self.canal = 0; 
    
    def mudarCanalPracima(self):
        self.canal += 1;
        print(f"O Canal foi mudado para {self.canal}");
    
    def mudarCanalPraBaixo(self):
        self.canal -= 1;
        if(self.canal <= 0):
            self.canal = 0;
        print(f"O canal foi mudado para {self.canal}");
    
    def ligarDesligarTelevisao(self):
        self.ligada = not self.ligada;
        print(f"A televisao esta {'ligada' if self.ligada else 'desligada'}")

televisao = Televisao();
televisao.mudarCanalPraBaixo()
televisao.mudarCanalPracima()
televisao.ligarDesligarTelevisao();
televisao.ligarDesligarTelevisao();
