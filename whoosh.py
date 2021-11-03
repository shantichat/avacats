import json
import os

from PIL import Image
from pilkit.processors import SmartResize
from pilkit.utils import process_image


def main(root, dest, sizes):
    options = {
        'progressive': True,
        'optimize': True,
        'quality': 85,
    }

    for size in sizes:
        os.makedirs(f'{dest}/{size}x{size}', exist_ok=True)

    files = os.listdir(root)
    for i, name in enumerate(files):
        print(i, name)
        img = Image.open(f'{root}/{name}')

        for size in sizes:
            icon_path = f'{dest}/{size}x{size}/{i}.jpg'
            print('-->', icon_path)

            if os.path.exists(icon_path):
                os.remove(icon_path)

            icon = process_image(img, processors=[SmartResize(size, size)], options=options)
            with open(icon_path, 'wb') as f:
                f.write(icon.getvalue())

    index_json = {
        'sizes': sizes,
        'max': len(files),
    }

    with open(f'{dest}/index.json', 'w') as f:
        json.dump(index_json, f)


if __name__ == '__main__':
    main('source', 'public', sizes=[
        80,
        120,
        160,
        240,
    ])
