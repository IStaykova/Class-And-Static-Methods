from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

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
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id):
        return self.__find_object_by_id(document_id, self.documents)

    def __repr__(self):
        return "\n".join(repr(doc) for doc in self.documents)


    def __edit_object(self, object_id: int, collection: list, *new_values):
        current_object = self.__find_object_by_id(object_id, collection)
        if current_object:
            current_object.edit(*new_values )

    def __delete_object(self, object_id: int, collection: list):
        obj_to_delete = self.__find_object_by_id(object_id,collection)
        if obj_to_delete:
            collection.remove(obj_to_delete)

    @staticmethod
    def __find_object_by_id(object_id: int, collection: list):
        return next((obj for obj in collection if obj.id == object_id), None)













