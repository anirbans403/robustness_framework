## Generate Scores for LLM Responses (generate_scores)

This folder contains code to generate hallucination scores for LLM responses for the dataset. These scores aim to assess the consistency between the response to the original query and the responses to perturbed queries.

### Functionality

1. **Leverages Pre-trained Model:**
    * The code utilizes a pre-trained hallucination evaluation model from `vectara/hallucination_evaluation_model`. This model takes pairs of responses (base and comparison) and predicts a score indicating potential hallucination.
2. **Calculates Scores for Each Perturbation:**
    * The script iterates through various perturbed query responses available in the dataset (character-level, word-level, and sentence-level variations).
    * For each question, it compares the response to the original query (stored in `query_<model-name>_response`) with each perturbed response.
    * The pre-trained model is used to generate a score between 0 and 1, indicating the likelihood of hallucination in the perturbed response compared to the original response.
3. **Output:**
    * The script generates a new parquet file `<dataset>_scored.parquet`. 
    * This file contains the original data with additional columns appended to each perturbed response column (e.g., `c1p_sent_<model-name>_response_score`). These new columns store the corresponding hallucination score.

### Note
Version for model `vectara/hallucination_evaluation_model` used for our analysis - [hhem-1.0-open](https://huggingface.co/vectara/hallucination_evaluation_model/tree/hhem-1.0-open)
