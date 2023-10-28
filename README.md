# RNA APROXIMADOR FUNÇÕES - TESTES 2 A 5

## Descrição 
Codigo de aproximadores de função com base em um 5 arquivos "testesX.npy". Realizei no mínimo três simulações de 
arquitetura de rede neural para cada um dos problemas, variando camadas e quantidade de neurônios. Cada simulação
foi executada pelo menos 10 vezes para garantir robustez, e os resultados incluem a média e o desvio padrão do erro 
final.

## Arquivo
* "main.py": script em Python para as simulações de rede neural.
* "arquivo_teste": pasta contendo os arquivos "testeX.npy".
* "graficos_simulacoes": pasta com gráficos destacando os melhores resultados das três simulações e a arquitetura 
utilizada.

# Melhores Resultados

## Teste2.npy
### Arquitetura 1

![teste2_sim1](https://github.com/vitorAugusto2/CC7711-IA/blob/main/rna_aproximador_testes/graficos_simulacoes/imagem_graficos/teste2_simulacao1.png)

    MLPRegressor(hidden_layer_sizes=(10, 10), learning_rate='adaptive', max_iter=5000, n_iter_no_change=20)
    Media = 4.74
    Desvio padrao = 7.04

### Arquitetura 2
![teste2_sim2](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste2_simulacao2.png)

    MLPRegressor(hidden_layer_sizes=(12, 12), learning_rate='adaptive',max_iter=10000, n_iter_no_change=30)
    Media = 5.05
    Desvio padrao = 5.49

### Arquitetura 3
![teste2_sim3](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste2_simulacao3.png)

    MLPRegressor(hidden_layer_sizes=(12, 12, 10), learning_rate='adaptive', max_iter=20000, n_iter_no_change=50)
    Media = 4.07
    Desvio padrao = 5.25

## Teste3.npy
### Arquitetura 1
![teste3_sim1](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste3_simulacao1.png)

    MLPRegressor(hidden_layer_sizes=(10, 10), learning_rate='adaptive', max_iter=5000, n_iter_no_change=20)
    Media = 13.79
    Desvio padrao = 24.89

### Arquitetura 2
![teste3_sim2](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste3_simulacao2.png)

    MLPRegressor(hidden_layer_sizes=(10, 10, 2), learning_rate='adaptive', max_iter=25000, n_iter_no_change=40)
    Media = 11.35
    Desvio padrao = 28.32

### Arquitetura 3
![teste3_sim3](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste3_simulacao3.png)

    MLPRegressor(hidden_layer_sizes=(12, 12, 5), learning_rate='adaptive', max_iter=30000, n_iter_no_change=50)
    Media = 8.18
    Desvio padrao = 25.69

## Teste4.npy
### Arquitetura 1
![teste4_sim1](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste4_simulacao1.png)

    MLPRegressor(hidden_layer_sizes=(10, 10), learning_rate='adaptive', max_iter=20000, n_iter_no_change=20)
    Media = 666.04
    Desvio padrao = 987.01

### Arquitetura 2
![teste4_sim2](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste4_simulacao2.png)

    MLPRegressor(hidden_layer_sizes=(10, 10, 10), learning_rate='adaptive', max_iter=50000, n_iter_no_change=30)
    Media = 261.90
    Desvio padrao = 644.68

### Arquitetura 3
![teste4_sim3](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste4_simulacao3.png)

    MLPRegressor(hidden_layer_sizes=(12, 12, 12, 4), learning_rate='adaptive', max_iter=80000, n_iter_no_change=40)
    Media = 105.83
    Desvio padrao = 286.97

## Teste5.npy
### Arquitetura 1
![teste5_sim1](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste5_simulacao1.png)

    MLPRegressor(hidden_layer_sizes=(12, 12, 12, 2), learning_rate='adaptive', max_iter=50000, n_iter_no_change=30)
    Media = 4125.76
    Desvio padrao = 161.38

### Arquitetura 2
![teste5_sim2](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste5_simulacao2.png)

    MLPRegressor(hidden_layer_sizes=(200, 200, 200, 200), max_iter=20000, n_iter_no_change=50)
    Media = 2610.81
    Desvio padrao = 857.87

### Arquitetura 3
![teste5_sim3](https://github.com/vitorAugusto2/CC7711-IA/blob/main/LAB04/graficos_simulacoes/imagem_graficos/teste5_simulacao3.png)

    MLPRegressor(hidden_layer_sizes=(400, 400, 400, 400), max_iter=20000, n_iter_no_change=50)
    Media = 2146.21
    Desvio padrao = 1365.03
