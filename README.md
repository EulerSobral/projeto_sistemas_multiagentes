# Nome do Projeto
> Auditor da realização de um serviço de instalação de fibra óptica

## 👨‍🎓 Integrantes
- Euler Pereira Sobral
- Edriel José Pacífico Gama
- Felipe Luiz de Lima

## 💡 Ideia Principal
A ideia consiste no desenvolvimento de um agente que recebe a imagem de um trabalho realizado em uma rede elétrica, o agente precisa checar se a foto segue o padrão exigido e se ele comprova o trabalho realizado pelo colaborador, a comprovação do trabalho consiste na visualização de uma etiqueta amarela no fio do poste, essa etiqueta mostra que o cabo de fibra óptica foi devidamente instalado no poste pelo colaborador da empresa. Se for possível ajustar a legenda da imagem para condizer com padrão, o agente faz o ajuste. Caso contrário, ele envia para o Whatsapp do colaborador uma mensagem informando que a imagem não está no padrão aceito. 
	A legenda da imagem deve conter os dados da localização do poste, como por exemplo, as coordenadas e o endereço, também é necessário a data e hora do serviço realizado. Caso esses dados não estejam na norma proposta pela empresa, o agente deve fazer a edição desses dados.


## 🎯 Objetivos
- Melhorar a eficência dos serviços prestados pela empresa
- Fazer a auditoria em tempo hábil se o serviço foi realizado com sucesso
- Perceber se o serviço seguiu as normas técnicas da empresa
- Deixar a foto no padrão exigido pela empresa
- Diminuir a auditoria humana para com a realização da instalação de fibra óptica em postes.
Algumas pessoas precisam analisar a foto enviada pelo técnico quando este finaliza o seu serviço, além de demorar um certo tempo para perceber que o trabalho do técnico não seguiu
as normas exigidas, esse pessoal perde tempo fazendo este serviço e com isso atrasa ou não realizada demandas da empresa


## 👥 Público-Alvo
Este projeto visa as empresas de provedores de Internet

## 🤖 Agentes Envolvidos
Liste os agentes que existirão no sistema e suas funções.
Exemplo:
- Agente A: verifica se a foto está nos padrões exigidos pela empresa, como, por exemplo, verifica se a etiqueta que precisa estar no cabo de fibra óptica foi realmente colocada
  pelo técnico

- Agente B: verfica se a foto está nos padrões exigidos. Caso não esteja, envia uma mensagem para o técnico pedindo que o mesmo retire outra foto, se o erro foi só na legenda da foto
  um terceiro agente, Agente C, faz a edição da legenda. Se a foto estiver nos padrões exigidos, o chamado da realização da instalação do cabo é encerrada e a foto é enviada para o setor
  responsável pea documentação
  

## 🧱 Tecnologias Pretendidas
- Python
- CrewAI: Construção do bot que envia as mensagens para o empregador e o setor responsável pela documentação do serviço. Também vai ser rensponsável por consetar a legenda foto
- OpenCV: vai ser o responsável por analisar se a foto está nos padrões exigidos pela empresa, como, por exemplo, identificar se a etiqueta da instalção da fibra óptica foi colocada no cabo
- Ferramentas para teste, simulação, visualização, etc.


## 📦 Entradas e Saídas Esperadas
**Entradas:**
- Recebe uma imagem

**Saídas:**
- Um texto informando que o colaborador concluiu o serviço, caso este tenha realizado seu trabalho nos padrões exigidos
- Um texto pedindo que o colaborador tire outra foto, caso este não tenha realizado seu trabalho nos padrões exigidos

## 🔁 Interação entre os Agentes
- Agente A analisa a foto e envia para o Agente B 
- Agente B faz a auditoria da imagem. Caso a imagem não esteja nos padrões exigidos, envia uma mensagem para o colaborador pedindo que retire outra foto, caso contrário, envia uma mensagem dizendo que o seu serviço foi encerrado com sucesso
- Caso o erro seja no ná legenda, o Agente B envia a imagem para o Agente C. O Agente C vai editar a legenda e informar ao colaborador que o seu serviço foi concluído

## 🗂️ Organização e Planejamento do Projeto
O progresso deste projeto será monitorado através do **GitHub Projects**.e p

> Acesse a aba "Projects" do repositório para acompanhar:
- Tarefas pendentes
- Tarefas em andamento
- Tarefas concluídas

Cada integrante deve ser responsável por pelo menos uma tarefa no quadro.
Use etiquetas (labels) e comentários para detalhar o andamento e as decisões.

## 📌 Status Inicial do Projeto
- [ ] Ideia discutida e validada com o professor
- [ ] Estrutura básica do repositório criada
- [ ] Quadro no GitHub Projects criado
- [ ] Primeiras tarefas definidas e atribuídas

## 📄 Documentação  

Para o projeto funcionar, é necessário que você utilize alguma LLM por meio de uma api fornecida pela LLM, como, por exemplo, a api do chat gpt. Nesse projeto, 
eu utilize a LLM gemini/gemini-2.0-flash-lite-001, mas você pode se sentir livre em utilizar outra LLM do seu gosto para rodar o projeto. 
Na data em que desenvolvi esse projeto, 20/05/2025, fiz uso da API do Gemini disponibilizada gratuitamente pelo Google. Para acessar a chave da api do Google, [clique aqui](https://aistudio.google.com/0)

Com a sua chave da api, acesse o arquivo do projeto `.env` e cole cahve  da api no seguinte espaço `GEMINI_API_KEY=DIGITE SUA API KEY` 

Caso não tenha o crewai instalado em sua máquina, siga os seguintes procedimentos. 
- Instale o uv
    No MacOs ou Linux: ```bash curl -LsSf https://astral.sh/uv/install.sh | sh ```
    Caso seu sistema não utilize o curl, utilize o seguinte comando ```bash wget -qO- https://astral.sh/uv/install.sh | sh```
    No Windows: ```bash powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```
- Rodando o projeto
- **OBS: Antes de rodar o projeto, verifique se a sua versão do Python é maior ou equivalente a 3.10**
- Para fazer uso dos comandos abaixo é necessário que você abra o terminal na pasta agentes_projeto.
- O comando crewai install só é necessário ser executado na primeira vez que o projeto for utilzado ou caso você deseje atualizar a versão do CrewAI 

```bash
crewai install
```

```bash
crewai run
```
