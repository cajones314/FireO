from datetime import datetime

from fireo.fields import Field, errors
from google.cloud import firestore
from google.cloud.firestore_v1.transforms import Sentinel


class DateTime(Field):
    """Date Time field for firestore

    allowed_attributes = [auto]

    Examples
    --------
        class User(Model):
            created = DateTime()

        u = User()
        u.created = datetime.datetime.now()
    """

    allowed_attributes = ['auto']

    def attr_auto(self, attr_val, field_val):
        """Method for attribute auto"""
        if field_val is None and attr_val:
            return firestore.SERVER_TIMESTAMP
        return field_val

    # Override method
    def db_value(self, val):
        if type(val) is datetime or type(val) is Sentinel or val is None:
            return val
        raise errors.InvalidFieldType(f'Invalid field type. Field "{self.name}" expected {datetime}, '
                                      f'got {type(val)}')
