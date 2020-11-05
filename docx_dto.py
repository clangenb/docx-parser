from typing import List

class Metadata:
    def __init__(self, name: str, date: str, location: str, type: str = '', category: str = ''):
        self.name = name
        self.date = date
        self.location = location
        self.type = type
        self.category = category


class Section:
    def __init__(self, text: str, text_style: str = ''):
        self.text = text,
        self.tex_style = text_style


class Paragraph:
    def __init__(self, content: List[Section] = None):
        if content is None:
            content = []
        self.content = content


class DocxDto:
    def __init__(self, doc_id: str = '', metadata: Metadata = None, content: List[Paragraph] = None):
        if content is None:
            content = []
        self.id = doc_id
        self.metadata = metadata
        self.content = content
