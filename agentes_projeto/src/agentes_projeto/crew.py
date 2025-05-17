from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class AgentesProjeto():
    """AgentesProjeto crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def agent_a(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_a'],
            verbose=True
        )

    @agent
    def agent_b(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_b'], 
            verbose=True
        )
    
    @task
    def agent_a_task(self) -> Task:
        return Task(
            config=self.tasks_config['agent_a_task'], 
        )

    @task
    def agent_b_task(self) -> Task:
        return Task(
            config=self.tasks_config['agent_b_task'], 
            output_file='report.md'
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
