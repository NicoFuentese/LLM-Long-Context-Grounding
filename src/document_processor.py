import fitz  # PyMuPDF
import re

def clean_text(text: str) -> str:
    """Elimina caracteres de control nulos o problemáticos que puedan romper el JSON payload."""
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

def extract_text(file_bytes: bytes, filename: str) -> str:
    """Extrae texto de PDFs y TXTs de forma eficiente."""
    text = ""
    if filename.lower().endswith('.pdf'):
        # Abrir el PDF desde memoria
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        for page in doc:
            text += page.get_text("text") + "\n"
        doc.close()
    elif filename.lower().endswith('.txt'):
        text = file_bytes.decode('utf-8')
    
    return clean_text(text)

def build_xml_context(uploaded_files) -> str:
    """
    Toma una lista de archivos de Streamlit, extrae su contenido 
    y los envuelve en etiquetas XML para anclaje de contexto.
    """
    xml_output = "<documentos>\n"
    for idx, file in enumerate(uploaded_files, start=1):
        file_bytes = file.read()
        filename = file.name
        content = extract_text(file_bytes, filename)
        
        xml_output += f'  <documento id="{idx}" nombre="{filename}">\n'
        xml_output += f'    {content}\n'
        xml_output += f'  </documento>\n'
    xml_output += "</documentos>"
    
    return xml_output