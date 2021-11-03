# Cat avatars for adult independent users

## Samples

![Hi](https://shantichat.github.io/avacats/80x80/1.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/2.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/3.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/4.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/5.jpg)
![Hi](https://shantichat.github.io/avacats/80x80/6.jpg)

(Natasha, wake up!)

## Usage

Check values from https://shantichat.github.io/avacats/index.json:

```json
{ "sizes": [80, 120, 160, 240], "num": 255 }
```

Create url like `https://shantichat.github.io/avacats/{size}x{size}/{i}.jpg`, where:

- `size` is value from `sizes`
- `i = CRC32(lowercased_username) % num`.

Snippets:

- [Go](https://github.com/shantichat/avacats/tree/main/snippets/avacat.go)
- [JavaScript](https://github.com/shantichat/avacats/tree/main/snippets/avacat.js)
- [PHP](https://github.com/shantichat/avacats/tree/main/snippets/avacat.php)
- [Python](https://github.com/shantichat/avacats/tree/main/snippets/avacat.py)

## Sources

Thanx for https://thiscatdoesnotexist.com
