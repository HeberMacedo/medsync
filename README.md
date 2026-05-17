# MedSync
![CI](https://github.com/HeberMacedo/medsync/actions/workflows/main.yml/badge.svg)

Este é o meu projeto para o BootCamp. Criei o **MedSync** para ajudar no controle de medicamentos, pensando principalmente em idosos ou pessoas que tomam muitos remédios e acabam esquecendo os horários. 

É uma ferramenta simples que roda direto no terminal (CLI), mas que foca na organização e na segurança dos dados.

## O que o programa faz:
* Cadastra o nome do remédio e o horário que deve ser tomado.
* Lista todos os agendamentos salvos para consulta rápida.
* Valida as entradas (não deixa salvar se os campos estiverem vazios).

## Tecnologias que usei:
Para o código usei **Python**. Além disso, configurei o **Pytest** para garantir que tudo funciona e o **Ruff** para manter o código limpo e padronizado. Também montei um **GitHub Actions** que roda esses testes sozinho toda vez que eu subo uma alteração.

## Como rodar o projeto:
1. Primeiro, baixe ou clone o repositório.
2. Instale as dependências com o comando: `pip install -r requirements.txt`
3. O comando padrão para rodar é `python src/main.py`.
4. Ao iniciar, o MedSync busca uma dica de saúde de uma API pública aberta e mostra essa informação no console.

## Nova funcionalidade de API pública:
* O MedSync agora consome a API gratuita `https://api.adviceslip.com/advice` para exibir uma dica de saúde sempre que a aplicação for iniciada ou quando o usuário escolher a opção de dica de saúde.
* Isso demonstra a integração com um serviço externo e garante valor adicional ao usuário sem precisar de chave de API.

## Testes e Qualidade:
Eu configurei comandos simples para testar o código:
* Para rodar os testes: `python -m pytest`
* Para ver se o código está no padrão (Lint): `python -m ruff check .`

## Deploy / Disponibilidade
* Esta é uma aplicação CLI para uso local.
* O valor extra foi entregue com a integração à API pública `https://api.adviceslip.com/advice`.
* Para usar, rode `python src/main.py` e a dica de saúde aparecerá automaticamente.

**Versão:** 1.0.0  
**Autor:** Heber Macedo
**repositório:** `https://github.com/HeberMacedo/medsync`
