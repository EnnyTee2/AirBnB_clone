import uuid
from datetime import datetime

class BaseModel:
    """
    """

    def __init__(self, *args, **kwargs):
        if kwargs == {}:
            my_id = uuid.uuid4()
            self.id = str(my_id)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    setattr(self, key, self.formatter(value))
                elif key == 'updated_at':
                    setattr(self, key, self.formatter(value))
                else:
                    setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()

    def formatter(self, time):
        time_f = time[2:]
        time_f = time_f.replace('T', ' ')
        time_f = time_f.replace('-', '/')
        time_format = '%y/%m/%d %H:%M:%S.%f'
        return datetime.strptime(time_f, time_format)

    def to_dict(self):
        dicto = {'__class__': type(self).__name__ ,
                 'created_at': datetime.isoformat(self.created_at),
                 'updated_at': datetime.isoformat(self.updated_at)
                }
        dict_rep = dict(self.__dict__)
        dict_rep.update(dicto)
        return dict_rep

    def __str__(self):
        print(f"[{type(self).__name__}] ({self.id}) {self.__dict__}")
