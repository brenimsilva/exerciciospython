# Exercicio 01

count = 1;
PAR = [];
IMPAR = [];
INPUTS = [];
while (count < 20):
    numero = input(f"digite o {count} numero > ");
    if(numero % 2 == 0):
        PAR.append(numero);
    else:
        IMPAR.append(numero);
    INPUTS.append(numero);
    count++

print(PAR);
print(IMPAR);
print(INPUTS);
