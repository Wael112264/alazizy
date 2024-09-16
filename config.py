import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAE327YAxTts9rUhj1docyIlaMN4LofdPOhjGz75M-VN1VMkgILm-3Pu9uKtaRD3K3Fzwx2GHL7tXH_mzTF-NDJne2DmrrS0OC5zWpXos9_R8rB6Lg7kA_IvsJGrQm9UIyHlO9ytVQdc6pRYYWQut7oJ3lR7iVqZwIgzGSdJwsnK_CwDOMjs1_tL-qJ5CenHuRPurqCqMFRyobWVu35N0GXN-rbvMJVziu4J6QbBDDkBESfqhnI8K0aNbaCl4xtethN6Xs0lEeMME4S04lM-VbGke0FVKujpO4E0sAy8-M0MRs4rJghYyIrnIoaZoBDVEArS3g7DjrLZR8f6d9LI0EISaLhGFQAAAAG3Kc83AA")
BOT_TOKEN = getenv("BOT_TOKEN", "7516175611:AAG_Ja2c7XATzCbRqgvCajIa8fBR4-4ao7c")
BOT_NAME = getenv("BOT_NAME", "FR3ON")
API_ID = int(getenv("API_ID", "20437942"))
API_HASH = getenv("API_HASH", "abb0a6303ec6de4c5125b4fcdaf2b7b4")
OWNER_NAME = getenv("OWNER_NAME", "MG4_44")
ALIVE_NAME = getenv("ALIVE_NAME", "MG4_44")
BOT_USERNAME = getenv("BOT_USERNAME", "FR3ON_bot_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Uniquexa_7")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Fr3on_S")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G_aE5")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6425347654").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/06b651dc0d827b6887764.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
