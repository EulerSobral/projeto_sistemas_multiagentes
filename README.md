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
- LangChain: Construção do bot que envia as mensagens para o empregador e o setor responsável pela documentação do serviço. Também vai ser rensponsável por consetar a legenda foto
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

## 📄 Documentação Futura
Este repositório poderá incluir:
- Diagramas de arquitetura
- Relatórios parciais de progresso
- Scripts de testes ou simulações
- Resultados e conclusões finais

