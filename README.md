Sistema MedSync

Status do Projeto: v2.0.0 (Etapa Intermediária)
🌍 Acesse o Repositório Oficial: https://github.com/HeberMacedo/medsync

Descrição do Problema Real
Muitas pessoas, especialmente idosos ou indivíduos que utilizam múltiplos medicamentos diários, enfrentam sérias dificuldades para manter a regularidade de seus tratamentos. O esquecimento de horários, a falta de registro e a ausência de orientações básicas de bem-estar podem comprometer a eficácia terapêutica e colocar a saúde em risco, gerando ansiedade tanto para o paciente quanto para seus familiares.

Proposta do Projeto
O MedSync surge como uma ferramenta objetiva e acessível para o controle de medicamentos e promoção da saúde. Através de uma interface de linha de comando (CLI) focada na simplicidade e usabilidade, o sistema resolve o problema do acompanhamento diário de tratamentos. Como diferencial para o bem-estar do usuário, o sistema agora integra uma funcionalidade ativa que busca conselhos e dicas de saúde em tempo real, transformando o gerenciamento de remédios em uma experiência informativa e humanizada.

Público-alvo
Idosos, cuidadores, familiares e pacientes que necessitam de organização rigorosa em suas rotinas de medicação e buscam um monitoramento centralizado.

----------------------------------------------------------------------
FUNCIONALIDADES DE BASE (CONSOLIDADAS NA ENTREGA INICIAL)
----------------------------------------------------------------------
- Cadastro de Medicamentos: Registro seguro do nome do remédio e do horário associado para controle diário.
- Listagem de Agendamentos: Consulta rápida, limpa e organizada de todos os remédios salvos no sistema.
- Validação de Dados: Sistema de proteção que impede campos vazios ou registros incorretos no terminal.

----------------------------------------------------------------------
NOVIDADES DA VERSÃO 2.0.0 (ADICIONADAS NA ETAPA INTERMEDIÁRIA)
----------------------------------------------------------------------
- Gestão de Demandas (GitHub Issues): Mapeamento completo de funcionalidades através da Issue #1, garantindo rastreabilidade no ciclo de desenvolvimento.
- Estratégia de Branching: Isolamento do código na ramificação obrigatória 'entrega-intermediaria-1' antes da integração definitiva no sistema.
- Integração com API Pública: Consumo em tempo real da API REST gratuita Adviceslip (https://api.adviceslip.com/advice) para exibição automatizada de dicas de saúde e autocuidado ao iniciar o programa.
- Qualidade e Testes de Integração: Implementação de testes automatizados com o ecossistema 'unittest.mock' do Python (test_obter_dica_saude_mockada) para garantir a estabilidade da esteira de testes sem depender de internet externa.
- Resolução via Pull Request: Integração contínua e fechamento automatizado de demandas via Git Merge com validação de status de testes aprovados pelo GitHub Actions.

Tecnologias Utilizadas
- Linguagem: Python 3.12
- Integração: Requests (Consumo de API REST externa)
- Testes: Pytest (Testes de unidade e testes de integração com Mock)
- Qualidade de Código: Ruff (Linting e padronização de código avançada/PEP 8)
- CI/CD: GitHub Actions (Esteira automatizada de Build e testes para cada Push ou Pull Request)

Instruções de Instalação
1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos do projeto.
3. Acesse a pasta raiz do projeto no terminal e instale as dependências necessárias:
   pip install -r requirements.txt

Instruções de Execução
Para iniciar a aplicação via terminal (CLI) e visualizar a integração com a API de dicas de saúde:
Execute o seguinte comando na raiz do projeto: 
python src/main.py

Instruções para rodar os testes
Para validar a lógica de negócios e os novos testes de integração com Mock:
Execute o comando: 
python -m pytest

Instruções para rodar o Linter (Qualidade de Código)
Para verificar a conformidade do código com os padrões de Clean Code e PEP 8:
Execute o comando: 
python -m ruff check .

Informações Adicionais
- Versão atual: 2.0.0
- Autor: Heber Americo Macedo
- Link para repositório público: https://github.com/HeberMacedo/medsync

Este projeto faz parte da disciplina de Bootcamp II da graduação em Engenharia de Software, seguindo rigorosamente os critérios de Gestão de Configuração, Qualidade de Software e Gerenciamento de Ciclo de Vida.
