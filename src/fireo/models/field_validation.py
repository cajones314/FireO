
class FieldValidation:

    def __init__(self, field, attributes):
        self.field = field
        self.attributes = attributes or {}

    # validate each field and it's attributes
    def validate(self, value):
        for attr in self.attributes:
            if attr not in self.field.allowed_attributes:
                raise AttributeError(f'{self.field.__class__.__name__} not allow attribute {attr}')

            if self.default is not None and value is None:
                value = self.default

    @property
    def default(self):
        return self.attributes.get('default')