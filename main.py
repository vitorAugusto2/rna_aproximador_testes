import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor


print(f"+----------------------------+\n"
      f"      Carregando arquivo      \n"
      f"+----------------------------+\n")
arquivo = np.load("arquivo_teste/teste5.npy")  # carregue o arquivo desejado
x = arquivo[0]
y = np.ravel(arquivo[1])

n_execucao = 10
melhor_resultado = 1
simulacao = []

for i in range(n_execucao):
    regr = MLPRegressor(hidden_layer_sizes=(400, 400, 400, 400),
                        max_iter=20000,
                        activation='relu',  # {'identity', 'logistic', 'tanh', 'relu'},
                        solver='adam',
                        learning_rate='constant',
                        n_iter_no_change=50)

    print(f"Treinando RNA")
    regr = regr.fit(x, y)

    print(f"Predito")
    y_est = regr.predict(x)

    media = np.mean(regr.loss_curve_)
    dp = np.std(regr.loss_curve_)
    print(f"Execucao: {i+1}\n"
          f"Media = {media:.2f}\n"
          f"Desvio padrao = {dp:.2f}\n")

    simulacao.append({"media": media,
                      "dp": dp,
                      "y_est": y_est,
                      "regre.loss_curve_": regr.loss_curve_})


simulacao.sort(key=lambda result: result["media"])
melhor_resultado = simulacao[:melhor_resultado]


print(f"+----------------------------+\n"
      f"       Melhor resultado       \n"
      f"+----------------------------+\n")
for i, result in enumerate(melhor_resultado):
    media = result["media"]
    dp = result["dp"]

    print(f"Resultado {i + 1}:\n"
          f"Media = {media:.2f}\n"
          f"Desvio padrao = {dp:.2f}\n")

    plt.figure(figsize=[14, 7])

    # plot curso original
    plt.subplot(1, 3, 1)
    plt.plot(x, y)
    plt.title("Gráfico Curso Original")

    # plot aprendizagem
    plt.subplot(1, 3, 2)
    plt.plot(result["regre.loss_curve_"])
    plt.title("Gráfico Aprendizagem")

    # plot regressor
    plt.subplot(1, 3, 3)
    plt.plot(x, y, linewidth=1, color="yellow")
    plt.plot(x, result["y_est"], linewidth=2)
    plt.title("Gráfico Regressor")

    plt.show()

print(f"+----------------------------+\n"
      f"         Arquitetura          \n"
      f"+----------------------------+\n"
      f"\n{regr}")
