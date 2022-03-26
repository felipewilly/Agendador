'''
Aqui nesse arquivo teremos os dados de tranferencia de email
'''
from datetime import  date, timedelta
from email.message import EmailMessage
import smtplib 
import json


def alterna_datas(esc):
    if esc == 1:
        return dias(180) #Renovação licença Windows Server 
    if esc == 2:
        return dias(120) #Renovação multiplos RDP

def dias(dia):
    atual = date.today()
    nova =  atual + timedelta(days=dia)
    data = SendMail(nova.strftime('%d/%m/%Y'))
    return data.getConstroi_msg()

#Funções de tratamento email-----------------------------------
class SendMail:
    def __init__(self, nova):
        self.data = nova


    def getConstroi_msg(self):
        return self.data
    
    def abrir_arquivo(self):
        with open('server.json') as file:
            self.servico = json.load(file)
            return self.servico

    #config email
    def setExecutar_config(self):
        SMTP_SERVER = self.servico['host' ]
        SMTP_PORT =   self.servico['port' ]
        SMTP_LONGIN = self.servico['login']
        SMTP_PASS =   self.servico['senha']    

            #CONTROI EMAIL
        mensagem = EmailMessage()
        mensagem['Subject'] = "Teste Sistema Agenda Felipe"
        mensagem['From'] = SMTP_LONGIN
        mensagem['To'] = "yourMail@youmail.com"
        mensagem.set_content(f'teste de função felipe data:')
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        try:
            server.login(SMTP_LONGIN, SMTP_PASS)
            server.send_message(mensagem)
            server.quit()
            return True
        except smtplib.SMTPAuthenticationError:
            return False
        

