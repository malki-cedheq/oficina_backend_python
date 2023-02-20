''' Cliente e-mail do gmail com yagmail'''
import yagmail


def envia_email(to: list = [],
                cc: list = [],
                bcc: list = [],
                subject: str = "",
                contents: str = "",
                attachments: list = []
                ):
    ''' '''
    try:
        yag = yagmail.SMTP(user="doctorstrange1987@gmail.com",
                           oauth2_file="./ex19_flask/libs/oauth2_creds_doctorstrange.json"
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
