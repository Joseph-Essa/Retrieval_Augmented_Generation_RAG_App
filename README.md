# Rag-App

This is the minimal implementation of the RAG model for Question Answering .

## Requirements

- python 3.8 or later 

#### install python using miniconda 

1) Download miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install)
2) create a new enviroment Using following comand :
```bash
$ conda craete -n rag_app python=3.8
```
3) Activate the enviroment :
```bash
$ conda activate rag_app
```
### (optional) Setup your comand line interface for better readability
``` bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation 

### Install the Requirment packages 

```bash
$ pip install -r requirements.txt
```
### Setup the enviroment variables 
```bash
$ cp .env.example .env
```

set your enviroment variables in the `.env` file. like `OPENAI_API_KEY` value.