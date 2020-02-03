
from wand.image import Image
import os, sys
from tqdm import tqdm#loop progress bar

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

data_path = os.getcwd() + '/imagens_tratamento'

def convertPdfToImagem(pdf):
    with(Image(filename=pdf, resolution=300)) as source:
        for i, image in enumerate(source.sequence):
            newfilename = pdf[:-4] + str(i + 1) + '.jpeg'
            Image(image).save(filename=newfilename)
            os.remove(pdf)


def process_data():

    for img in tqdm(os.listdir(data_path)):
        convertPdfToImagem( data_path + '/' + img )


process_data()
