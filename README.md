# Book_Recomendation_System
Live Demo : https://book-recomendation-system-zidn.onrender.com
<img width="1592" height="860" alt="image" src="https://github.com/user-attachments/assets/4b945d49-ed58-4bba-8f02-44b6b3ab8060" />
# Built With
1. streamlit
2. Machine learning
3. sklearn

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/ML-Based-Book-Recommender-System.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now run,
```bash
streamlit run app.py
```

```bash
Note: Before clicking on show recommendations first of all click on Train Recommender System for generating models
```

# How to run in Docker?

#### Build a Docker image
The docker build command builds an image from a Dockerfile . Run the following command from the app/ directory on your server to build the image:


```bash
docker build -t streamlit .
```

The -t flag is used to tag the image. Here, we have tagged the image streamlit. If you run:

```bash
docker images
```
You should see a streamlit image under the REPOSITORY column. For example:

```bash
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```

#### Run the Docker container
Now that you have built the image, you can run the container by executing:

```bash
docker run -p 8501:8501 streamlit
```

The -p flag publishes the container’s port 8501 to your server’s 8501 port.

If all went well, you should see an output similar to the following:



