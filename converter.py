from docx2pdf import convert
import os

def docx_to_pdf(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"
    convert(input_path, output_path)
    return output_path

if __name__ == "__main__":
    input_docx = "MINI Project report Final.docx"   # MUST exist in same folder
    pdf_path = docx_to_pdf(input_docx)
    print("PDF created at:", pdf_path)
