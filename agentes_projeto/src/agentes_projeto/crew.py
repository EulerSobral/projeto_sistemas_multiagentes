from crewai.agents.agent_builder.base_agent import BaseAgent 
from crewai import Agent, Crew, Process, Task 
from crewai.project import CrewBase, agent, crew, task 
from typing import List 
from src.agentes_projeto.tools.image_train_tool import ImageTrain


@CrewBase
class AgentesProjeto():
    """AgentesProjeto crew"""

    agents: List[BaseAgent]
    tasks: List[Task]   

    @agent 
    def train_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['train_analyst'], 
            tools=[ImageTrain],
            verbose=True
        )
                      
    @agent 
    def image_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['image_analyst'], 
            allow_delegation=True,
            verbose=True
        )
     
    @task
    def train_image_task(self) -> Task:
        return Task(
            config=self.tasks_config['train_image_task']
        )    
    

    @task
    def image_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_analysis_task'], 
            output_file="report.md"
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AgentesProjeto crew"""
     
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
           
        )
