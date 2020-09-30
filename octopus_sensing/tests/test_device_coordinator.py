# This file is part of Octopus Sensing <https://octopus-sensing.nastaran-saffar.me/>
# Copyright © Nastaran Saffaryazdi 2020
#
# Octopus Sensing is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
#  either version 3 of the License, or (at your option) any later version.
#
# Octopus Sensing is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar.
# If not, see <https://www.gnu.org/licenses/>.

import time

import pytest

from octopus_sensing.device_coordinator import MonitoringCache, DeviceCoordinator
from octopus_sensing.devices.device import Device


def test_monitoring_cache():
    cache = MonitoringCache()

    data = [1, 2, 3]

    cache.cache(data)

    time.sleep(0.06)
    assert cache.get_cache() == data

    time.sleep(0.05)
    assert cache.get_cache() is None

class FakeDevice(Device):
    def _run(self):
        pass

def test_should_assign_device_names():

    device = FakeDevice()

    coordinator = DeviceCoordinator()
    coordinator.add_device(device)

    assert device.name is not None

def test_no_duplicated_device_name():
    device1 = FakeDevice(name="test-device")
    device2 = FakeDevice(name="test-device")

    coordinator = DeviceCoordinator()
    with pytest.raises(Exception):
        coordinator.add_devices([device1, device2])
