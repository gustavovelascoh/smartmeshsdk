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


class NetworkWriteConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NetworkWriteConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'advertising_key': 'bytearray',
            'base_pk_period': 'int',
            'cca_mode': 'int',
            'channel_list': 'int',
            'common_join_key': 'bytearray',
            'down_frame_multiplier': 'int',
            'down_frame_multiplier_delay': 'int',
            'down_frame_size': 'int',
            'gps_mode': 'bool',
            'ip_addr_prefix': 'str',
            'join_security_type': 'str',
            'min_service_pk_period': 'int',
            'network_id': 'int',
            'num_parents': 'int',
            'topology_type': 'str',
            'up_frame_size': 'int'
        }

        self.attribute_map = {
            'advertising_key': 'advertisingKey',
            'base_pk_period': 'basePkPeriod',
            'cca_mode': 'ccaMode',
            'channel_list': 'channelList',
            'common_join_key': 'commonJoinKey',
            'down_frame_multiplier': 'downFrameMultiplier',
            'down_frame_multiplier_delay': 'downFrameMultiplierDelay',
            'down_frame_size': 'downFrameSize',
            'gps_mode': 'gpsMode',
            'ip_addr_prefix': 'ipAddrPrefix',
            'join_security_type': 'joinSecurityType',
            'min_service_pk_period': 'minServicePkPeriod',
            'network_id': 'networkId',
            'num_parents': 'numParents',
            'topology_type': 'topologyType',
            'up_frame_size': 'upFrameSize'
        }

        self._advertising_key = None
        self._base_pk_period = None
        self._cca_mode = None
        self._channel_list = None
        self._common_join_key = None
        self._down_frame_multiplier = None
        self._down_frame_multiplier_delay = None
        self._down_frame_size = None
        self._gps_mode = None
        self._ip_addr_prefix = None
        self._join_security_type = None
        self._min_service_pk_period = None
        self._network_id = None
        self._num_parents = None
        self._topology_type = None
        self._up_frame_size = None

    @property
    def advertising_key(self):
        """
        Gets the advertising_key of this NetworkWriteConfig.
        Advertising key for this network, in base64 format. The key must be 128 bits long. For security reasons, the key is not returned in GET response.

        :return: The advertising_key of this NetworkWriteConfig.
        :rtype: bytearray
        """
        return self._advertising_key

    @advertising_key.setter
    def advertising_key(self, advertising_key):
        """
        Sets the advertising_key of this NetworkWriteConfig.
        Advertising key for this network, in base64 format. The key must be 128 bits long. For security reasons, the key is not returned in GET response.

        :param advertising_key: The advertising_key of this NetworkWriteConfig.
        :type: bytearray
        """
        self._advertising_key = advertising_key

    @property
    def base_pk_period(self):
        """
        Gets the base_pk_period of this NetworkWriteConfig.
        Base bandwidth (in ms/packet) that the manager should allocate for each device

        :return: The base_pk_period of this NetworkWriteConfig.
        :rtype: int
        """
        return self._base_pk_period

    @base_pk_period.setter
    def base_pk_period(self, base_pk_period):
        """
        Sets the base_pk_period of this NetworkWriteConfig.
        Base bandwidth (in ms/packet) that the manager should allocate for each device

        :param base_pk_period: The base_pk_period of this NetworkWriteConfig.
        :type: int
        """
        self._base_pk_period = base_pk_period

    @property
    def cca_mode(self):
        """
        Gets the cca_mode of this NetworkWriteConfig.
        Clear channel assessment (CCA) mode. The value 0 means CCA is disabled. The CCA mode enabled by other values depends on the capabilities of the hardware. Other CCA mode values are 1 - energy detect, 2 - carrier sense, 3 - both energy detect and carrier sense. *

        :return: The cca_mode of this NetworkWriteConfig.
        :rtype: int
        """
        return self._cca_mode

    @cca_mode.setter
    def cca_mode(self, cca_mode):
        """
        Sets the cca_mode of this NetworkWriteConfig.
        Clear channel assessment (CCA) mode. The value 0 means CCA is disabled. The CCA mode enabled by other values depends on the capabilities of the hardware. Other CCA mode values are 1 - energy detect, 2 - carrier sense, 3 - both energy detect and carrier sense. *

        :param cca_mode: The cca_mode of this NetworkWriteConfig.
        :type: int
        """
        self._cca_mode = cca_mode

    @property
    def channel_list(self):
        """
        Gets the channel_list of this NetworkWriteConfig.
        RF channels used in the network, encoded as bitmap.  Bit 0x0001 corresponds to channel 1 and bit 0x8000 corresponds to channel 16 (0=not used, 1=used). The actual frequency, in megahertz, for any channel can be calculated using the following formula: `F = 2405+5*(chanNumber-1)`. *

        :return: The channel_list of this NetworkWriteConfig.
        :rtype: int
        """
        return self._channel_list

    @channel_list.setter
    def channel_list(self, channel_list):
        """
        Sets the channel_list of this NetworkWriteConfig.
        RF channels used in the network, encoded as bitmap.  Bit 0x0001 corresponds to channel 1 and bit 0x8000 corresponds to channel 16 (0=not used, 1=used). The actual frequency, in megahertz, for any channel can be calculated using the following formula: `F = 2405+5*(chanNumber-1)`. *

        :param channel_list: The channel_list of this NetworkWriteConfig.
        :type: int
        """
        self._channel_list = channel_list

    @property
    def common_join_key(self):
        """
        Gets the common_join_key of this NetworkWriteConfig.
        Common join key (only valid if joinSecurityMode is \"common skey\"), in base64 format. The key must be 128 bits long. For security reasons, the key is not returned in GET response

        :return: The common_join_key of this NetworkWriteConfig.
        :rtype: bytearray
        """
        return self._common_join_key

    @common_join_key.setter
    def common_join_key(self, common_join_key):
        """
        Sets the common_join_key of this NetworkWriteConfig.
        Common join key (only valid if joinSecurityMode is \"common skey\"), in base64 format. The key must be 128 bits long. For security reasons, the key is not returned in GET response

        :param common_join_key: The common_join_key of this NetworkWriteConfig.
        :type: bytearray
        """
        self._common_join_key = common_join_key

    @property
    def down_frame_multiplier(self):
        """
        Gets the down_frame_multiplier of this NetworkWriteConfig.
        Downstream frame multiplier is a multiplier for the length of the primary downstream frame. Valid values are 1, 2 or 4. *

        :return: The down_frame_multiplier of this NetworkWriteConfig.
        :rtype: int
        """
        return self._down_frame_multiplier

    @down_frame_multiplier.setter
    def down_frame_multiplier(self, down_frame_multiplier):
        """
        Sets the down_frame_multiplier of this NetworkWriteConfig.
        Downstream frame multiplier is a multiplier for the length of the primary downstream frame. Valid values are 1, 2 or 4. *

        :param down_frame_multiplier: The down_frame_multiplier of this NetworkWriteConfig.
        :type: int
        """
        self._down_frame_multiplier = down_frame_multiplier

    @property
    def down_frame_multiplier_delay(self):
        """
        Gets the down_frame_multiplier_delay of this NetworkWriteConfig.
        Time delay to apply the downstream frame multiplier, in minutes, starting from first mote join. *

        :return: The down_frame_multiplier_delay of this NetworkWriteConfig.
        :rtype: int
        """
        return self._down_frame_multiplier_delay

    @down_frame_multiplier_delay.setter
    def down_frame_multiplier_delay(self, down_frame_multiplier_delay):
        """
        Sets the down_frame_multiplier_delay of this NetworkWriteConfig.
        Time delay to apply the downstream frame multiplier, in minutes, starting from first mote join. *

        :param down_frame_multiplier_delay: The down_frame_multiplier_delay of this NetworkWriteConfig.
        :type: int
        """
        self._down_frame_multiplier_delay = down_frame_multiplier_delay

    @property
    def down_frame_size(self):
        """
        Gets the down_frame_size of this NetworkWriteConfig.
        Frame size (in number of timeslots) for downstream traffic. *

        :return: The down_frame_size of this NetworkWriteConfig.
        :rtype: int
        """
        return self._down_frame_size

    @down_frame_size.setter
    def down_frame_size(self, down_frame_size):
        """
        Sets the down_frame_size of this NetworkWriteConfig.
        Frame size (in number of timeslots) for downstream traffic. *

        :param down_frame_size: The down_frame_size of this NetworkWriteConfig.
        :type: int
        """
        self._down_frame_size = down_frame_size

    @property
    def gps_mode(self):
        """
        Gets the gps_mode of this NetworkWriteConfig.
        Indicates whether the manager should expect GPS-enabled AP Bridge devices to join the network. If this field is set to false, the manager will select an AP Mote to be the master clock source. *

        :return: The gps_mode of this NetworkWriteConfig.
        :rtype: bool
        """
        return self._gps_mode

    @gps_mode.setter
    def gps_mode(self, gps_mode):
        """
        Sets the gps_mode of this NetworkWriteConfig.
        Indicates whether the manager should expect GPS-enabled AP Bridge devices to join the network. If this field is set to false, the manager will select an AP Mote to be the master clock source. *

        :param gps_mode: The gps_mode of this NetworkWriteConfig.
        :type: bool
        """
        self._gps_mode = gps_mode

    @property
    def ip_addr_prefix(self):
        """
        Gets the ip_addr_prefix of this NetworkWriteConfig.
        IPv6 address prefix for devices in the network. Only the leading 8 octets are relevant. Mask (if any) should be specified using CIDR notation. *

        :return: The ip_addr_prefix of this NetworkWriteConfig.
        :rtype: str
        """
        return self._ip_addr_prefix

    @ip_addr_prefix.setter
    def ip_addr_prefix(self, ip_addr_prefix):
        """
        Sets the ip_addr_prefix of this NetworkWriteConfig.
        IPv6 address prefix for devices in the network. Only the leading 8 octets are relevant. Mask (if any) should be specified using CIDR notation. *

        :param ip_addr_prefix: The ip_addr_prefix of this NetworkWriteConfig.
        :type: str
        """
        self._ip_addr_prefix = ip_addr_prefix

    @property
    def join_security_type(self):
        """
        Gets the join_security_type of this NetworkWriteConfig.
        Join security type. *

        :return: The join_security_type of this NetworkWriteConfig.
        :rtype: str
        """
        return self._join_security_type

    @join_security_type.setter
    def join_security_type(self, join_security_type):
        """
        Sets the join_security_type of this NetworkWriteConfig.
        Join security type. *

        :param join_security_type: The join_security_type of this NetworkWriteConfig.
        :type: str
        """
        allowed_values = ["common_skey", "unique_skey"]
        if join_security_type not in allowed_values:
            raise ValueError(
                "Invalid value for `join_security_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._join_security_type = join_security_type

    @property
    def min_service_pk_period(self):
        """
        Gets the min_service_pk_period of this NetworkWriteConfig.
        Limit for service requests from a mote. Defines minimum data interval (in ms/packet) that a single mote may be allocated for the total user-requested bandwidth

        :return: The min_service_pk_period of this NetworkWriteConfig.
        :rtype: int
        """
        return self._min_service_pk_period

    @min_service_pk_period.setter
    def min_service_pk_period(self, min_service_pk_period):
        """
        Sets the min_service_pk_period of this NetworkWriteConfig.
        Limit for service requests from a mote. Defines minimum data interval (in ms/packet) that a single mote may be allocated for the total user-requested bandwidth

        :param min_service_pk_period: The min_service_pk_period of this NetworkWriteConfig.
        :type: int
        """
        self._min_service_pk_period = min_service_pk_period

    @property
    def network_id(self):
        """
        Gets the network_id of this NetworkWriteConfig.
        Network id. *

        :return: The network_id of this NetworkWriteConfig.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """
        Sets the network_id of this NetworkWriteConfig.
        Network id. *

        :param network_id: The network_id of this NetworkWriteConfig.
        :type: int
        """
        self._network_id = network_id

    @property
    def num_parents(self):
        """
        Gets the num_parents of this NetworkWriteConfig.
        Number of parents to assign to each mote

        :return: The num_parents of this NetworkWriteConfig.
        :rtype: int
        """
        return self._num_parents

    @num_parents.setter
    def num_parents(self, num_parents):
        """
        Sets the num_parents of this NetworkWriteConfig.
        Number of parents to assign to each mote

        :param num_parents: The num_parents of this NetworkWriteConfig.
        :type: int
        """
        self._num_parents = num_parents

    @property
    def topology_type(self):
        """
        Gets the topology_type of this NetworkWriteConfig.
        Topology created by the Network Controller. *

        :return: The topology_type of this NetworkWriteConfig.
        :rtype: str
        """
        return self._topology_type

    @topology_type.setter
    def topology_type(self, topology_type):
        """
        Sets the topology_type of this NetworkWriteConfig.
        Topology created by the Network Controller. *

        :param topology_type: The topology_type of this NetworkWriteConfig.
        :type: str
        """
        allowed_values = ["mesh", "star", "event"]
        if topology_type not in allowed_values:
            raise ValueError(
                "Invalid value for `topology_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._topology_type = topology_type

    @property
    def up_frame_size(self):
        """
        Gets the up_frame_size of this NetworkWriteConfig.
        Frame size (in number of timeslots) for upstream traffic. *

        :return: The up_frame_size of this NetworkWriteConfig.
        :rtype: int
        """
        return self._up_frame_size

    @up_frame_size.setter
    def up_frame_size(self, up_frame_size):
        """
        Sets the up_frame_size of this NetworkWriteConfig.
        Frame size (in number of timeslots) for upstream traffic. *

        :param up_frame_size: The up_frame_size of this NetworkWriteConfig.
        :type: int
        """
        self._up_frame_size = up_frame_size

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

