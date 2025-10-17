# Analisador de Senhas

Um projeto em Python para avaliar a força de senhas, desenvolvido como parte do meu aprendizado em segurança da informação. 
O programa verifica a complexidade de uma senha com base em critérios como comprimento, uso de letras maiúsculas/minúsculas, 
números e caracteres especiais, além de fornecer uma pontuação de força e sugestões de melhoria usando a biblioteca `zxcvbn`.
O projeto foi criado com a ajuda de ferramentas de apoio ao desenvolvimento, todas voltadas para o aprendizado.

## Funcionalidades
- Verifica se a senha tem pelo menos 12 caracteres.
- Analisa a presença de letras maiúsculas, minúsculas, números e caracteres especiais.
- Calcula a força da senha (de "Muito Fraca" a "Muito Forte") usando a biblioteca `zxcvbn`.
- Fornece sugestões personalizadas para melhorar a segurança da senha.
- Interface de linha de comando simples e intuitiva.

## Tecnologias Utilizadas
- **Python 3.x**: Linguagem principal do projeto.
- **zxcvbn**: Biblioteca para análise avançada de força de senhas.
- **re**: Módulo Python para expressões regulares, usado na validação de caracteres.

## Pré-requisitos
- Python 3.6 ou superior instalado.
- Biblioteca `zxcvbn` instalada.

## Instalação
1. Instale o Python a partir de [python.org](https://www.python.org/downloads/).
2. Instale a biblioteca `zxcvbn` com o comando:
   ```bash
   pip install zxcvbn
