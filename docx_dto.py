from typing import List


class Metadata:
    def __init__(self, doc_id: str, name: str, date: str, location: str, type: str = '', category: str = ''):
        self.id = doc_id
        self.name = name
        self.date = date
        self.location = location
        self.type = type
        self.category = category


class TextSpan:
    def __init__(self, text: str, text_style: str = ''):
        self.text = text
        self.text_style = text_style


class Paragraph:
    def __init__(self, content: List[TextSpan] = None):
        if content is None:
            content = []
        self.content = content

    def append_span(self, span: TextSpan):
        self.content.append(span)


class DocxDto:
    def __init__(self, metadata: Metadata = None, content: List[Paragraph] = None):
        if content is None:
            content = []
        self.metadata = metadata
        self.content = content

    def append_paragraph(self, paragraph):
        self.content.append(paragraph)
