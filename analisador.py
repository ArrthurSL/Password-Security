import re
try:
    import zxcvbn
    print("Biblioteca zxcvbn importada com sucesso.")
except ImportError:
    print("Erro: A biblioteca 'zxcvbn' não está instalada. Instale com 'pip install zxcvbn'.")
    exit(1)

# Restaurar a função input
input = __builtins__.input

def analisar_forca_senha(senha):
    print(f"DEBUG: Iniciando análise da senha: '{senha}'")
    
    if not senha:
        print("\n❌ A senha não pode estar em branco.")
        return
    
    try:
        print("DEBUG: Executando zxcvbn...")
        resultado_zxcvbn = zxcvbn.zxcvbn(senha)
        pontuacao = resultado_zxcvbn['score']
        print(f"DEBUG: Pontuação obtida: {pontuacao}")
    except Exception as e:
        print(f"Erro ao executar zxcvbn: {e}")
        return

    niveis_forca = {
        0: "Muito Fraca",
        1: "Fraca",
        2: "Razoável",
        3: "Forte",
        4: "Muito Forte"
    }

    print("\n" + "="*40)
    print("        RESULTADO DA ANÁLISE DE SENHA")
    print("="*40)
    
    print(f"\nForça Geral: {niveis_forca.get(pontuacao, 'Desconhecida')} ({pontuacao}/4)")
    
    sugestoes = []
    
    comprimento_ok = len(senha) >= 12
    print(f"\nCritérios de Composição:")
    if comprimento_ok:
        print(f"Comprimento (mínimo de 12 caracteres): Sim ({len(senha)})")
    else:
        print(f"Comprimento (mínimo de 12 caracteres): Não ({len(senha)})")
        sugestoes.append("Aumente a senha para pelo menos 12 caracteres.")

    if re.search(r'[a-z]', senha):
        print("Contém letras minúsculas: Sim")
    else:
        print("Contém letras minúsculas: Não")
        sugestoes.append("Inclua letras minúsculas (a-z).")

    if re.search(r'[A-Z]', senha):
        print("Contém letras maiúsculas: Sim")
    else:
        print("Contém letras maiúsculas: Não")
        sugestoes.append("Inclua letras maiúsculas (A-Z).")

    if re.search(r'[0-9]', senha):
        print("Contém números: Sim")
    else:
        print("Contém números: Não")
        sugestoes.append("Inclua números (0-9).")

    if re.search(r'[^a-zA-Z0-9]', senha):
        print("Contém caracteres especiais: Sim")
    else:
        print("Contém caracteres especiais: Não")
        sugestoes.append("Inclua caracteres especiais (ex: !@#$%).")

    if resultado_zxcvbn['feedback']['warning']:
        sugestoes.append(resultado_zxcvbn['feedback']['warning'])
    
    for sugestao in resultado_zxcvbn['feedback']['suggestions']:
        sugestoes.append(sugestao)
    
    if sugestoes:
        print("\n💡 Sugestões para Melhorar:")
        for i, sugestao in enumerate(sugestoes, 1):
            print(f"   {i}. {sugestao}")
    else:
        print("\n Excelente! Sua senha atende a todos os critérios de complexidade.")
    
    print("\n" + "="*40 + "\n")
    print("DEBUG: Análise concluída.")

# Solicitar a senha do usuário
try:
    print("DEBUG: Aguardando entrada do usuário...")
    senha = input("Insira a senha que deseja analisar: ")
    print(f"DEBUG: Senha recebida: '{senha}'")
    analisar_forca_senha(senha)
except Exception as e:
    print(f"Erro ao processar a entrada: {e}")