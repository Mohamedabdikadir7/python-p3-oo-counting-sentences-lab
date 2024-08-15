#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        return self.value.strip().endswith('.')

    def is_question(self):
        return self.value.strip().endswith('?')

    def is_exclamation(self):
        return self.value.strip().endswith('!')

    def count_sentences(self):
        # Replace ellipsis with a single period to avoid counting it as multiple sentences
        text = self.value.replace('...', '.')
        # Split the text by sentence-ending punctuation
        sentences = re.split('[.!?]+', text)
        # Remove empty strings and count non-empty sentences
        return sum(1 for sentence in sentences if sentence.strip())