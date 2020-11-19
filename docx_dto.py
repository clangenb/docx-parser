from typing import List


class Metadata:
    def __init__(
            self,
            doc_id: str,
            title: str,
            date: str,
            location: str,
            type: str = '',
            category: str = '',
            img: str = ''
    ):
        self.id = doc_id
        self.title = title
        self.date = date
        self.location = location
        self.type = type
        self.category = category
        self.img = img


class TextSpan:
    def __init__(self, text: str, text_style: str = ''):
        self.text = text
        self.text_style = text_style


class Paragraph:
    def __init__(self, text_spans: List[TextSpan] = None):
        if text_spans is None:
            text_spans = []
        self.text_spans = text_spans

    def append_span(self, span: TextSpan):
        self.text_spans.append(span)

    def to_text(self):
        return ''.join(
            span.text
            for span in self.text_spans
        )



class DocxDto:
    def __init__(self, metadata: Metadata = None, content: List[Paragraph] = None):
        if content is None:
            content = []
        self.metadata = metadata
        self.content = content

    def append_paragraph(self, paragraph):
        self.content.append(paragraph)

    def extract_metadata_from_content(self):
        # first item is irrelevant (`Originalskript des Vortrags`)
        self.content.pop(0)

        title = self.content.pop(0).to_text()
        loc_dat = self.content.pop(0).to_text().split(', ')
        id = self.content.pop(0).to_text()
        type = self.content.pop(0).to_text()
        category = self.content.pop(0).to_text()
        img = self.content.pop(0).to_text()

        self.metadata = Metadata(
            doc_id=id.replace('Code:', '').strip(),
            title=title,
            location=loc_dat[0],
            date=loc_dat[1],
            type=type.replace('Typ:', '').strip(),
            category=category.replace('Kategorie:', '').strip(),
            img=img
        )
