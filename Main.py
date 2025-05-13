from Utils.Agent import Cardiologist, Psychologist, Pulmonologist, MutlidisciplinaryTeam
from concurrent.futures import ThreadPoolExecutor, as_completed
import json , os

with open("Medical_Report_1.txt", "r") as file:
    medical_report = file.read()


agents = {
    "Cardiologist": Cardiologist(medical_report),
    "Psychologist":Psychologist(medical_report),
    "Pulmonologist":Pulmonologist(medical_report)
}

def get_reponse(agent_name, agent):
    response = agent.run()
    return agent_name, response

responses = {}

with ThreadPoolExecutor() as executor:
    futures = {executor.submit(get_reponse, name, agent): name for name, agent in agents.items()}

    for future in as_completed(futures):
        agent_name, response = future.result()
        responses[agent_name] = response
    



team_agents = MutlidisciplinaryTeam(
    cardiologist_report=responses["Cardiologist"],
    psychologist_report=responses["Psychologist"],
    pulmonologist_report=responses["Pulmonologist"]
)


final_diagnosis = team_agents.run()
txt_output_path = "results/final_diagnosis.txt"

os.makedirs(os.path.dirname(txt_output_path), exist_ok=True)


with open(txt_output_path, "w") as txt_file:
    txt_file.write(final_diagnosis)


print(f"Final Diagnosis has been saved to {txt_output_path}")