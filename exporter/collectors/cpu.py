import psutil

class CPUCollector:

    def __init__(self) -> None:
        """
        TODO: @
        Constructor
        """
        pass

    def get_utilization(self):
        """
        TODO: @
        Returns the CPU utilization as a percentage.
        """
        return psutil.cpu_percent();

    def get_frequency(self):
        """
        TODO: @
        Returns the current CPU frequency in MHz.
        """
        return psutil.cpu_freq()[0];

    def get_temperature(self):
        """
        TODO: @
        Returns the CPU temperature in degrees Celsius.        
        """
        pass

    def __str__(self) -> str:
        """
        TODO:
        Returns to string representation of all CPU metrics.        
        """
        utilization = self.get_utilization();
        frequency = self.get_frequency();
        temp = self.get_temperature();
        return "CPU utilization: {utilization}%\n CPU frequency: {frequency}MHz\n CPU temperature: {temp}°C\n";
