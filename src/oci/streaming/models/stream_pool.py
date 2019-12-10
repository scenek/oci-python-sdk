# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamPool(object):
    """
    The details of a stream pool.
    """

    #: A constant which can be used with the lifecycle_state property of a StreamPool.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a StreamPool.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a StreamPool.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a StreamPool.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a StreamPool.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a StreamPool.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new StreamPool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this StreamPool.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StreamPool.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this StreamPool.
        :type name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this StreamPool.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this StreamPool.
        :type lifecycle_state_details: str

        :param time_created:
            The value to assign to the time_created property of this StreamPool.
        :type time_created: datetime

        :param kafka_settings:
            The value to assign to the kafka_settings property of this StreamPool.
        :type kafka_settings: KafkaSettings

        :param freeform_tags:
            The value to assign to the freeform_tags property of this StreamPool.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this StreamPool.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'time_created': 'datetime',
            'kafka_settings': 'KafkaSettings',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'time_created': 'timeCreated',
            'kafka_settings': 'kafkaSettings',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._time_created = None
        self._kafka_settings = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this StreamPool.
        The OCID of the stream pool.


        :return: The id of this StreamPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StreamPool.
        The OCID of the stream pool.


        :param id: The id of this StreamPool.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this StreamPool.
        Compartment OCID that the pool belongs to.


        :return: The compartment_id of this StreamPool.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this StreamPool.
        Compartment OCID that the pool belongs to.


        :param compartment_id: The compartment_id of this StreamPool.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this StreamPool.
        The name of the stream pool.


        :return: The name of this StreamPool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StreamPool.
        The name of the stream pool.


        :param name: The name of this StreamPool.
        :type: str
        """
        self._name = name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this StreamPool.
        The current state of the stream pool.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this StreamPool.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this StreamPool.
        The current state of the stream pool.


        :param lifecycle_state: The lifecycle_state of this StreamPool.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this StreamPool.
        Any additional details about the current state of the stream.


        :return: The lifecycle_state_details of this StreamPool.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this StreamPool.
        Any additional details about the current state of the stream.


        :param lifecycle_state_details: The lifecycle_state_details of this StreamPool.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this StreamPool.
        The date and time the stream pool was created, expressed in in `RFC 3339`__ timestamp format.

        Example: `2018-04-20T00:00:07.405Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this StreamPool.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this StreamPool.
        The date and time the stream pool was created, expressed in in `RFC 3339`__ timestamp format.

        Example: `2018-04-20T00:00:07.405Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this StreamPool.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def kafka_settings(self):
        """
        **[Required]** Gets the kafka_settings of this StreamPool.

        :return: The kafka_settings of this StreamPool.
        :rtype: KafkaSettings
        """
        return self._kafka_settings

    @kafka_settings.setter
    def kafka_settings(self, kafka_settings):
        """
        Sets the kafka_settings of this StreamPool.

        :param kafka_settings: The kafka_settings of this StreamPool.
        :type: KafkaSettings
        """
        self._kafka_settings = kafka_settings

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this StreamPool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this StreamPool.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this StreamPool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this StreamPool.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this StreamPool.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this StreamPool.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this StreamPool.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this StreamPool.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
