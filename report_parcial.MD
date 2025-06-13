# 📄 Relatório de Acompanhamento de Projeto — Sistemas Multiagente

> Preencha com atenção. Este relatório tem o objetivo de **organizar o pensamento, identificar bloqueios e alinhar os próximos passos do seu projeto**.

---

## 🧠 1. Visão Geral do Projeto

- **Título do Projeto**:  
  Auditor da realização de um serviço de instalação de fibra óptica

- **Integrantes da Equipe**:  
  - Euler (visão computacional e interação do agente com as imagens)
  - Edriel (Construção do ChatBot que será utilizado no Whatsapp ou Discord)
  - Felipe (Construção da engenharia de prompt dos agentes e interação deles)

- **Resumo em uma frase**:  
  O primeiro agente vai analisar uma imagem e perceber se ela atende os requisitos exigidos pela empresa de Internet, esses requisitos são a presença da etiqueta amarela da empresa no cabo de fibra óptica do poste e a visualização das informações da etiqueta. Além disso, esse agente também pode receber um texto contendo informações sobre a localização do poste, o tipo, data, hora e localização do serviço realizado. 
  O segundo agente vai enviar uma mensagem para o ChatBot informando se a foto e as informações fornecidas ao primeiro agente estão atendendo as normas exigidas pela empresa. 
  O ChatBot vai enviar uma mensagem informando ao colaborador se a foto atende ou não os requisitos solicitados. 

---

## ⚙️ 2. Arquitetura Atual

- **Quantos agentes existem no sistema atualmente?**  
  Apenas 3 agentes: `image_analyst`, `technician_fiber_optic` e `analyst_fiber_optic`

- **Função principal de cada agente:**  
  OBS: O agente do ChatBot ainda não foi implementado!

  image_analyst: recebe e analisa imagens do poste;  
  technician_fiber_optic: analisa as informações da imagem verificando a fibra óptica instalada e o seu tipo; 
  technician_fiber_optic: analisa as informações da imagem verificando a fibra óptica instalada e o seu tipo; 
  analyst_fiber_optic_task: escreve um relatório sobre o trabalho do técnico de fibra óptica 



- **Eles interagem entre si? Como?**  
  Ainda não. A ideia futura é criar um agente de parsing separado e outro de curadoria de resposta.

- **Já existe algum ambiente de simulação/teste?**  
  Ainda não, por enquanto só foi testado a interação das imagens entre os agentes. Problemas foran verificados e precisam ser corrigidos, o pricipal deles é que o agente informa que não consiguiu visualizar a imagem fornecida.

---

## ✅ 3. Avanços Concretos

- Treinamento das imagens, utilizando a Yolo, já foi iniciado 
- Interação do agente com a imagem já foi inciada.

---

## 🧱 4. Dificuldades Enfrentadas

- As respostas geradas pelo agente ainda são muito genéricas ou irrelevantes.
- O treinamento do modelo que faz uso da visão computacional ainda está fraco 
- O primeiro agente não consegue visualizar as informações da imagem, ainda não descobri o motivo. Mas suspeitamos que está ocorrendo erro na visualização do diretório onde a imagem foi salva, problemas na engenharia de prompt e o modelo de LLM utilizado apresenta limitações para lidar com imagens

---

## 🛠️ 5. Estratégias de Superação

- Perceber se existe problemas na visualização do diretório onde a imagem está salva e caso esse seja o problema realiza eventuais concertos 
- Perceber se existe problemas na engenharia de prompt e caso esse seja o problema modificar o prompt para que ele seja eficiente 
- Trocar a LLM utilizada por uma com melhor desempenho  


---

## 🎯 6. Próximos Passos

- Construir a estrutura do segundo agente (responsável por verificar se a imagem está nos conformes ou não) e sua comunicação com o agente que analisa as imagens
- Efetuar uma melhor engenharia de prompt 
- Desenvolver o ChatBot
---

## 📢 7. Pedido de Ajuda

- Precisamos de ajuda para uma melhor abordagem na parte do treinamento de visão computacional, como, por exemplo, uma recomendação de materiais da área para realizar estudos 
- Estudos na parte de Engenharia de Prompt 

---
