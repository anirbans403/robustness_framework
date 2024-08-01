import pandas as pd
from datasets import load_dataset
from prepare_data.perturbations.main import all_perturbation

data = load_dataset("THUDM/LongBench", "2wikimqa_e", split="test")
df = pd.DataFrame()
df["query"] = data["input"]
df["context"] = data["context"]
df["ga"] = data["input"]
df = df.iloc[:2]
res = all_perturbation(df["query"])
df["c1p_sent"] = res[0]
df["c2p_sent"] = res[1]
df["c3p_sent"] = res[2]
df["w1p_sent"] = res[3]
df["w2p_sent"] = res[4]
df["w3p_sent"] = res[5]
df["s1p_sent"] = res[6]
df["s2p_sent"] = res[7]
df["s3p_sent"] = res[8]
df.to_parquet("2wikimqa_e.parquet", index=False)
