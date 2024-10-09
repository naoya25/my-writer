import cv2
import numpy as np
from PIL import Image
import io
import os


def main():
    # 小文字
    image_slice("images/abc.png", "images/abc", 26, lambda i: chr(97 + i) + "_lower")
    # 大文字
    image_slice(
        "images/abc_large.png", "images/abc", 26, lambda i: chr(65 + i) + "_upper"
    )
    # その他、数字や記号など
    image_slice("images/other.png", "images/abc", 16, lambda i: str(i))

    # 背景を透過する
    sampling_chars()


def image_slice(image_path, output_path, slice_num, filename_rule):
    image = Image.open(image_path)

    width, height = image.size
    slice_width = width / slice_num

    for i in range(slice_num):
        left = i * slice_width
        right = (i + 1) * slice_width if i < slice_num - 1 else width

        cropped_image = image.crop((left, 0, right, height))

        file_name = filename_rule(i)
        cropped_image.save(f"{output_path}/{file_name}.png")

def sampling_chars():
    image_files = [
        f
        for f in os.listdir("images/abc")
        if os.path.isfile(os.path.join("images/abc", f))
    ]

    for image_file in image_files:
        sampling_black_area(
            os.path.join("images/abc", image_file),
            os.path.join("images/rm_bg_chars", image_file),
        )


def sampling_black_area(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    lower_black = np.array([0, 0, 0], dtype=np.uint8)
    upper_black = np.array([50, 50, 50], dtype=np.uint8)

    mask = cv2.inRange(image, lower_black, upper_black)

    image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    image_rgba[mask == 0] = [0, 0, 0, 0]

    output_image = Image.fromarray(image_rgba)
    output_image.save(output_image_path)


if __name__ == "__main__":
    main()
