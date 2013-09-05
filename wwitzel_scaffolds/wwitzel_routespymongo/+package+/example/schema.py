import colander as c

class Example(c.MappingSchema):
    name = c.SchemaNode(c.String())

