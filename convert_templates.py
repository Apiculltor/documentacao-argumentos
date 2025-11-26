import os
from markitdown import MarkItDown

def convert_templates():
    source_dir = r"C:\Users\Ton\OneDrive\Área de Trabalho\Projetos\Sinc Github\documentacao-argumentos\Templates - Coleta de dados do cliente"
    dest_dir = r"C:\Users\Ton\OneDrive\Área de Trabalho\Projetos\Sinc Github\documentacao-argumentos\docs\templates\raw_analysis"
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    md = MarkItDown()
    
    for filename in os.listdir(source_dir):
        if filename.endswith(".docx") and not filename.startswith("~$"):
            source_path = os.path.join(source_dir, filename)
            dest_filename = filename.replace(".docx", ".md")
            dest_path = os.path.join(dest_dir, dest_filename)
            
            print(f"Converting {filename}...")
            try:
                result = md.convert(source_path)
                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                print(f"Saved to {dest_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    convert_templates()
