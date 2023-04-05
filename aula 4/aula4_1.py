import pandas as pd
import matplotlib.pyplot as plt

dt = {
    "nome": ["Breno", "Cristiano", "Patrik"],
    "idade": [29, 30, 32],
    "data_nascimento": ["15/05/1993", "10/03/1990", "12/01/1876"]
}

df = pd.DataFrame(dt);

tabela_df = pd.read_excel("aula 4/tabela_aula.xlsx")

dados = {
    'x': [1,2,3,4,5,6],
    'Y1': [120,110,130,145,118,125],
    "Y2": [95,54,86,77,90,81]
}

dados_df = pd.DataFrame(dados);
plt.plot(dados);

plt.show();

print(tabela_df);