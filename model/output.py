# %%
import tqdm as notebook_tqdm
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
# Load tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained(r'C:\Users\Aniket\Downloads\model_14-07-2024')
model = DistilBertForSequenceClassification.from_pretrained(r'C:\Users\Aniket\Downloads\model_14-07-2024')

# Sample text
sample_text = input()

# Tokenize the input text
inputs = tokenizer(sample_text, return_tensors='pt')

# Get model outputs
outputs = model(**inputs)

# Get logits
logits = outputs.logits

# Find the predicted label ID
predicted_label_id = logits.argmax().item()

# Map the predicted label ID to the actual label
predicted_label = model.config.id2label[predicted_label_id]

# Define the label dictionary
label_dict = {
    'LABEL_8': ['positive', 'desire'],
    'LABEL_0': ['positive', 'pride'],
    'LABEL_17': ['positive', 'joy'],
    'LABEL_5': ['positive', 'caring'],
    'LABEL_15': ['positive', 'gratitude'],
    'LABEL_18': ['positive', 'love'],
    'LABEL_7': ['ambiguous', 'curiosity'],
    'LABEL_13': ['positive', 'excitement'],
    'LABEL_21': ['positive', 'optimism'],
    'LABEL_20': ['ambiguous', 'neutral'],
    'LABEL_14': ['negative', 'fear'],
    'LABEL_26': ['negative', 'remorse'],
    'LABEL_3': ['negative', 'annoyance'],
    'LABEL_11': ['negative', 'disgust'],
    'LABEL_12': ['negative', 'embarrassment'],
    'LABEL_9': ['negative', 'disappointment'],
    'LABEL_2': ['negative', 'anger'],
    'LABEL_6': ['ambiguous', 'confusion'],
    'LABEL_23': ['ambiguous', 'realization'],
    'LABEL_27': ['ambiguous', 'surprise']
}

# Convert the predicted label to plain text using the label dictionary
plain_text = label_dict[predicted_label][0]
print(plain_text)

plain_text = label_dict[predicted_label][1]
print(plain_text)




# %%
