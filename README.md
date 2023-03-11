# ChatGPT Dataset Collection

This repository contains the dataset collection methods for ChatGPT-related mentions on Reddit, Twitter, and major news websites.

## Creating a virtual environment

Follow the steps [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Once you have activated the virtual environment, move on to the next section.

## Installing dependencies

```bash
pip install -r requirements.txt
```

## Downloading news articles using News API

This section details the steps to download the news articles from major news websites using the News API and save them in the ```data``` folder of the project:

### Prerequisites

- You need to have a News API account to download news articles from major news websites. You can sign up [here](https://newsapi.org/register).

- Once you have signed up, you will receive an API key. Save this API key in a file called ```.env``` in the root folder of the project. Make sure to add ```.env``` to the ```.gitignore``` file if it is not already there.

- The ```.env``` file should contain the following line:

```bash
NEWS_API_KEY=<your_api_key>
```

### Downloading the news articles

Run the following command in the terminal or command prompt to download the news articles:

```bash
python download_news_articles.py
```

This command will download the news articles and save them to ```news_retrieval.py``` in the ```data``` folder of your project.

## Downloading Kaggle datasets using Kaggle API

This section details the steps to download the datasets from the following Kaggle links using the Kaggle API and save them in the ```data``` folder of the project:

- https://www.kaggle.com/datasets/armitaraz/chatgpt-reddit

- https://www.kaggle.com/datasets/tariqsays/chatgpt-twitter-dataset

- https://www.kaggle.com/datasets/manishabhatt22/tweets-onchatgpt-chatgpt

### Prerequisites

- You need to have a Kaggle account to download datasets from Kaggle. You can sign up [here](https://www.kaggle.com/account/login).

- You need to have the Kaggle API installed on your machine. You can install it using the following command:

```bash
pip install kaggle
```

### Downloading the datasets

1. Go to the Kaggle website and create an API token by going to the "Account" tab and clicking "Create New API Token". This will download a JSON file containing your API credentials.

2. Save the API token JSON file to your local machine (do not put it in the git-controlled folder of your project).

3. Set up the Kaggle API by running the following commands in the terminal or command prompt:

```bash 
mkdir ~/.kaggle
cp /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

Replace ```/path/to/kaggle.json``` with the path to the JSON file containing your API credentials.

4. Run the following commands in the terminal or command prompt to download the datasets:

```bash
mkdir data
cd data
kaggle datasets download -d armitaraz/chatgpt-reddit
kaggle datasets download -d tariqsays/chatgpt-twitter-dataset
kaggle datasets download -d manishabhatt22/tweets-onchatgpt-chatgpt
```
These commands will download the datasets and save them in the ```data``` folder of your project.

5. Unzip the downloaded datasets