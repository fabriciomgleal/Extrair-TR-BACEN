import calendar
from bcb import sgs
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text("Extrator de Taxa Referencial")],
    [sg.Text("Insira o mês desejado: "), sg.Input(key = 'mes', size = (15,1))],
    [sg.Text("Insira o ano desejado: "), sg.Input(key = 'ano', size = (15,1))],
    [sg.Button("Extrair"), sg.Button("Média"), sg.Button("Encerrar")]
]

janela = sg.Window('Extrator de TR', layout)
while True:
    eventos, valor = janela.read()
    mes = int(valor['mes'])
    ano = int(valor['ano'])
    if mes < 10:
        taxa_referencial = sgs.get(226, start = '20'+str(ano)+'-0'+str(mes)+'-01', end = '20'+str(ano)+'-0'+str(mes)+'-'+str(calendar.monthrange(int('20'+str(ano)), (mes))[1]))
    elif mes >= 10:
        taxa_referencial = sgs.get(226, start = '20'+str(ano)+'-'+str(mes)+'-01', end = '20'+str(ano)+'-'+str(mes)+'-'+str(calendar.monthrange(int('20'+str(ano)), (mes))[1]))
    if eventos == "Extrair":
        print(taxa_referencial)
    elif eventos == "Média":
        tamanho_dataframe = len(taxa_referencial)
        valores_taxa_referencial = taxa_referencial['226']
        soma_taxa_referencial = valores_taxa_referencial.sum()
        media = soma_taxa_referencial/tamanho_dataframe
        if mes < 10:
            sg.Popup("O valor médio da Taxa Referencial no mês 0"+str(mes)+" do ano 20"+str(ano)+" foi de "+str(media)+"%.")
        elif mes >= 10:
            sg.Popup("O valor médio da Taxa Referencial no mês "+str(mes)+" do ano 20"+str(ano)+" foi de "+str(media)+"%.")
    elif eventos == "Encerrar":
        break
