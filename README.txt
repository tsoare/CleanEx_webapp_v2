README for the CleanEx web app:

The goal of CleanEx: Tissue-specific expression predictor is to predict whether a novel promoter sequence is likely to be expressed specifically in an organ or tissue of interest.
The input is a FASTA file (e.g. *.fasta, *.fa) of sequences that are 1000 base pairs long and the output is the probability that each sequence is likely to be "liver-specific" or
expressed primarily in the liver as opposed to the rest of the human body.

Under the hood, features are derived from the sequences (counts of N-grams), normalized, and fed into a logistic regression model to return the probability of being "liver-specific".
The accuracy in the test data was 60%, so testing novel sequences in this way is a useful filter before carrying forward promising sequences to be assessed experimentally in cell lines.

For more background information, please see cleanex.press.  For more information on feature engineering, model selection, and statistical analyses, see the clean_ex2_data folder.  Feel free to reach out with any questions!