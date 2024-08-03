# Prepare Data for LLM Hallucination Evaluation

This folder contains the code used to prepare and perturb data for evaluating hallucinations in Large Language Models (LLMs). The perturbations are applied at character, word, and sentence levels to generate varied input scenarios that help in analyzing the robustness of LLMs against such perturbations.

## Overview

The main script in this folder loads a dataset, applies a series of perturbations to the input queries, and saves the perturbed data into a parquet file for further analysis. The perturbations include:

1. **Character-level perturbations:**
   - Introduce typos in words.
   - Alter specific characters in the sentence.
   - Append extraneous characters to the end of the sentence.

2. **Word-level perturbations:**
   - Replace words with their synonyms.
   - Delete words that do not alter the sentence's meaning.
   - Add semantically neutral words to the sentence.

3. **Sentence-level perturbations:**
   - Append a randomly generated irrelevant handle to the sentence.
   - Paraphrase the sentence.
   - Change the syntactic structure of the sentence.

## Script Usage

The script performs the following steps:

1. **Load the Dataset:**
   - Uses the `datasets` library to load the split (e.g. `2wikimqa_e` ) from the `LongBench` dataset by `THUDM`.
   - Selects the first two examples for demonstration purposes.

2. **Prepare the DataFrame:**
   - Creates a pandas DataFrame containing the `query`, `context`, and `ga` (ground truth answer) columns from the loaded dataset.

3. **Apply Perturbations:**
   - Calls the `all_perturbation` function from the `prepare_data.perturbations.main` module, which applies all nine types of perturbations to the `query` column.

4. **Save the Perturbed Data:**
   - The perturbed queries are added to the DataFrame under the following columns:
     - `c1p_sent`, `c2p_sent`, `c3p_sent`: Character-level perturbations.
     - `w1p_sent`, `w2p_sent`, `w3p_sent`: Word-level perturbations.
     - `s1p_sent`, `s2p_sent`, `s3p_sent`: Sentence-level perturbations.
   - The final DataFrame is saved to a parquet file named `<split-name>.parquet`.


In the code example in `main.py`, we downloaded the `2wikimqa_e` dataset from Hugging Face Hub. The datasets we used include -  TriviaQA, WikiQA, HotpotQA, Qasper, SAMSum, TREC. 

Refer to [THUDM/LongBench](https://huggingface.co/datasets/THUDM/LongBench)  to explore the dataset. 