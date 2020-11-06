import jsonpickle

from pydocx_text_exporter import PyDocXTextExporter

path = './docs/raw/IVOx0012 Selbstbewusstsein&Selbstvertrauen finden 2013-06.docx'

if __name__ == '__main__':

    exporter = PyDocXTextExporter(open(path, 'rb'))

    jsonStr = jsonpickle.encode(exporter.export_to_docx_dto(), unpicklable=False, make_refs=False)
    print(jsonStr)
    # print(exporter.export())
