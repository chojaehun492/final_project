import torch
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2Tokenizer

class TextDataset(Dataset):
    """
    텍스트 데이터를 GPT-2 모델에 맞게 전처리하는 데이터셋 클래스
    """
    def __init__(self, texts, tokenizer, max_length=128):
        if not texts:
            raise ValueError("Empty list provided for TextDataset.")
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        tokenized = self.tokenizer(
            text,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        return tokenized["input_ids"].squeeze(), tokenized["attention_mask"].squeeze()

def get_data_loader(texts, batch_size=8, max_length=128):
    """
    데이터 로더 생성 함수
    """
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    dataset = TextDataset(texts, tokenizer, max_length)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)
