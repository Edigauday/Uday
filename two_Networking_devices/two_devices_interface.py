from pyats import aetest
from pyats.topology import loader

# Load the testbed
testbed = loader.load('two_testbeds.yaml')

# Define a testcase class
class MyTestcase(aetest.Testcase):

    # Define a common setup method to connect to devices
    @aetest.setup
    def connect_to_devices(self):
        self.connections = {}
        self.interface_names = ['GigabitEthernet3', 'Ethernet1/6']  # Replace with your interface names

        for device_name, device in testbed.devices.items():
            self.connections[device_name] = device
            device.connect()

    # Define tests to be performed on each device
    @aetest.test
    def test_interface_status(self):
        self.failed_devices = []

        for device_name, device in self.connections.items():
            show_interfaces = device.execute('show interface')

            for interface_name in self.interface_names:
                if interface_name in show_interfaces:
                    output_lines = show_interfaces.splitlines()
                    for line in output_lines:
                        if interface_name in line:
                            status = line.split()[-1].strip('(),')
                            if status.lower() == 'up':
                                self.passed(f'Interface {interface_name} on {device_name} is UP.')
                            else:
                                # Interface is down, try to bring it up
                                device.configure(f'interface {interface_name}\n'
                                                 'no shutdown\n'
                                                 'end\n')
                                self.passed(f'Interface {interface_name} on {device_name} has been enabled.')
                            break
                    else:
                        self.failed_devices.append(f'{device_name}: {interface_name}')
                else:
                    self.failed_devices.append(f'{device_name}: {interface_name}')

        if self.failed_devices:
            self.failed(
                f'Interfaces not found or not in UP state on devices: {", ".join(self.failed_devices)}')

    # Define a cleanup method to disconnect from devices
    @aetest.cleanup
    def disconnect_from_devices(self):
        for device_name, device in self.connections.items():
            device.disconnect()

# Run the testcases
if __name__ == '__main__':
    aetest.main()
