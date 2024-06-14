import re
import nltk
from nltk.corpus import wordnet
from nltk import pos_tag
from utils.core_utils import CoreUtils
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import ssl

class PathsUtils(CoreUtils):
    def __init__(self):

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        self.tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
        self.model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

    @staticmethod
    def is_kebab_case(s):
        return bool(re.match(r'^[a-z]+(-[a-z]+)*$', s))

    def is_valid_english_word(self, word):
        context = (
            "In the financial industry, words like bank, banks, loan, loans, investment, "
            "investments, stock, stocks, bond, bonds, asset, assets, equity, equities, "
            "portfolio, portfolios, derivative, derivatives, trade, trades, market, markets, "
            "fund, funds, transaction, transactions, account, accounts, client, clients, "
            "insurance, insurances, mortgage, mortgages, credit, credits, debit, debits, "
            "finance, finances, capital, capitals, currency, currencies are considered valid words."
        )
        inputs = self.tokenizer.encode_plus(word, context, return_tensors='pt')
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        outputs = self.model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits).item()
        predicted_class_label = self.model.config.id2label[predicted_class_id]

        return predicted_class_label.lower() == "positive"

    @staticmethod
    def is_plural(word):
        return word.endswith('s') and not word.endswith('ss')

    @staticmethod
    def is_noun(word):
        synsets = wordnet.synsets(word)
        if not synsets:
            return False
        return any('n' in synset.lexname() for synset in synsets)

    @staticmethod
    def is_verb(word):
        pos = pos_tag([word])[0][1]
        return pos.startswith('VB')

    def is_noun_and_plural(self, word):
        return self.is_noun(word) and self.is_plural(word)
