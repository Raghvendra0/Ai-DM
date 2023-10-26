class SymptomChecker:
    def __init__(self):
        self.knowledge_base = {
            'Common Cold': ['runny nose', 'sneezing', 'cough'],
            'Influenza': ['fever', 'muscle aches', 'fatigue', 'cough'],
            'COVID-19': ['fever', 'dry cough', 'shortness of breath'],
            'Asthma':['wheezing','coughing','a tight chest']
        }

    def diagnose(self, symptoms):
        possible_diseases = []
        for disease, required_symptoms in self.knowledge_base.items():
            if all(symptom in symptoms for symptom in required_symptoms):
                possible_diseases.append(disease)
        return possible_diseases

def main():
    checker = SymptomChecker()

    print("Welcome to the Disease Symptom Checker")
    print("Enter your symptoms (comma-separated):")
    user_input = input().split(',')

    user_symptoms = [symptom.strip() for symptom in user_input]

    if not user_symptoms:
        print("No symptoms provided. Please enter symptoms.")
        return

    possible_diseases = checker.diagnose(user_symptoms)

    if possible_diseases:
        print("Possible diseases based on your symptoms:")
        for disease in possible_diseases:
            print(f"- {disease}")
    else:
        print("No matching diseases found for your symptoms.")

if __name__ == "__main__":
    main()
