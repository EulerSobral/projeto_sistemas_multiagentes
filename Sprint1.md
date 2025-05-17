# Sprint 1 

Nesse primeiro momento, vamos exemplificar os agentes utilizados no projeto utilizando o CrewAI. Mais especificamente, estamos utilizando como base o exemplo do código apresentando na aula da disciplina de Sistemas Multiagentes mininistrada no dia 16/05/2025. 

Dividimos o projeto em dois agentes, o agente A e o agente B. O agente A tem conhecimentos técnicos sobre redes de fibra óptica e o agente B vai analisar as informações fornecidas pelo agente A e fornecer pontos positivos e negativos sobre as mesmas.  

O agente A vai fazer uma requisição á LLM, Gemini, sobre redes de fibra óptica 

O próximo passo desse projeto é utilizar visão computacional para analisar imagens da instalação de redes de fibra óptica e indicar se a instalação foi feita com as normas estabelecidas. Para isso, vamos utlizar OpenCV com o intuito de desenvolver um agente que analise a imagem. Depois disso, vamos pegar a informação e enviar para outro agente que vai analisar e dizer se a informação é correta ou não. Em um primeiro momento, o grupo vai testar se é necessária a utilização do CrewAI no desenvolvimento desse agente. Caso não seja necessário o uso de CrewAI, vamos analisar o uso de ferramentas para a construção desse e outros agentes do projeto

# Ferramentas utilizadas na Sprint 1 

Python 13.13.1 
uv 0.7.5 
crewai 0.120.1 
Sistema Operacional Windows 10
