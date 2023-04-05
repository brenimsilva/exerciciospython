import pandas as pd
import matplotlib.pyplot as plt

#Exercicio aula 04

dados = {
    'X': [1,2,3,4,5,6],
    'Y1': [120,110,130,145,118,125],
    "Y2": [95,54,86,77,90,81]
}

dados_df = pd.DataFrame(dados);
plt.plot(dados_df);

plt.show();

#Bonus lendo tabela do excel
tabela_df = pd.read_excel("aula 4/tabela_aula.xlsx")
print(tabela_df);