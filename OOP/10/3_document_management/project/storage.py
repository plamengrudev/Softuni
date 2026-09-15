from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: list[Category]=[]
        self.topics: list[Topic]=[]
        self.documents: list[Document]=[]
    
    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
    
    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
        
    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
    
    def edit_category(self, category_id: int, new_name: str):
        cat=next((c for c in self.categories if c.id==category_id),None)
        cat.edit(new_name)
    
    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        top=next((t for t in self.topics if t.id==topic_id))
        top.edit(new_topic,new_storage_folder)
    
    def edit_document(self,document_id: int, new_file_name: str):
        doc=next((d for d in self.documents if d.id==document_id),None)
        doc.edit(new_file_name)
    
    def delete_category(self, category_id: int):
        cat=next((c for c in self.categories if c.id==category_id),None)
        if cat in self.categories:
            self.categories.remove(cat)
    
    def delete_topic(self,topic_id: int):
        top=next((t for t in self.topics if t.id==topic_id))
        if top in self.topics:
            self.topics.remove(top)
    
    def delete_document(self, document_id: int):
        doc=next((d for d in self.documents if d.id==document_id),None)
        if doc in self.documents:
            self.documents.remove(doc)
    
    def get_document(self, document_id: int):
        doc=next((d for d in self.documents if d.id==document_id),None)
        return doc
    
    def __repr__(self):
        result=[]
        [result.append(d.__repr__()) for d in self.documents]
        return '\n'.join(result)


