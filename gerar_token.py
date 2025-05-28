from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

# Escopo de permissão: enviar e-mails pelo Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gerar_token():
    # Caminho para o seu arquivo client_secret.json
    caminho_credenciais = 'ID Cliente ID secrete Json.json'
  # Ajuste conforme o nome do seu arquivo

    # Inicializa o fluxo de autenticação
    flow = InstalledAppFlow.from_client_secrets_file(
        caminho_credenciais, SCOPES
    )
    
    # Executa o fluxo → abrirá o navegador
    creds = flow.run_local_server(port=0)
    
    # Salva o token gerado
    with open('token_gmail.pickle', 'wb') as token:
        pickle.dump(creds, token)
    
    print('✅ Token OAuth2 gerado e salvo com sucesso!')

if __name__ == '__main__':
    gerar_token()

