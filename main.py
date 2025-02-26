# Open the file apikey.txt and read the API key from it
with open("Secret Data/apikey.txt", "r") as file:
    API_KEY = file.read().strip()

from google import genai

client = genai.Client(api_key=API_KEY)

question = "Ciao, dimmi qualcosa di interessante"

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=question,
)

print("-----------------GEMINI MODEL 2.0 FLASH----------------\n")
print("-----------------Question------------------------------\n")
print(question+"\n")
print("-----------------Response------------------------------\n")
print(response.text)