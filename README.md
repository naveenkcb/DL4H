# DL4H
Final Project
Reproduction of the paper "A Data-Centric Approach To Generate Faithful and High Quality Patient Summaries with Large Language Models"

This project was performed was part of CS 598 Deep Learning for Healthcare. We are part of Spring 2025 Cohorts. This is an effort to reproduce subset of the tasks performed by the authors of the original paper. The original github repo can be found here https://github.com/stefanhgm/patient_summaries_with_llms


##Overview

The below repository contains the necessary code that was used to reproduce the original paper in our local enviornment and prove the orginal methodology can be reproduced to a greater extent

preprocess - Preprocessing pipeline as presented in the paper.

labeling - Scripts to analyse and work with labeling data created with MedTator.

[scripts] - Scripts for parameter tuning of Llama2 7B model

[summarization] - All code related to the summarization experiments with LED and Llama 2 models

summ_notebooks - all notebooks used for fine tuning and evaluation along with complete log of the steps and results


In order to run evaluation, you can run the below code the below code

python summarization/exp1_eval_fine_tune_llama.py --model_name_or_path meta-llama/Llama-2-7b-hf --evaluation --evaluation_model_path /content/drive/MyDrive/DL4H-Project/mimic-iv-note-di-bhc/models/Llama-2-7b-hf/mimic-iv-note-di-bhc_Llama-2-7b-hf_4000_600_chars_100_valid/lora_rank_8_lora_alpha_32_lora_dropout_0.1_num_target_modules_2_learning_rate_2e-5/best_val_loss --data_path /content/drive/MyDrive/DL4H-Project/mimic-iv-note-di-bhc/dataset --output_path /content/drive/MyDrive/DL4H-Project/mimic-iv-note-di-bhc/models/Llama-2-7b-hf/mimic-iv-note-di-bhc_Llama-2-7b-hf_4000_600_chars_100_valid/lora_rank_8_lora_alpha_32_lora_dropout_0.1_num_target_modules_2_learning_rate_2e-5_test --num_train_examples 100 --num_val_examples 100 --num_test_examples 100
