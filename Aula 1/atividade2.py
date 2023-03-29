def calculaMedia(nota1, nota2):
    media = nota1 + nota2 / 2;
    if(media <= 3.9):
        return "E";
    if(media <= 5.9):
        return "D";
    if(media <= 7.4):
        return "C";
    if(media <= 8.9):
        return "B";
    return "A";

def verificaAprovacao(conceito):
    if(conceito == "E" or conceito == "D"):
        return "REPROVADO";
    return "APROVADO";


print(verificaAprovacao(calculaMedia(6,7)))


