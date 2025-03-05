import requests #importowanie usługi 

def deepai_chatbot(prompt, api_key):
    url = "https://api.deepai.org/api/text-generator"
    headers = {"api-key": api_key}
    data = {"text": prompt}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("output", "Brak odpowiedzi.")
    else:
        return f"Błąd: {response.status_code} - {response.text}"

if __name__ == "__main__":
    API_KEY = "wpisz kod api"  # klucz api z ai
    print("Czatbot DeepAI - wpisz 'exit', aby zakończyć.")
    while True:
        user_input = input("Ty: ")
        if user_input.lower() == "exit":
            print("Czatbot: Do zobaczenia!")
            break
        response = deepai_chatbot(user_input, API_KEY)
        print(f"Czatbot: {response}")
