'''
Arquivo: libs.yagmail_sender.py
Descrição: Cliente e-mail do gmail com yagmail
Autores: Malki-çedheq Benjamim,
Criado em: 25/08/2022
Atualizado em: 19/02/2022
'''

import yagmail


def envia_email(to: list = [],
                cc: list = [],
                bcc: list = [],
                subject: str = "",
                contents: str = "",
                attachments: list = []
                ):
    ''' 
        to: list = [lista de emails destinatários],
        cc: list = [lista de emails copia],
        bcc: list = [lista de emails com copia oculta],
        subject: str = "assunto do email",
        contents: str = "conteudo textual do email aceita marcação html",
        attachments: list = [lista de anexos ao email]
    '''
    try:
        yag = yagmail.SMTP(user="jairo.marques1309@gmail.com",
                           oauth2_file="./ex19_flask/libs/ouath2_creds_jairomarques"
                           )
        yag.send(to=to,
                 cc=cc,
                 bcc=bcc,
                 subject=subject,
                 contents=contents,
                 attachments=attachments
                 )
        return {'message': 'sucesso'}
    except:
        return {'message': 'erro'}
