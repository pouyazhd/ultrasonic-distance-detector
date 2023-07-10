from src.sensors import UltraSonic
from src.metrics import *  # Metric settings
from time import sleep
import yaml
import logging

def load_configs(file_name:str="config.yaml")-> dict:
      try:
            with open(file=file_name, mode='r', encoding="utf-8") as cfp:
                  configs = yaml.safe_load(cfp)
      except FileNotFoundError:
            logging.error("config file does not found.")
            raise f"[ERROR] config file does not exist"
      except Exception as err:
            logging.error(err)
            raise f"[ERROR] could not read config file {file_name} "
      return configs

def main():
      CONFIG_PATH = "config.yaml"
      config = load_configs(CONFIG_PATH)
      start_http_server(config["metrics"]["exporter_port"])
      distance_sensor = UltraSonic(pins=config["pins"],
                                    parameters=config["global-parameters"])
      while True:
            distance = distance_sensor.get_distance()
            GARBAGE_HEIGHT_METRIC.set(distance)
            print(distance)
            sleep(config["global-parameters"]["interval"])

if __name__ =="__main__":
      main()
