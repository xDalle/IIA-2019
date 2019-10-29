# driver.py

'''		Cria a engine	'''
from pyke import knowledge_engine

engine = knowledge_engine.engine(__file__)

engine.activate('rule')
engine.get_kb('knowledge')

'''		Contadores da valoração de cada doença	'''
ctd_dengue = 0
ctd_zika = 0
ctd_chikungunya = 0

'''		FEBRE	'''

print()
print("Insira grau e duracao da febre: ")
print("1- Acima de 38ºC (4 a 7 dias)")
print("2- Sem febre ou subfebril 38ºC (1-2 dias subfebril)")
print("3- Febre alta > 38ºC (2-3 dias)")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.febre(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.febre(2, $doenca)')
	ctd_zika+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.febre(3, $doenca)')
	ctd_chikungunya+= 1

'''		MANCHAS NA PELE	'''

print()
print("Insira intervalo mais proximo de aparicao de manchas na pele: ")
print("1- A partir do 1º ou 2º dia")
print("2- A partir do 3º dia")
print("3- A partir do 4º ou 5º dia")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.mancha(2, $doenca)')
	ctd_zika+= 0.95
	res, _ = engine.prove_1_goal('knowledge.mancha(3, $doenca)')
	ctd_chikungunya+= 0.5

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.mancha(3, $doenca)')
	ctd_chikungunya+= 0.5
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.mancha(3, $doenca)')
	ctd_chikungunya+= 0.5
	res, _ = engine.prove_1_goal('knowledge.mancha(1, $doenca)')
	ctd_dengue+= 0.4

'''		DOR NOS MÚSCULOS	'''

print()
print("Insira nivel de dor nos musculos: ")
print("1- Nivel alto")
print("2- Nivel medio")
print("3- Nivel baixo")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.musculo(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.musculo(2, $doenca)')
	ctd_zika+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.musculo(3, $doenca)')
	ctd_chikungunya+= 1
	
	
'''		DOR NA ARTICULAÇÃO	'''

print()
print("Insira nivel de dor nas articulacoes: ")
print("1- Nivel baixo")
print("2- Nivel medio")
print("3- Nivel alto")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.articulacao(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.articulacao(2, $doenca)')
	ctd_zika+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.articulacao(3, $doenca)')
	ctd_chikungunya+= 1
	

'''		INTENSIDADE DA DOR ARTICULAR	'''

print()
print("Insira intensidade da dor articular: ")
print("1- Leve")
print("2- Moderada")
print("3- Intensa")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.dorarticular(1, $doenca)')
	ctd_dengue+= 1
	res, _ = engine.prove_1_goal('knowledge.dorarticular(2, $doenca)')
	ctd_zika+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.dorarticular(2, $doenca)')
	ctd_zika+= 1
	res, _ = engine.prove_1_goal('knowledge.dorarticular(3, $doenca)')
	ctd_chikungunya+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.dorarticular(3, $doenca)')
	ctd_chikungunya+= 1
	

'''		EDEMA DA ARTICULAÇÃO	'''

print()
print("Insira presenca de edema da articulacao: ")
print("1- Nao possui")
print("2- Possui, de leve intensidade")
print("3- Possui, de moderada a elevada intensidade")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.edema(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.edema(2, $doenca)')
	ctd_zika+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.edema(3, $doenca)')
	ctd_chikungunya+= 1
	
'''		CONJUNTIVITE	'''

print()
print("Insira presenca de conjuntivite: ")
print("1- Nao possui")
print("2- Possui")

alt = input()

while(alt < "1" or alt > "2"):
	print("Insira uma opcao valida (1 - 2): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.conjuntivite(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.conjuntivite(2, $doenca)')
	res, _ = engine.prove_1_goal('knowledge.conjuntivite(3, $doenca)')
	ctd_zika+= 0.7
	ctd_chikungunya+= 0.3
	
'''		DOR DE CABECA	'''

print()
print("Insira frequencia e intensidade da dor de cabeca: ")
print("1- Alta")
print("2- Moderada")

alt = input()

while(alt < "1" or alt > "2"):
	print("Insira uma opcao valida (1 - 2): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.cabeca(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.cabeca(2, $doenca)')
	ctd_zika+= 1
	res, _ = engine.prove_1_goal('knowledge.cabeca(3, $doenca)')
	ctd_chikungunya+= 1
	
'''		COCEIRA		'''

print()
print("Insira intensidade da coceira: ")
print("1- Leve")
print("2- Moderada ou intensa")

alt = input()

while(alt < "1" or alt > "2"):
	print("Insira uma opcao valida (1 - 2): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.coceira(1, $doenca)')
	ctd_dengue+= 1
	res, _ = engine.prove_1_goal('knowledge.coceira(3, $doenca)')
	ctd_chikungunya+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.coceira(2, $doenca)')
	ctd_zika+= 1
	
'''		HIPERTROFIA	GANGLIONAR	'''

print()
print("Insira frequencia de hipertrofia ganglionar: ")
print("1- Leve")
print("2- Moderada")
print("3- Intensa")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.hipertrofia(1, $doenca)')
	ctd_dengue+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.hipertrofia(3, $doenca)')
	ctd_chikungunya+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.hipertrofia(2, $doenca)')
	ctd_zika+= 1
	
'''		DISCRASIA HEMORRÁGICA		'''

print()
print("Insira frequencia de discrasia hemorragica: ")
print("1- Ausente")
print("2- Leve")
print("3- Moderada")

alt = input()

while(alt < "1" or alt > "3"):
	print("Insira uma opcao valida (1 - 3): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.discrasia(2, $doenca)')
	ctd_zika+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.discrasia(3, $doenca)')
	ctd_chikungunya+= 1
	
if alt == "3":
	res, _ = engine.prove_1_goal('knowledge.discrasia(1, $doenca)')
	ctd_dengue+= 1
		
'''		ACOMETIMENTO NEUROLÓGICO	'''

print()
print("Insira presenca de acometimento neurologico: ")
print("1- Nao possui")
print("2- Possui")

alt = input()

while(alt < "1" or alt > "2"):
	print("Insira uma opcao valida (1 - 2): ")
	alt = input()
	
if alt == "1":
	res, _ = engine.prove_1_goal('knowledge.acometimento(1, $doenca)')
	ctd_dengue+= 1
	res, _ = engine.prove_1_goal('knowledge.acometimento(3, $doenca)')
	ctd_chikungunya+= 1

if alt == "2":
	res, _ = engine.prove_1_goal('knowledge.acometimento(2, $doenca)')
	ctd_zika+= 1
		
'''		Relaciona a valoração da chance de ser cada doença
		em relação ao total e obtém sua porcentagem				'''
		
soma = ctd_dengue + ctd_zika + ctd_chikungunya

print()
print("Diagnostico: ")
print("Chance do paciente estar com dengue:" , round(((ctd_dengue/soma) * 100), 2) , "%")
print("Chance do paciente estar com zika:" , round(((ctd_zika/soma) * 100), 2) , "%")
print("Chance do paciente estar com chikungunya:" , round(((ctd_chikungunya/soma) * 100), 2) , "%")

'''			RESETA ENGINE		'''

engine.reset()