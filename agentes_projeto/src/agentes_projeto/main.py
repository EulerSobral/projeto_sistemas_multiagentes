#!/usr/bin/env python
import sys
import warnings
from agentes_projeto.crew import AgentesProjeto

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    
    try:
        AgentesProjeto().crew().kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'detections': analyze_image(train_model(),r'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\train\\', 'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\val\\poste_fibra01.jpg'),
    }
    try:
        AgentesProjeto().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgentesProjeto().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'detections': analyze_image(train_model(), r'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\train\\', 'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\val\\poste_fibra01.jpg'),
    }
    
    try:
        AgentesProjeto().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
