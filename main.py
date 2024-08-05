from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
import valor


def mensagemerro():
	content = BoxLayout(orientation='vertical')
	error_label = Label(text="Ocorreu um erro!")
	close_button = Button(text="Fechar", size_hint_y=None, height=40)
	
	content.add_widget(error_label)
	content.add_widget(close_button)

	popup = Popup(title='Erro',
				content=content,
				size_hint=(None, None), size=(300, 200))
	
	close_button.bind(on_press=popup.dismiss)
	popup.open()


Window.size = (400, 700)


class GerenciadorTelas(ScreenManager):
	pass


class Menu(Screen):
	pass


class Config(Screen):
	def config(self):
		try:
			dados = [
				float(self.ids.kgpet03.text),
				float(self.ids.kgpet06.text),
				float(self.ids.taxa.text),
				float(self.ids.comlaminacao.text),
				float(self.ids.fator.text)]
			if len(dados) == 5:
				valor.salvar_dados_em_json(dados, 'precos.json')
			else:
				valor.carregar('precos.json')
		except:
			mensagemerro()


class Precos(Screen):
	def set_value(self):
		dados = valor.carregar('precos.json')
		p03 = float(dados[0])
		p06 = float(dados[1])
		taxa = float(dados[2])
		comlaminacao = float(dados[3])
		fator = float(dados[4])
		self.display_pet03.text = f'R$ {p03:.2f}'
		self.ids.display_pet06.text = f'R$ {p06:.2f}'
		self.ids.display_taxa.text = f'R$ {taxa:.2f}'
		self.ids.display_comlaminacao.text = f'R$ {comlaminacao:.2f}'
		self.ids.display_fator.text = f'R$ {fator:.2f}'

	def atualizar(self):
		dados = valor.carregar('precos.json')
		if dados[0] == str or dados[1] == str or dados[2] == str or dados[3] == str or dados[4] == str:
			mensagemerro()
		else:
			p03 = float(dados[0])
			p06 = float(dados[1])
			taxa = float(dados[2])
			comlaminacao = float(dados[3])
			fator = float(dados[4])
		self.ids.display_pet03.text = f'R$ {p03:.2f}'
		self.ids.display_pet06.text = f'R$ {p06:.2f}'
		self.ids.display_taxa.text = f'R$ {taxa:.2f}'
		self.ids.display_comlaminacao.text = f'R$ {comlaminacao:.2f}'
		self.ids.display_fator.text = f'R$ {fator:.2f}'


class Orcamento(Screen):
	def build(self):
		layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
		material_spinner = Spinner(
			text='Selecione o Material',
			values=('PET', 'PVC')
		)
		layout.add_widget(material_spinner)
		espessura_spinner = Spinner(
			text='Selecione a Espessura',
			values=('0.3', '0.6')
		)
		layout.add_widget(espessura_spinner)
		laminacao_spinner = Spinner(
			text='Com laminação',
			values=('Sim', 'Não')
		)
		layout.add_widget(laminacao_spinner)
		largura_input = TextInput(hint_text='Largura (cm)', multiline=False, input_filter='float')
		comprimento_input = TextInput(hint_text='Comprimento (cm)', multiline=False, input_filter='float')
		layout.add_widget(largura_input)
		layout.add_widget(comprimento_input)
		quantidade_input = TextInput(hint_text='Quantidade', multiline=False, input_filter='int')
		layout.add_widget(quantidade_input)
		gerar_button = Button(text='Gerar Orçamento', on_press=self.gerar_orcamento())
		layout.add_widget(gerar_button)
		result_label = Label(text='')
		layout.add_widget(result_label)
		return layout

	def gerar_orcamento(self):
		try:
			info = valor.carregar('precos.json')
			kgpet03 = float(info[0])
			kgpet06 = float(info[1])
			taxa = float(info[2])
			prlam = float(info[3])
			fator = float(info[4])
			material = self.ids.material_spinner.text
			espessura = self.ids.espessura_spinner.text
			laminacao = self.ids.laminacao_spinner.text
			largura = float(self.ids.largura_input.text)
			comprimento = float(self.ids.comprimento_input.text)
			quantidade = int(self.ids.quantidade_input.text)
			if espessura == '0.3':
				kgdopet = kgpet03
			else:
				kgdopet = kgpet06
			total = (largura * comprimento * taxa * kgdopet * fator) * quantidade
			totalcomlam = ((largura * comprimento * taxa * kgdopet * fator) + prlam) * quantidade
			formnor = f"{total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
			formcom = f"{totalcomlam:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

			if material == 'Selecione o Material' or espessura == 'Selecione a Espessura' or \
					laminacao == 'Com laminação' or not largura or not comprimento or not quantidade:
				self.result_label.text = 'Por favor, preencha todos os campos corretamente.'
			else:
				if laminacao == 'Sim':
					resultado = f'R$ {formcom}'
				else:
					resultado = f'R$ {formnor}'
				self.ids.result_label.text = resultado
		except:
			result_label = Label(text='')
			result_label.text = 'Algum dado inválido'


class MyApp(App):
	def build(self):
		return GerenciadorTelas()


if __name__ == '__main__':
	MyApp().run()
