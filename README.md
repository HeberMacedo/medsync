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

**Versão:** 1.0.0  
**Autor:** Heber Macedo
**repositório:** `https://github.com/HeberMacedo/medsync`
