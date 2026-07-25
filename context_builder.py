import json


def build_context(controller, analysis):

    return f"""

Controller Code:

{controller}


API Analysis:

{json.dumps(
    analysis,
    indent=4
)}

Generate API documentation.

"""