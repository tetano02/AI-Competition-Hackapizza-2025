# Open the file apikey.txt and read the API key from it
with open("Secret Data/apikey.txt", "r") as file:
    API_KEY = file.read().strip()

from google import genai
import PyPDF2

client = genai.Client(api_key=API_KEY)

# Esempio di domanda da fare a gemini
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

# Esempio di lettura pdf e riassunto
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

pdf_path = "Hackapizza Dataset\Codice Galattico\Codice Galattico.pdf"
pdf_text = extract_text_from_pdf(pdf_path)

summary_response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"Riassumi il seguente testo: {pdf_text}",
)

print("-----------------PDF Summary---------------------------\n")
print(summary_response.text)