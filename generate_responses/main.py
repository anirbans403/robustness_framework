import pandas as pd
from generate_responses.generate_response import get_answer

input_df = pd.read_parquet("2wikimqa_e.parquet")
question_columns = [
    "query",
    "c1p_sent",
    "c2p_sent",
    "c3p_sent",
    "w1p_sent",
    "w2p_sent",
    "w3p_sent",
    "s1p_sent",
    "s2p_sent",
    "s3p_sent",
]
models = ["gpt4"]


def get_responses(row):
    for model in models:
        for col in question_columns:
            question = row[col]
            context = row["context"]
            response = get_answer(context, question, model)
            row[f"{col}_{model}_response"] = response
    return row


output_df = input_df.apply(get_responses, axis=1)
output_df.to_parquet("2wikimqa_e_responses.parquet", index=False)
