from pydocx import PyDocX
from pydocx_text_exporter import PyDocXTextExporter

path = './docs/raw/IVOx0012 Selbstbewusstsein&Selbstvertrauen finden 2013-06.docx'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    html = PyDocX.to_html(path)

    exporter = PyDocXTextExporter(open(path, 'rb'))
    exporter._first_pass_export()
    exporter._post_first_pass_processing()
    exporter.first_pass = False

    print(exporter.main_document_part.document)
