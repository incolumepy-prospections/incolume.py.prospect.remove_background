import easygui as eg
from incolumepy.prospect.remove_bkgrounds.rmbg import rm_bg
from pathlib import Path
import logging

logFormat = '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;' \
            ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
logging.basicConfig(level=logging.INFO, format=logFormat)


def run():
    input_path = eg.fileopenbox(title='Select image file')
    output_path = eg.filesavebox(title='Save file to..')
    logging.info(f'{type(input_path)} {input_path}')
    logging.info(f'{type(output_path)} {output_path}')
    return rm_bg(input_path, output_path)


if __name__ == '__main__':
    run()
