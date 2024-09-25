```python
import string

text = input()
result = text.translate(str.maketrans('', '', string.punctuation))
print(result)
```