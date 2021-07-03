from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor
from Giveme5W1H.extractor.preprocessors.preprocessor_core_nlp import Preprocessor

preprocessor = Preprocessor('http://localhost:9000')

extractor = MasterExtractor(preprocessor=preprocessor)


doc = Document.from_text(
    text=""" Way out at the end of a tiny little town was an old overgrown garden, and in the garden was an old house, and in the house lived Pippi Longstocking

""")
# or: doc = Document(title, lead, text, date_publish)
doc = extractor.parse(doc)


# top_when = doc.get_top_answer('when').get_parts_as_text()
# print(top_when)
# top_who_answer = doc.get_top_answer('what').get_parts_as_text()
# print(top_who_answer)
# top_who_answer = doc.get_top_answer('who').get_parts_as_text()
# print(top_who_answer)
top_who_answer = doc.get_top_answer('where').get_parts_as_text()
print(top_who_answer)
