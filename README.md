# bot-o-dedo-aqui

A simple chatbot built while following and trying to understand the [Pytorch chatbot tutorial](https://pytorch.org/tutorials/beginner/chatbot_tutorial.html). I'll keep trying in other tutorials. I also need to learn *Python*. My bad.🙏

Some parts of this document may not work on a *Windows* or *Mac* rig. I could potentially test this doc on those types of machine, but I haven't so far. If you really need this stuff use a Linux rig. 🐧

## Install *pyenv*

We recommend **pyenv** to handle *python* versions. Install that (please...?).

### Windows 🪟

You're better off using wsl and following the "Linux" install, but I heard about these guys [right here](https://github.com/pyenv-win/pyenv-win) attempting to run *pyenv* on your sophisticated OS.

⚠️ **But proceed at your own risk! I ain't testing this in my awesome Windows rig. Nonetheless, I'll be happy to listen to you and update this doc if you have gone through the process, pal. Let's do business. The open source and free as free beer type of business.**

### MacOS

You should install *pyenv* using **Homebrew**.

```shell
brew update && \
brew install pyenv
# Now follow the rest of the installation process...
```

### Linux (and the majestic WSL as well)

Run the cool **Automatic Installer**!

```shell
curl https://pyenv.run | bash
# Follow the rest of the installation process. You go get what is yours, pumpkin!
```

## Build your environment

First of all, make sure you're using the right python version. It should be the same version as in the `.python-version` file.

```shell
python --version
# Should print something like this:
# Python 3.10.12
```

If *pyenv* is installed but the *python* version is not changing, you can run this 'fix-everything' command below (which I don't exactly know what it is doing, but things worked after running it on my machine).

```shell
eval "$(pyenv init -)"
# Now check the python version again
```

Finally, build the environment stuff.

```shell
python -m venv venv
```

A folder named `venv/` will be created. Now let's activate the created environment.

```shell
. venv/bin/activate
```

## Install the dependencies

Now that you've activated the environment, let's install the dependencies listed in the `requirements.txt` file.

```shell
pip install -r requirements.txt
```

⚠️ **When you install new dependencies on the project, you must update the `requirements.txt` file! Like, if you need the cool spring dependency and install it with `pip install spring`. Now, so others can install this new dependency, we must list it in the `requirements.txt`.**

```
pip freeze > requirements.txt
```

## The `.env` file not provided 😥

As a good practice (in my own mind) we didn't included an `.env` file. But the nature of our `.env` file makes it a candidate for publicity since no sensitive or private information is in there... Nonetheless let's keep the good practices and force our users to create their own `.env` file in the project's root folder.

Here's my `.env` file. You can use these values on your `.env` as well.

⚠️ **The `.env` file does not have an extension. It is exactly '`.env`' and that's it.**

```env
CORPUS_NAME=comm-corpus
UTTERANCES_ENCODING=iso-8859-1
FORMATTED_UTTERANCES_ENCODING=utf-8

ASSEMBLING_MAX_LENGTH=10
```

## The [**Pytorch chatbot tutorial**](https://pytorch.org/tutorials/beginner/chatbot_tutorial.html) files

Yeah... You totally need the *tutorial* files, provided in a zip by the awesome *Cornell* folks (see below). So far, for this code, you'll at least need to put the `utterances.jsonl` from the *tutorial zip* in the `data/comm-corpus/` folder here in the project. I'm not putting it in the repo. It is a big *a*** file (around 350Mb). 

You can get the files directly from the [**Pytorch chatbot tutorial**](https://pytorch.org/tutorials/beginner/chatbot_tutorial.html) or you can get them [here](https://zissou.infosci.cornell.edu/convokit/datasets/movie-corpus/movie-corpus.zip) directly, for your convenience (we're just pointing you to the *Cornell* zip file).


