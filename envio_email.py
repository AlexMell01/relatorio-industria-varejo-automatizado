import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_email(destinatario, assunto, corpo, arquivo_anexo):
    remetente = 'alexasc.automacao@gmail.com'
    senha_app = 'rfdwxwuqfwtvdqcb'  # Senha de app do Gmail (sem espaços)

    # Monta o e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Anexo
    with open(arquivo_anexo, 'rb') as f:
        parte = MIMEApplication(f.read(), Name=arquivo_anexo)
    parte['Content-Disposition'] = f'attachment; filename="{arquivo_anexo}"'
    mensagem.attach(parte)

    # Envia o e-mail via servidor SMTP do Gmail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha_app)
        servidor.send_message(mensagem)
        servidor.quit()
        print(f"✅ E-mail enviado com sucesso para {destinatario}!")
    except Exception as e:
        print(f"❌ Falha ao enviar e-mail: {e}")

# Exemplo de uso
enviar_email(
    destinatario='mellfuture@gmail.com',
    assunto='Relatório Comercial Automatizado - Indústria → Varejo',
    corpo='Prezado(a),\n\nSegue em anexo o relatório automatizado com análise de vendas por categoria, canal e desempenho.\n\nAtenciosamente,\nAlex Sandro',
    arquivo_anexo='relatorio_comercial.pdf'
)

