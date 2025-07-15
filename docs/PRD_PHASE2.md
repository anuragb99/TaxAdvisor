## Tax Advisor Application - Phase 2 Development Plan

### Overview
Phase 2 enables users to upload a Pay Slip or Form 16 (PDF), extract relevant financial data, and review/edit the extracted data in a form.

### Scope & Deliverables
| Phase   | Deliverable/Feature         | Acceptance Criteria                                                                 |
|---------|----------------------------|-------------------------------------------------------------------------------------|
| Phase 2 | PDF upload, extraction, and manual data review | User can upload a PDF and review/edit the auto-extracted data in a form. |

### Core Requirements
- **PDF Upload:**  
  After the user presses the “Start” button, they are taken to an upload interface to select and upload a Pay Slip or Form 16 (PDF only).
- **Data Extraction:**  
  The backend extracts relevant financial data from the uploaded PDF using:
  - PyPDF2 for text extraction
  - pytesseract (OCR) for scanned PDFs
  - pdf2image for image conversion if needed
  - **Gemini LLM** for structuring ambiguous or complex data
- **Manual Data Review:**  
  The extracted data is displayed in a single-page form on the frontend, pre-filled for the user to review and edit.
- **Form Fields:**  
  The form includes all fields required for tax calculation (as per the `UserFinancials` schema).
- **Session Handling:**  
  Each upload and review session is tracked with a unique session ID (UUID).
- **Error Handling:**  
  If extraction fails or the PDF is not in the expected format, the user receives a clear, user-friendly error message and guidance.

### Tech Stack
| Component | Technology |
|-----------|------------|
| Frontend  | Vanilla HTML, CSS, JavaScript |
| Backend   | Python (FastAPI), PyPDF2, pytesseract, pdf2image, Gemini API |
| Database  | Supabase (Cloud PostgreSQL) |

### UI/UX Principles
- After clicking “Start,” the user is guided to the PDF upload interface.
- Only PDF files are accepted for upload.
- The upload interface is simple and intuitive, with clear instructions.
- The data review form is single-page, responsive, and accessible.
- Use the “Aptos Display” font and maintain the modern, blue-accented theme.
- Proper error messages and guidance are provided for failed uploads or extraction errors.

### Acceptance Criteria
- User can upload a PDF file after pressing the “Start” button.
- The backend extracts data and returns it to the frontend.
- The user sees a single-page form pre-filled with the extracted data and can edit any field.
- The form includes all fields from the `UserFinancials` schema.
- The session is tracked with a UUID.
- Proper error handling and user feedback are implemented for upload and extraction failures. 