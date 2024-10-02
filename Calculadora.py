import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função que realiza as operações
    def calcular(e):
        try:
            numero1 = float(campo_numero1.value)
            numero2 = float(campo_numero2.value)
            if operacao.value == "+":
                resultado.value = str(numero1 + numero2)
            elif operacao.value == "-":
                resultado.value = str(numero1 - numero2)
            elif operacao.value == "*":
                resultado.value = str(numero1 * numero2)
            elif operacao.value == "/":
                if numero2 != 0:
                    resultado.value = str(numero1 / numero2)
                else:
                    resultado.value = "Erro: Divisão por zero"
            else:
                resultado.value = "Erro: Operação inválida"
        except ValueError:
            resultado.value = "Erro: Entrada inválida"
        
        # Atualiza a tela com o resultado
        page.update()

    # Campos de entrada
    campo_numero1 = ft.TextField(label="Número 1", width=150)
    campo_numero2 = ft.TextField(label="Número 2", width=150)
    
    # Menu de seleção da operação
    operacao = ft.Dropdown(width=100, options=[
        ft.dropdown.Option("+"),
        ft.dropdown.Option("-"),
        ft.dropdown.Option("*"),
        ft.dropdown.Option("/")
    ])
    
    # Botão para calcular
    botao_calcular = ft.ElevatedButton("Calcular", on_click=calcular)
    
    # Campo para exibir o resultado
    resultado = ft.Text(value="Resultado: ", size=20)

    # Adicionando os componentes na página
    page.add(
        ft.Row([campo_numero1, operacao, campo_numero2, botao_calcular]),
        resultado
    )

# Executa a aplicação
ft.app(target=main)
