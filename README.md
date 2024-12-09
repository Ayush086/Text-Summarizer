# Text-Summarizer
NLP based Text Summarizer using Hugging Face

## Workflows
1. Update config.yaml
2. update params.yaml
3. update entity
4. update configuration manager in src/config/configuration.py
5. update components
6. update pipelines
7. update main.py
8. update app.py


## How to run it ?
### STEPS
#### 1. Clone the repository
```sh  
git clone https://github.com/Ayush086/Text-Summarizer.git  
```
#### 2. Open the repo and create a environment
```sh
conda create -m summary python=3.8 -y
```
**Activate the environment**
```sh
conda activate summary
```
*Run above commands to create and activate the environment*
#### 3. Install the requirements
```sh
pip install -r requirements.txt
```
#### 4. Run the app
```sh
python app.py
```
**Open the browser and navigate to http://127.0.0.1:8080 or http://localhost:8080**  
*Here port number may change in your case*