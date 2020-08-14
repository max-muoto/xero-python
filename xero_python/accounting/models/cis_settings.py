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


class CISSettings(BaseModel):
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
    openapi_types = {"cis_settings": "list[CISSetting]"}

    attribute_map = {"cis_settings": "CISSettings"}

    def __init__(self, cis_settings=None):  # noqa: E501
        """CISSettings - a model defined in OpenAPI"""  # noqa: E501

        self._cis_settings = None
        self.discriminator = None

        if cis_settings is not None:
            self.cis_settings = cis_settings

    @property
    def cis_settings(self):
        """Gets the cis_settings of this CISSettings.  # noqa: E501


        :return: The cis_settings of this CISSettings.  # noqa: E501
        :rtype: list[CISSetting]
        """
        return self._cis_settings

    @cis_settings.setter
    def cis_settings(self, cis_settings):
        """Sets the cis_settings of this CISSettings.


        :param cis_settings: The cis_settings of this CISSettings.  # noqa: E501
        :type: list[CISSetting]
        """

        self._cis_settings = cis_settings
