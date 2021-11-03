import os
import PIL


def main(root):
    os.makedirs('i')
    for i, image in enumerate(os.listdir(root)):
        print(i, image)


if __name__ == '__main__':
    main('source')
