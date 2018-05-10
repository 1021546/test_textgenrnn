from textgenrnn import textgenrnn

# textgen = textgenrnn()
# textgen.generate()

# textgen.train_from_file('./datasets/hacker_news_2000.txt', num_epochs=1)
# textgen.generate()

textgen_2 = textgenrnn('./weights/hacker_news.hdf5')
textgen_2.generate(3, temperature=1.0)

# https://github.com/minimaxir/textgenrnn