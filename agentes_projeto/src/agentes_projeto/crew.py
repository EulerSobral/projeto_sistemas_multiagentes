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
    def image_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['image_analyst'],
            verbose=True
        )
    
    @agent
    def technician_fiber_optic(self) -> Agent:
        return Agent(
            config=self.agents_config['technician_fiber_optic'],
            verbose=True
        )
    
    @agent
    def analyst_fiber_optic(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst_fiber_optic'],
            verbose=True
        )

    
    @task
    def image_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_analysis_task'],
        )
    
    @task
    def technician_fiber_optic_task(self) -> Task:
        return Task(
            config=self.tasks_config['technician_fiber_optic_task'], 
        )

    @task
    def analyst_fiber_optic_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyst_fiber_optic_task'], 
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
