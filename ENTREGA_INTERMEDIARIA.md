# Entrega intermediaria - MedSync

Aluno: Heber Macedo

Repositorio: https://github.com/HeberMacedo/medsync

Deploy: https://hebermacedo.github.io/medsync/

Branch da entrega: `entrega-intermediaria`

API publica usada: ViaCEP

## Resumo da entrega

Nesta etapa, o projeto MedSync foi evoluido a partir da entrega inicial. A branch `main` ficou com a versao inicial do projeto, enquanto a branch `entrega-intermediaria` recebeu as novas funcionalidades.

O projeto agora tem integracao com a API publica ViaCEP para consultar enderecos por CEP. Essa consulta foi usada no contexto do MedSync para simular um endereco de entrega ou retirada de medicamentos.

Tambem foi criada uma versao web simples publicada pelo GitHub Pages, para que o avaliador consiga acessar e testar a aplicacao pelo navegador.

## Funcionalidades implementadas

- Cadastro de medicamento e horario.
- Listagem dos medicamentos cadastrados.
- Consulta de endereco por CEP usando a API ViaCEP.
- Versao CLI em Python.
- Versao web publicada no GitHub Pages.
- Teste de integracao com resposta mockada da API.

## Testes e qualidade

Comandos usados para validar o projeto:

`python -m pytest`

Resultado:

`7 passed`

`python -m ruff check .`

Resultado:

`All checks passed!`

## Texto sugerido para a Issue

Titulo:

`Integrar API ViaCEP ao MedSync`

Descricao:

`Nesta entrega intermediaria, o objetivo e integrar o MedSync com uma API publica externa. A API escolhida foi a ViaCEP, que permite consultar enderecos a partir de um CEP. Essa funcionalidade agrega valor ao projeto porque pode apoiar a entrega ou retirada de medicamentos. A implementacao tambem inclui testes de integracao, atualizacao do README e uma versao web publicada pelo GitHub Pages.`

## Texto sugerido para o Pull Request

Titulo:

`Entrega intermediaria - integracao com ViaCEP`

Descricao:

`Closes #NUMERO_DA_ISSUE`

`Esta PR adiciona a entrega intermediaria do projeto MedSync. Foram implementadas a integracao com a API publica ViaCEP, testes de integracao com resposta mockada, atualizacao do README e uma versao web publicada no GitHub Pages para avaliacao pelo navegador.`
