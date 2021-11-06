# This script works best when ran on Google Colab.
# https://colab.research.google.com/
# This script is used to train an GPT2 AI based on your dataset.
# Make sure your dataset has <|startoftext|> and <|endoftext|> at the beginning and end of your lines for a lower loss!

# !pip install gpt-2-simple

import gpt_2_simple as gpt2
import os

if not os.path.isdir("models"):
    gpt2.download_gpt2(model_name="124M")

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset="gpt_dataset.txt",
              model_name='124M',
              print_every=10,
              sample_every=100,
              save_every=500,
              )

# gpt2.mount_gdrive()
# gpt2.copy_checkpoint_to_gdrive(run_name="run1")
