import json


class FileStorage:
    '''
        This class serializes instances to a JSON file
        and deserializes JSON file to instances, It thus
        represents an abstracted storage engine.

        Attributes:
        __file_path (str): The path to the name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    '''

    __filepath = 'airbnb_file.json'
    __objects = {}

    def all(self):
        """Returns all the objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id."""
        self.__objects['{}.{}'.format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        dicobject = {}
        for key in self.__objects:
            dicobject[key] = self.__objects[key]
        with open(self.__filepath, 'w', encoding='utf8') as json_file:
            json.dump(dicobject, json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__filepath, 'r', encoding='utf8') as json_file:
                json.load(json_file)
        except FileNotFoundError:
            pass
