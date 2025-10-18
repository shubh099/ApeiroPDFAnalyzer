# PDF Intelligence Analysis

This is a web application that extracts tables from PDF documents, displays them with hierarchical context, and provides intelligent analysis to detect contradictions and gaps in the content.

## Features

*   **PDF Upload:** Upload PDF files through a drag-and-drop interface.
*   **Table Extraction:** Automatically extract tables from PDF documents using the Gemini 2.5 Pro model.
*   **Hierarchical Display:** Display the extracted tables in a clear and organized hierarchical format.
*   **Contradiction Detection:** Detect contradictions in the extracted data using the Gemini 2.5 Pro model.
*   **Gap Detection:** Find gaps in the extracted data using the Gemini 2.5 Pro model.
*   **Web-based Clarifications:** Get web-based clarifications for the identified contradictions and gaps using the Claude API.

## Tech Stack

*   **Backend:** Python, FastAPI
*   **Frontend:** React, Vite, Tailwind CSS
*   **AI/ML:** Google Gemini 2.5 Pro, Anthropic Claude

## Getting Started

### Prerequisites

*   Python 3.9+
*   Node.js 18+

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    ```

2.  **Install backend dependencies:**

    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd frontend
    npm install
    ```

4.  **Create a `.env` file** in the project root and add your API keys:

    ```
    GEMINI_API_KEY=your_gemini_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key
    ```

### Running the Application

1.  **Start the backend server:**

    ```bash
    cd backend
    uvicorn main:app --reload
    ```

2.  **Start the frontend development server:**

    ```bash
    cd frontend
    npm run dev
    ```

3.  Open your browser and go to `http://localhost:5173`.

## Usage

1.  Upload a PDF file using the drag-and-drop interface or the "Browse Files" button.
2.  Wait for the application to extract the tables from the PDF.
3.  View the extracted tables in the hierarchical display.
4.  Click the "Detect Contradictions" button to analyze the data for contradictions.
5.  Click the "Find Gaps" button to analyze the data for gaps.
6.  For each finding, click the "Get Clarifications" button to get a web-based clarification.

## License

This project is licensed under the MIT License.
