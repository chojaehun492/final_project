from transformers import GPT2Tokenizer, GPT2Model

class GPT2Small:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2Model.from_pretrained(model_name)

        # Add a padding token if it doesn't exist
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def preprocess(self, text):
        tokens = self.tokenizer(
            text, 
            return_tensors="pt", 
            padding=True, 
            truncation=True, 
            max_length=128
        )
        return tokens

    def forward(self, inputs):
        outputs = self.model(**inputs)
        return outputs.last_hidden_state
