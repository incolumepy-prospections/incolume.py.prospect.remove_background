# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib

from rembg import remove
from PIL import Image

__author__ = "@britodfbr"  # pragma: no cover


def rm_bg(input_path: (str | pathlib.Path),
          output_path: (str | pathlib.Path)) -> bool:
    input_path = pathlib.Path(input_path)
    if not input_path.exists():
        raise FileExistsError('File not exists')

    output_path = pathlib.Path(output_path)
    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True, exist_ok=True)

    input_filename = Image.open(input_path)
    output_filename = remove(input_filename)
    output_filename.save(output_path)
    return True
