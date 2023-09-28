from pyats import aetest
from pyats.topology import loader

testbed = loader.load('my_testbed.yaml')

class MyTestcase(aetest.Testcase):

    @aetest.setup

    def connect_to_device(self):

        self.device= testbed.devices['Cat8000V']
        self.device.connect()

 
    @aetest.test

    def check_device_reachability(self):

        if self.device.is_connected():

            self.passed(f"{self.device} is reachable.")

        else:

            self.failed(f"{self.device} is not reachable.")

    @aetest.test

    def get_device_info(self):

        output = self.device.execute('show version')

        self.passed(f"Device Info:\n{output}")

 

    @aetest.cleanup

    def disconnect_from_device(self):

        self.device.disconnect()

if __name__ == '__main__':

    aetest.main()
