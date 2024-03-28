from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from request import ModelRequest

class Model():
    def __new__(cls, context):
        cls.context = context
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)
        model = 'KunalEsM/bank_complaint_intent_classifier_v2'
        cls.tokenizer = AutoTokenizer.from_pretrained(model)
        cls.model = AutoModelForSequenceClassification.from_pretrained(model)
        cls.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        cls.model.to(cls.device)
        return cls.instance


    async def inference(self,  request: ModelRequest):
        inputs = self.tokenizer(request.text, return_tensors="pt")
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with torch.no_grad():
            predicted_label = self.model(**inputs).logits.argmax().item()
        
        return predicted_label
