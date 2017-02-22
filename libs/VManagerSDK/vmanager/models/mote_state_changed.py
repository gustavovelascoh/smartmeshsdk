# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class MoteStateChanged(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MoteStateChanged - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sys_time': 'datetime',
            'reason': 'str',
            'state': 'str',
            'mac_address': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'sys_time': 'sysTime',
            'reason': 'reason',
            'state': 'state',
            'mac_address': 'macAddress',
            'type': 'type'
        }

        self._sys_time = None
        self._reason = None
        self._state = None
        self._mac_address = None
        self._type = None

    @property
    def sys_time(self):
        """
        Gets the sys_time of this MoteStateChanged.
        Time of notification

        :return: The sys_time of this MoteStateChanged.
        :rtype: datetime
        """
        return self._sys_time

    @sys_time.setter
    def sys_time(self, sys_time):
        """
        Sets the sys_time of this MoteStateChanged.
        Time of notification

        :param sys_time: The sys_time of this MoteStateChanged.
        :type: datetime
        """
        self._sys_time = sys_time

    @property
    def reason(self):
        """
        Gets the reason of this MoteStateChanged.
        Reason for state transition

        :return: The reason of this MoteStateChanged.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this MoteStateChanged.
        Reason for state transition

        :param reason: The reason of this MoteStateChanged.
        :type: str
        """
        allowed_values = ["", "none", "rejoined", "globalCmd", "initialization", "noParents", "noResources", "unreachable", "transport", "rcError", "unexpected", "forced"]
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason`, must be one of {0}"
                .format(allowed_values)
            )
        self._reason = reason

    @property
    def state(self):
        """
        Gets the state of this MoteStateChanged.
        New state

        :return: The state of this MoteStateChanged.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this MoteStateChanged.
        New state

        :param state: The state of this MoteStateChanged.
        :type: str
        """
        allowed_values = ["lost", "negotiating", "connected", "operational", "decommissioned"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def mac_address(self):
        """
        Gets the mac_address of this MoteStateChanged.
        MAC address of the device whose state has changed

        :return: The mac_address of this MoteStateChanged.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this MoteStateChanged.
        MAC address of the device whose state has changed

        :param mac_address: The mac_address of this MoteStateChanged.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def type(self):
        """
        Gets the type of this MoteStateChanged.
        Notification type

        :return: The type of this MoteStateChanged.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MoteStateChanged.
        Notification type

        :param type: The type of this MoteStateChanged.
        :type: str
        """
        allowed_values = ["netStarted", "pathStateChanged", "pathAlert", "moteStateChanged", "joinFailed", "pingResponse", "invalidMIC", "dataPacketReceived", "ipPacketReceived", "packetSent", "cmdFinished", "configChanged", "configLoaded", "alarmOpened", "alarmClosed", "deviceHealthReport", "neighborHealthReport", "discoveryHealthReport", "rawMoteNotification", "serviceChanged", "apStateChanged", "managerStarted", "managerStopping", "optPhase", "pathAlert"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

