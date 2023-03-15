# -*- coding: utf-8 -*-
import requests
import os
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


def main():
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    data_url = os.environ.get("GAMMA_MAGIC_DATA_PATH")
    names_url = os.environ.get("GAMMA_MAGIC_NAME_PATH")
    data_response = requests.get(data_url)
    names_response = requests.get(names_url)
    project_dir = Path(__file__).resolve().parents[2]
    out_data_dir = os.path.join(project_dir, "data/processed/magic04.data")
    out_name_dir = os.path.join(project_dir, "data/processed/magic04.names")

    with open(out_data_dir, "wb") as f:
        f.write(data_response.content)

    with open(out_name_dir, "wb") as f:
        f.write(names_response.content)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
