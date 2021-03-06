# WebAPIScrapping

A flask App to scrap API from The NY Times Most Popular Articles API

## Getting Started

### Dependencies

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)

### Installing

**Clone this repository:**

```bash
git clone https://github.com/syahmi001/WebAPIScrapping
cd WebAPIScrapping
```

**Create a new virual environment:**

Conda

```bash
conda create -n <env_name> python=3.8
conda activate <env_name>
```

Virtualenv

```bash
python3 -m venv <env_name>
source <env_name>/bin/activate
```

**Install all the requirements:**

```bash
pip install -r requirements.txt
```

**Adding .env file to project root:**

For this step, you can either use your own API key or use the attached .env file.

1. Use your own api:
   - Visit the official website [here.](https://developer.nytimes.com/)
   - Register/Log in to your own account.
   - Get your API Key.
   - create .env file and put the value there. Example:
   ```
   # Environment variables for the project
   API_KEY=<Put your key here>
   ```
2. Using the provided .env file:
   - Copy the `.env` file and put them at the root of the folder
   - The structure will be like this:
   ```
   .
   ├── static             # CSS folder
   ├── templates          # HTML folder
   ├── utils              # Custom made Utils library to help with the automation scrapping script
   ├── .env <--(put here) # Automated tests (alternatively `spec` or `tests`)
   ├── app.py            # The main file to run Flask App
   ├── requirements.txt   # Requirement file to install
   └── README.md
   ```

### Executing program

Run `app.py` to execute the program:

```bash
python app.py
```

To access the app, go to `http://localhost:5000`

### Running the App in Docker

**Build Docker Image:**

To build docker image, simply run:

```bash
docker build --tag webapi-scrapper .
```

**Run Docker Image:**

To run the image, use the following command:

```bash
docker run -d -p 5000:5000 webapi-scrapper
```

Then, the app is available at `http://localhost:5000`.

(Note: Don't forget to include `.env` file to be copied into your container!)

### Deployment

The app is deployed in `heroku`. To access it, you can click the link below:

[https://web-api-scrapping.herokuapp.com/](https://web-api-scrapping.herokuapp.com/)

OR

The link in project's `About` at the top right of the Github page.
