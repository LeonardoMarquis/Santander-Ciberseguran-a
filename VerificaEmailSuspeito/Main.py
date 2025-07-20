# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
import string

def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
    mensagem = mensagem.translate(str.maketrans('', '', string.punctuation)) # removendo as pontuações
    # para nao cair na ideia de que ganhe! é != de ganhe

    mensagem = mensagem.strip().lower()
    palavras_da_mensag = mensagem.split()
    resultado = "Seguro"

    for palavra_suspeita_da_vez in palavras_suspeitas:
        for palavra in palavras_da_mensag:
            if palavra_suspeita_da_vez in palavra:  # é melhor para detectar variantes, Ex desconto em descontos
                resultado = "Phishing"
                return resultado
            
    return resultado 


    # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:
    
        
            

# no caso esse "email" é um texto
email_usuario = input()



resultado = verificar_phishing(email_usuario)   

print(f"Classificação: {resultado}")