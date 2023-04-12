
import os
import glob
import yamale


def validate_all(schema, pattern):
    with open("includes.schema.yaml") as fp:
        includes = fp.read()
    with open(schema) as fp:
        content = fp.read() + includes
    schema = yamale.make_schema(content=content)
    
    for defs in glob.glob(pattern):
        if "/ui/" in defs:
            continue
        print (defs)
        data = yamale.make_data(defs)
        yamale.validate(schema, data)
    
if __name__ == '__main__':
    validate_all("./tags.schema.yaml", "../data/*tags*.yaml")
    validate_all("./point.schema.yaml", "../data/*/*point*.yaml")
    validate_all("./equip.schema.yaml", "../data/*/equip.*.yaml")

    
