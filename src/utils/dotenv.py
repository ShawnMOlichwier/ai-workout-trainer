from dotenv import load_dotenv



def load_env_vars():
    try:
        load_dotenv()  # take environment variables from .env.

    except:
        print("Environment variables not loaded. \n\n \
              Ensure you have a .env file in your repository.")