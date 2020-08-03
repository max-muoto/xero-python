# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TimeEntryCreateOrUpdate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "user_id": "str",
        "task_id": "str",
        "date_utc": "datetime",
        "duration": "int",
        "description": "str",
    }

    attribute_map = {
        "user_id": "userId",
        "task_id": "taskId",
        "date_utc": "dateUtc",
        "duration": "duration",
        "description": "description",
    }

    def __init__(
        self, user_id=None, task_id=None, date_utc=None, duration=None, description=None
    ):  # noqa: E501
        """TimeEntryCreateOrUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._task_id = None
        self._date_utc = None
        self._duration = None
        self._description = None
        self.discriminator = None

        self.user_id = user_id
        self.task_id = task_id
        self.date_utc = date_utc
        self.duration = duration
        if description is not None:
            self.description = description

    @property
    def user_id(self):
        """Gets the user_id of this TimeEntryCreateOrUpdate.  # noqa: E501

        The xero user identifier of the person logging the time.  # noqa: E501

        :return: The user_id of this TimeEntryCreateOrUpdate.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TimeEntryCreateOrUpdate.

        The xero user identifier of the person logging the time.  # noqa: E501

        :param user_id: The user_id of this TimeEntryCreateOrUpdate.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def task_id(self):
        """Gets the task_id of this TimeEntryCreateOrUpdate.  # noqa: E501

        Identifier of the task that time entry is logged against.  # noqa: E501

        :return: The task_id of this TimeEntryCreateOrUpdate.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TimeEntryCreateOrUpdate.

        Identifier of the task that time entry is logged against.  # noqa: E501

        :param task_id: The task_id of this TimeEntryCreateOrUpdate.  # noqa: E501
        :type: str
        """
        if task_id is None:
            raise ValueError(
                "Invalid value for `task_id`, must not be `None`"
            )  # noqa: E501

        self._task_id = task_id

    @property
    def date_utc(self):
        """Gets the date_utc of this TimeEntryCreateOrUpdate.  # noqa: E501

        Date time entry is logged on. UTC Date Time in ISO-8601 format.  # noqa: E501

        :return: The date_utc of this TimeEntryCreateOrUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        """Sets the date_utc of this TimeEntryCreateOrUpdate.

        Date time entry is logged on. UTC Date Time in ISO-8601 format.  # noqa: E501

        :param date_utc: The date_utc of this TimeEntryCreateOrUpdate.  # noqa: E501
        :type: datetime
        """
        if date_utc is None:
            raise ValueError(
                "Invalid value for `date_utc`, must not be `None`"
            )  # noqa: E501

        self._date_utc = date_utc

    @property
    def duration(self):
        """Gets the duration of this TimeEntryCreateOrUpdate.  # noqa: E501

        Number of minutes to be logged. Duration is between 1 and 59940 inclusively.  # noqa: E501

        :return: The duration of this TimeEntryCreateOrUpdate.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimeEntryCreateOrUpdate.

        Number of minutes to be logged. Duration is between 1 and 59940 inclusively.  # noqa: E501

        :param duration: The duration of this TimeEntryCreateOrUpdate.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError(
                "Invalid value for `duration`, must not be `None`"
            )  # noqa: E501

        self._duration = duration

    @property
    def description(self):
        """Gets the description of this TimeEntryCreateOrUpdate.  # noqa: E501

        An optional description of the time entry, will be set to null if not provided during update.  # noqa: E501

        :return: The description of this TimeEntryCreateOrUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TimeEntryCreateOrUpdate.

        An optional description of the time entry, will be set to null if not provided during update.  # noqa: E501

        :param description: The description of this TimeEntryCreateOrUpdate.  # noqa: E501
        :type: str
        """

        self._description = description
