# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TrackingCategory(BaseModel):
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
        "tracking_category_id": "str",
        "tracking_option_id": "str",
        "name": "str",
        "option": "str",
        "status": "str",
        "options": "list[TrackingOption]",
    }

    attribute_map = {
        "tracking_category_id": "TrackingCategoryID",
        "tracking_option_id": "TrackingOptionID",
        "name": "Name",
        "option": "Option",
        "status": "Status",
        "options": "Options",
    }

    def __init__(
        self,
        tracking_category_id=None,
        tracking_option_id=None,
        name=None,
        option=None,
        status=None,
        options=None,
    ):  # noqa: E501
        """TrackingCategory - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_category_id = None
        self._tracking_option_id = None
        self._name = None
        self._option = None
        self._status = None
        self._options = None
        self.discriminator = None

        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id
        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if option is not None:
            self.option = option
        if status is not None:
            self.status = status
        if options is not None:
            self.options = options

    @property
    def tracking_category_id(self):
        """Gets the tracking_category_id of this TrackingCategory.  # noqa: E501

        The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The tracking_category_id of this TrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        """Sets the tracking_category_id of this TrackingCategory.

        The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param tracking_category_id: The tracking_category_id of this TrackingCategory.  # noqa: E501
        :type: str
        """

        self._tracking_category_id = tracking_category_id

    @property
    def tracking_option_id(self):
        """Gets the tracking_option_id of this TrackingCategory.  # noqa: E501

        The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f  # noqa: E501

        :return: The tracking_option_id of this TrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._tracking_option_id

    @tracking_option_id.setter
    def tracking_option_id(self, tracking_option_id):
        """Sets the tracking_option_id of this TrackingCategory.

        The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f  # noqa: E501

        :param tracking_option_id: The tracking_option_id of this TrackingCategory.  # noqa: E501
        :type: str
        """

        self._tracking_option_id = tracking_option_id

    @property
    def name(self):
        """Gets the name of this TrackingCategory.  # noqa: E501

        The name of the tracking category e.g. Department, Region (max length = 100)  # noqa: E501

        :return: The name of this TrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackingCategory.

        The name of the tracking category e.g. Department, Region (max length = 100)  # noqa: E501

        :param name: The name of this TrackingCategory.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def option(self):
        """Gets the option of this TrackingCategory.  # noqa: E501

        The option name of the tracking option e.g. East, West (max length = 100)  # noqa: E501

        :return: The option of this TrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this TrackingCategory.

        The option name of the tracking option e.g. East, West (max length = 100)  # noqa: E501

        :param option: The option of this TrackingCategory.  # noqa: E501
        :type: str
        """
        if option is not None and len(option) > 100:
            raise ValueError(
                "Invalid value for `option`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._option = option

    @property
    def status(self):
        """Gets the status of this TrackingCategory.  # noqa: E501

        The status of a tracking category  # noqa: E501

        :return: The status of this TrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrackingCategory.

        The status of a tracking category  # noqa: E501

        :param status: The status of this TrackingCategory.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ARCHIVED", "DELETED", "None"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def options(self):
        """Gets the options of this TrackingCategory.  # noqa: E501

        See Tracking Options  # noqa: E501

        :return: The options of this TrackingCategory.  # noqa: E501
        :rtype: list[TrackingOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TrackingCategory.

        See Tracking Options  # noqa: E501

        :param options: The options of this TrackingCategory.  # noqa: E501
        :type: list[TrackingOption]
        """

        self._options = options
