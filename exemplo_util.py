from rich import print
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
from time import sleep
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel

console = Console()
prompt = Prompt()
continuar = True

while continuar == True:
    cpf = int(prompt.ask('[green]digite seu [bold]CPF[/]: [/]'))
    resposta = prompt.ask(
        f'Você digitou [red]{cpf}[/], este número está correto?')
    if resposta.lower() in ('s', 'sim'):
        print('ótimo')
        continuar = False
    elif resposta.lower() in ('n', 'não'):
        print('reiniciando...')
    else:
        print('Digite apenas [red]"s"[/] ou [red]"n"[/]')


def consultar_cpf():
    console.log('CPF sem bloqueios')
    sleep(2)
    console.log('Sem multas em financiamentos')
    sleep(2)
    console.log('Nome não encontrado no serasa')
    sleep(2)
    console.log('dados validados com sucesso')


with console.status('[green]Preenchendo formulário[/]') as status:
    consultar_cpf()

print('[green]Seu CPF está pronto para um financiamento![/]')

table = Table(title='Financiamentos Disponíveis')
table.add_column("Meses")
table.add_column("Valor")
table.add_column("Taxa de juros")

table.add_row('12x', 'R$1750,00', '7.5%')
table.add_row('36', 'R$560,00', '12.0%')
table.add_row('72x', 'R$360,00', '15.5%')

print(table)

tipo_financiamento = prompt.ask('Qual financiamento deseja contratar?',
                                choices=['12x', '36x', '72x'])

nome = input('Digite seu nome para finalizar: ')

print(
    f'[on blue][black]Parabéns [white]{nome}[/], você escolheu o financiamento de [green]{tipo_financiamento}[/][/][/]')
