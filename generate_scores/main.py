from generate_scores.utils import model
import pandas as pd

input_df = pd.read_parquet("2wikimqa_e_responses.parquet")

base_response_column = "query_gpt4_response"
response_col_list = [
    "c1p_sent_gpt4_response",
    "c2p_sent_gpt4_response",
    "c3p_sent_gpt4_response",
    "w1p_sent_gpt4_response",
    "w2p_sent_gpt4_response",
    "w3p_sent_gpt4_response",
    "s1p_sent_gpt4_response",
    "s2p_sent_gpt4_response",
    "s3p_sent_gpt4_response",
]


def get_scores(row):
    for col in response_col_list:
        base_response = row[base_response_column]
        comparison_response = row[col]
        score = float(model.predict([(base_response, comparison_response)])[0])
        row[f"{col}_score"] = score
    return row


output_df = input_df.apply(get_scores, axis=1)
output_df.to_parquet("2wikimqa_e_scored.parquet", index=False)
