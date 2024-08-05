import json

dados = [0.8, 0.1, 1.37, 2, 3]


def salvar_dados_em_json(informacoes, precos):
	with open(precos, 'w') as arquivo:
		json.dump(informacoes, arquivo, indent=4)


def carregar(valor):
	with open(valor, 'r') as arquivo:
		dados = json.load(arquivo)
	return dados
