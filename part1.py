from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the pre-trained BERT model and tokenizer
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Analyze the sentiment of the statements made by the Federal Reserve
statements = ["The Federal Reserve is committed to maintaining price stability and supporting the economic recovery.", "The Federal Reserve is concerned about rising inflation and may raise interest rates."]
scores = []
for statement in statements:
    input_ids = torch.tensor([tokenizer.encode(statement, add_special_tokens=True)])
    with torch.no_grad():
        output = model(input_ids)[0]
    score = torch.sigmoid(output[0,0]).item()
    scores.append(score)

# Print the sentiment scores for the two example statements
print("Sentiment scores:")
for i, statement in enumerate(statements):
    print(f"Statement {i+1}: {statement}\nScore: {scores[i]}\n")
