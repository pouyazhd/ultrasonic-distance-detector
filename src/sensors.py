from dataclasses import dataclass
import RPi.GPIO as gpio
import time
import logging


@dataclass
class Pins:
    pin_list: dict

    @property
    def echo(self)->int:
        try:
            echo_pin = self.pin_list["echo"]
        except ValueError:
            raise f"[Error] 'echo' pin did not introduced correctly in config file"
    
        return echo_pin
    
    @property
    def trig(self)->int:
        try:
            trig_pin = self.pin_list["trig"]
        except ValueError:
            raise f"[Error] 'trig' pin did not introduced correctly in config file"

        return trig_pin

@dataclass
class GlobalParameters:
    global_parameters : dict
    
    @property
    def sound_speed(self) ->int:
        try:
            speed = 100*self.global_parameters["sound-speed"]
        except ValueError:
            raise f"[Error] 'sound-speed' did not introduced correctly in config file"

        return speed

    # @property
    # def interval(self) ->int:
    #     try:
    #         delay = self.global_parameters["interval"]
    #     except ValueError:
    #         raise f"[Error] 'interval' did not introduced correctly in config file"

    #     return delay

@dataclass
class UltrasonicConfigs:
    pins : Pins
    params : GlobalParameters


class UltraSonic:
    def __init__(self,pins:dict, parameters: dict) -> None:
        self.pins = Pins(pin_list=pins)
        self.parameters = GlobalParameters(global_parameters=parameters)
        self.config = UltrasonicConfigs(pins= self.pins,
                                        params= self.parameters)
        
        self.define_pins()
    
    def define_pins(self)-> None:
        try:
            gpio.setmode(gpio.BOARD)
            gpio.setup(self.config.pins.trig, gpio.OUT)
            gpio.setup(self.config.pins.echo, gpio.IN)
        except Exception as err:
            
            raise f"[ERROR] board pins did not configured correctly.\n{err}"
    

    def set_trig(self)-> None:
        """active trig pin for a special duration of time
        """
        gpio.output(self.config.pins.trig, True)  #gpio.HIGH)
        time.sleep(0.00001)
        gpio.output(self.config.pins.trig, False) # gpio.LOW)

    def get_echo(self)-> int:
        """capture a special pin for 

        Returns:
            int: distance in cm
        """
        while gpio.input(self.config.pins.echo) == 0:
            begin_time = time.time()
        while gpio.input(self.config.pins.echo) == 1:
            end_time = time.time()
        echo_duration =  end_time - begin_time
        dist = self.config.params.sound_speed*echo_duration/2

        return dist
    
    def get_distance(self)-> int:
        """send trigger signal and calculate distance in cm

        Returns:
            int: distance
        """
        self.set_trig()
        distance = self.get_echo()
        return distance
    