def calcAumento(salario):
  salarioInicial = salario
  percentual = 0
  valorDoAumento = 0
  novoSalario = 0;
  
  if(salario <= 280):
    novoSalario = salario * 1.2;
    percentual = "20%";
    valorDoAumento = novoSalario - salario;
    
    return printaMensagem(salario, novoSalario, percentual, valorDoAumento)
  
  if (salario <= 700):
    novoSalario = salario * 1.15;
    percentual = "15%";
    valorDoAumento = novoSalario - salario;
    return printaMensagem(salario, novoSalario, percentual, valorDoAumento)

  if (salario <= 1500):
    novoSalario = salario * 1.1;
    percentual = "10%";
    valorDoAumento = novoSalario - salario;
    return printaMensagem(salario, novoSalario, percentual, valorDoAumento)

  novoSalario = salario * 1.05;
  percentual = "5%";
  valorDoAumento = novoSalario - salario;
  return printaMensagem(salario, novoSalario, percentual, valorDoAumento)

def printaMensagem(salario, novoSalario, percentual, valorDoAumento):
  return f"O Salario que era {salario} foi aumentado em {percentual} traduzidos em R${valorDoAumento} e o salario com aumento sera de: R${novoSalario}"

print(calcAumento(int(input("Insira seu salario: \n"))))
    