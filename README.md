# discord-user-ai-tools
A collection of tools that can be used to make your own AI of any Discord user.


## Contents
`generate_dataset.py`
---
A dataset generator bot. Use this to make a dataset of any Discord user's messages.

`generate_model.ipynb`
---
This notebook file creates and trains an AI based on your dataset. Please run this on Google Colab!

`generate_text.py`
---
A basic bot which generates new AI messages based on your model.

## Preequisites

[Tensorflow](https://www.tensorflow.org/) and [GPT2](https://github.com/minimaxir/gpt-2-simple) are required for this to work.
To use Tensorflow, please download the following packages: <br>
- [CUDA 11.2](https://developer.download.nvidia.com/compute/cuda/11.2.0/network_installers/cuda_11.2.0_win10_network.exe)<br>
- [CUDNN 8.1](https://developer.download.nvidia.com/compute/redist/cudnn/v8.1.0/cudnn-11.2-windows-x64-v8.1.0.77.zip)<br>

Have fun with your brand-new AIs!<br><br>
**WARNING:** With the smallest model possible (117M) you can't have datasets over 1.6M messages or you'll run out of memory.
If you want to have larger datasets, please encode the dataset.
