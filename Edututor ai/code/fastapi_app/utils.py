import json
from ibm_watsonx_ai.foundation_models import ModelInference

with open("../credentials/watsonx.json") as f:
    creds = json.load(f)

model = ModelInference(
    model_id="ibm/granite-3-2b-instruct",  
    project_id=creds["project_id"],
    credentials=creds,
    params={
        "decoding_method": "sample",
        "max_new_tokens": 1024
    }
)

def get_ibm_response(prompt):
    response = model.generate_text(prompt)

    # Check if it's a dict and contains 'generated_text'
    if isinstance(response, dict) and "generated_text" in response:
        return response["generated_text"]
    else:
        return str(response)
