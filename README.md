# **You Believe Your LLM is Not Delusional? Think Again!**

This repository contains the code accompanying our paper titled **"You Believe Your LLM is Not Delusional? Think Again! A Study of LLM Hallucination on Foundation Models under Perturbation,"** which has been submitted to [CODS-COMAD Dec'24](https://cods-comad.in/) and is currently under review.

## **Overview**

In this work, we present an evaluation framework designed to detect hallucinations in Large Language Models (LLMs). Our approach involves:
- **Query Perturbation:** Applying controlled perturbations at different levels (character, word, and sentence) to the input queries.
- **Consistency Score Calculation:** Measuring the consistency between the responses generated for the original query and the perturbed query to identify potential hallucination scenarios.

## **Repository Structure**

This repository is organized into the following sections:

### **1. Prepare Data**
- **Description:** Contains scripts to download datasets from Hugging Face Hub and apply various perturbations to the queries at character, word, and sentence levels.
- **Files and Modules:**
  - `perturbations`: Module with functions to introduce character-level, word-level, and sentence-level perturbations.
  - `main.py`: Script to download data from Hugging Face Hub and apply perturbations.

### **2. Generate Responses**
- **Description:** Includes code for querying LLMs and obtaining responses for both original and perturbed queries.
- **Files and Modules:**
  - `generate_response.py`: Function to format LLM call.
  - `main.py`: Script to generate responses using LLM.

### **3. Generate Scores**
- **Description:** Provides tools for calculating hallucination scores by comparing responses to original and perturbed queries.
- **Files and Modules:**
  - `utils.py`: Contains the model to return scores.
  - `main.py`: Script to generate scores.

## **Usage Instructions**

1. **Prepare the environment:**
   Ensure you have the required dependencies installed by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the data preparation pipeline:**
   ```bash
   python -m prepare_data.main
   ```

3. **Generate LLM responses:**
   ```bash
   python -m generate_responses.main
   ```

4. **Calculate hallucination scores:**
   ```bash
   python -m generate_scores.main
   ```

## **Contact**

For any questions or discussions, please feel free to reach out to the authors:

| **Name**             | **Email Address**                     |
|----------------------|---------------------------------------|
| Anirban Saha         | anirban.saha@walmart.com              |
| Binay Gupta          | binay.gupta@walmart.com               |
| Anirban Chatterjee   | anirban.chatterjee@walmart.com        |
| Kunal Banerjee       | kunal.banerjee1@walmart.com           |
