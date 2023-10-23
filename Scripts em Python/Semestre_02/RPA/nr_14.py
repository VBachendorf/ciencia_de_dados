import pandas as pd
import matplotlib as plt
 

dados_tempo = {
    'execucao':['1','2','4','5','6'],
    'coleta Manual':['15','4','35','46','52'],
    'coleta RPA':['1','1','10','20','12'],
    'Nome da Execução':['Verificar emails recebidos','Disparar mensagens Telegram','Enviar Relatório via Email para o Financeiro','Atulaizar dados planilha de despesas','Verificar NFe emitadas']

}

df = pd.DataFrame(dados_tempo)

# Convertendo as colunas para números inteiros
df['coleta Manual'] = df['coleta Manual'].astype(int)
df['coleta RPA'] = df['coleta RPA'].astype(int)

# Calculando o ganho de tempo
df['ganho de tempo'] = df['coleta Manual'] - df['coleta RPA']

# Encontrando a maior economia de tempo
maior_ganho_tempo = df[df['ganho de tempo'] == df['ganho de tempo'].max()]

print("Maior ganho de tempo de execução obtido após a aplicação do RPA:")
print(maior_ganho_tempo[['Nome da Execução', 'ganho de tempo']])
