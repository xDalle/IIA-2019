'''
Alunos 						- 		Matrícula
Lucas Dalle Rocha			-		17/0016641		
Matheus Breder Branquinho	-		17/0018997

https://towardsdatascience.com/random-forest-in-python-24d0893d51c0

- Selfie dataset used:
@inproceedings{kalayeh2015selfie,
  title={How to Take a Good Selfie?},
  author={Kalayeh, Mahdi M and Seifu, Misrak and LaLanne, Wesna and Shah, Mubarak},
  booktitle={Proceedings of the 23rd Annual ACM Conference on Multimedia Conference},
  pages={923--926},
  year={2015},
  organization={ACM}
}
'''

# Pandas para manipulação dos dados
import pandas as pd
# Numpy para conversão de arrays
import numpy as np
# Pydot para visualização da árvore
import pydot
# Skicit-learn para treinamento de sets, importação de modelos
# e visualização da árvore no graphviz
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz

# Variável 'alt' recebe alternativa para geração da imagem
print()
print('Selecione a opcao desejada para geracao da imagem.')
print()
print('1- Gerar arvore completa em formato png.')
print('2- Gerar arvore com tamanho reduzido em formato png (para melhor visualizacao).')
print('3- Nao gerar imagem alguma.')

alt = input()

print()
while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()

if(alt == "2"):
	print('Insira a altura desejada da arvore para geracao da imagem (recomendado: 3).')
	alt2 = int(input())


# Lê dataset das notas e atributos das fotos e aplica "one-hot encoding"
	
features = pd.read_csv('selfie_dataset.txt')
features = pd.get_dummies(features)

# Variável 'labels' são os valores que queremos prever
labels = np.array(features['photo_rate'])
features= features.drop('photo_rate', axis = 1)
feature_list = list(features.columns)
features = np.array(features)

# Separa dados para treinamento de modelo
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = np.random)

#			TRAIN MODEL			#

print()
print('Treinando modelo...')
# Seta modelo com 1000 árvores de decisão
rf = RandomForestRegressor(n_estimators = 1000, random_state = np.random)
# Treina modelo com as datas separadas
rf.fit(train_features, train_labels)
print('Treino finalizado!')
print()

if alt == "1":	
	#			GRAPHVIZ			#
	tree = rf.estimators_[5]
	# Escolhe uma árvore da floresta
	tree = rf.estimators_[5]
	# Exporta imagem para um arquivo .dot
	export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
	# Cria grafo com arquivo .dot
	(graph, ) = pydot.graph_from_dot_file('tree.dot')
	# Gera imagem em .png
	graph.write_png('tree.png')
	print('Imagem "tree.png" gerada com sucesso!')

if alt == "2":
	#		LIMITANDO ARVORE		#
	
	# Limita altura da árvore para 'alt2'
	rf_small = RandomForestRegressor(n_estimators=1000, max_depth = alt2)
	rf_small.fit(train_features, train_labels)
	# Escolhe uma árvore da floresta
	tree_small = rf_small.estimators_[5]
	# Salva imagem como .png
	export_graphviz(tree_small, out_file = 'small_tree.dot', feature_names = feature_list, rounded = True, precision = 1)
	(graph, ) = pydot.graph_from_dot_file('small_tree.dot')
	graph.write_png('small_tree.png');
	print('Imagem "small_tree.png" gerada com sucesso!')

#		IMPORTANCIA				#
# Lista importância de atributos
importances = list(rf.feature_importances_)
# Cria tupla de atributos e sua importância
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Ordena do mais importante ao menos importante
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

print()
[print('Atributo: {:20} Importancia: {}'.format(*pair)) for pair in feature_importances];

#		    FLORESTA			#

# Nova floresta randômica com os dois atributos mais importantes
rf_most_important = RandomForestRegressor(n_estimators= 1000, random_state = np.random)
# Treinos e testes...
important_indices = [feature_list.index('white'), feature_list.index('smiling')]
train_important = train_features[:, important_indices]
test_important = test_features[:, important_indices]
# Treina a floresta randômica
rf_most_important.fit(train_important, train_labels)
# Faz predições e determina os erros
predictions = rf_most_important.predict(test_important)
errors = abs(predictions - test_labels)

# Cálculo da acurácia
mape = np.mean(100 * (errors / test_labels))
accuracy = 100 - mape
print()
print('Acuracia:', round(accuracy, 2), '%.')