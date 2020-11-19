import jsonpickle

from pydocx_text_exporter import PyDocXTextExporter

path_raw = './docs/raw/example_template.docx'
# path_raw = './docs/raw/IVOx0012 Selbstbewusstsein&Selbstvertrauen finden 2013-06.docx'
path = './docs/example_template.dart'.replace(" ", "")
# path = './docs/IVOx0012 Selbstbewusstsein&Selbstvertrauen finden 2013-06.dart'.replace(" ", "")

if __name__ == '__main__':

    exporter = PyDocXTextExporter(open(path_raw, 'rb'))

    docx = exporter.export_to_docx_dto()

    # html = exporter.export()
    # print(exporter.export())

    jsonStr = jsonpickle.encode(docx, unpicklable=False, make_refs=False)
    print(jsonStr)
    # variable_name = docx.metadata.title.replace(" ", "")
    # with open(path, 'w') as file:
    #     file.write(f"Map {variable_name} = {jsonStr};")
