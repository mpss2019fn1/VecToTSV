# VecToTSV
Tiny script to convert a fastText / gensim vector file to a tsv file for displaying in Tensorflow's projector

## Usage
Make sure you have a vector file (result of word representation learning; e.g. fastText) at hand.
This file serves as input to this script.

`python model_to_tsv.py --input=<vector file> --output-vec=model.tsv --output-meta=meta.tsv`

You can upload both resulting files to the [TensorFlow Projector](https://projector.tensorflow.org/) in order to get a
visual representation of your word embeddings.
