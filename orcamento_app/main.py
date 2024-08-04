from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import pecas 
import valor


Window.size = (400, 700)  


class OrcamentoApp(App):
    def build(self):
        self.title = 'Orçamentos do Léo'

        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)

        # Campo de seleção para Material
        self.material_spinner = Spinner(
            text='Selecione o Material',
            values=('PET', 'PVC')
        )
        layout.add_widget(self.material_spinner)

        # Campo de seleção para Espessura
        self.espessura_spinner = Spinner(
            text='Selecione a Espessura',
            values=('0.3', '0.6')
        )
        layout.add_widget(self.espessura_spinner)

        # Campo de seleção para laminação
        self.laminacao_spinner = Spinner(
            text='Com laminação',
            values=('Sim', 'Não')
        )
        layout.add_widget(self.laminacao_spinner)

        # Campos de entrada para Largura e Comprimento
        self.largura_input = TextInput(hint_text='Largura (cm)', multiline=False, input_filter='float')
        self.comprimento_input = TextInput(hint_text='Comprimento (cm)', multiline=False, input_filter='float')
        layout.add_widget(self.largura_input)
        layout.add_widget(self.comprimento_input)

        # Campo de entrada para Quantidade
        self.quantidade_input = TextInput(hint_text='Quantidade', multiline=False, input_filter='int')
        layout.add_widget(self.quantidade_input)

        # Botão para gerar orçamento
        self.gerar_button = Button(text='Gerar Orçamento', on_press=self.gerar_orcamento)
        layout.add_widget(self.gerar_button)

        # Label para exibir as informações
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)

        return layout

    def gerar_orcamento(self, instance):
        try:
            material = self.material_spinner.text
            espessura = self.espessura_spinner.text
            laminacao = self.laminacao_spinner.text
            largura = float(self.largura_input.text)
            comprimento = float(self.comprimento_input.text)
            quantidade = int(self.quantidade_input.text)
            if espessura == '0.3':
                kgdopet = valor.kgpet03
            else:
                kgdopet = valor.kgpet06
            comlaminacao = valor.comlaminacao
            total = (largura*comprimento*valor.taxa*kgdopet*valor.fator) * quantidade
            totalcomlam = ((largura*comprimento*valor.taxa*kgdopet*valor.fator) + comlaminacao) * quantidade
            formnor = f"{total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            formcom = f"{totalcomlam:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


            # Verifica se todos os campos foram preenchidos
            if material == 'Selecione o Material' or espessura == 'Selecione a Espessura' or comlaminacao == 'Com laminação' or not largura or not comprimento or not quantidade:
                self.result_label.text = 'Por favor, preencha todos os campos corretamente.'
            else:
                if laminacao == 'Sim':
                    resultado = (f'R$ {formcom}')
                else:
                    resultado = (f'R$ {formnor}')
                self.result_label.text = resultado
        except:
            self.result_label.text = 'Algum dado inválido'

if __name__ == '__main__':
    OrcamentoApp().run()
