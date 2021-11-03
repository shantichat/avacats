# Cat avatars for adult independent users

## Samples
![Hi](https://shantichat.github.io/avacats/80x80/1.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/2.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/3.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/4.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/5.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/6.jpg)

## Usage

No libs need. Chek https://shantichat.github.io/avacats/index.json and write few lines of code:

### Python
```python
def avacat(name, size, *, num=36):
    """
    >>> avacat('user@example.com', 80)
    'https://shantichat.github.io/avacats/80x80/7.jpg'
    """
    assert size in {80, 120, 160, 240}
    i = hash(name.lower()) % num
    return f'https://shantichat.github.io/avacats/{size}x{size}/{i}.jpg'
```

### JS
```javascript
// implement me
```

## Sources

Thanx for https://www.pexels.com/search/cat/
