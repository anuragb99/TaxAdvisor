import os
import json
import PyPDF2
import google.generativeai as genai

USERFINANCIALS_FIELDS = [
    "gross_salary",
    "basic_salary",
    "hra_received",
    "rent_paid",
    "deduction_80c",
    "deduction_80d",
    "standard_deduction",
    "professional_tax",
    "tds"
]

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = "\n".join(page.extract_text() or '' for page in reader.pages)
            return text
    except Exception as e:
        print("PyPDF2 error:", e)
        return ""

def extract_userfinancials_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    gemini_api_key = os.getenv("GEMINI_API_KEY", "")
    if not gemini_api_key:
        raise Exception("Gemini API key not set in environment.")

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    prompt = (
        "Extract the following fields from this salary slip or Form 16 text. "
        "Return a JSON object with these keys: gross_salary, basic_salary, hra_received, rent_paid, "
        "deduction_80c, deduction_80d, standard_deduction, professional_tax, tds. "
        "If a value is not found, use an empty string. Here is the text:\n\n"
        f"{text}"
    )
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        # Remove code block formatting if present
        if response_text.startswith("```json"):
            response_text = response_text[7:].strip()
        elif response_text.startswith("```"):
            response_text = response_text.strip('`').strip()
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()
        print("Gemini response:", response_text[:500])
        data = json.loads(response_text)
        result = {field: data.get(field, "") for field in USERFINANCIALS_FIELDS}
        return result
    except Exception as e:
        print("Gemini extraction error:", e)
        return {field: "" for field in USERFINANCIALS_FIELDS} 