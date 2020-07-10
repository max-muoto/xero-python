# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class HomeAddress(BaseModel):
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
        "address_line1": "str",
        "address_line2": "str",
        "city": "str",
        "region": "State",
        "postal_code": "str",
        "country": "str",
    }

    attribute_map = {
        "address_line1": "AddressLine1",
        "address_line2": "AddressLine2",
        "city": "City",
        "region": "Region",
        "postal_code": "PostalCode",
        "country": "Country",
    }

    def __init__(
        self,
        address_line1=None,
        address_line2=None,
        city=None,
        region=None,
        postal_code=None,
        country=None,
    ):  # noqa: E501
        """HomeAddress - a model defined in OpenAPI"""  # noqa: E501

        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def address_line1(self):
        """Gets the address_line1 of this HomeAddress.  # noqa: E501

        Address line 1 for employee home address  # noqa: E501

        :return: The address_line1 of this HomeAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this HomeAddress.

        Address line 1 for employee home address  # noqa: E501

        :param address_line1: The address_line1 of this HomeAddress.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError(
                "Invalid value for `address_line1`, must not be `None`"
            )  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this HomeAddress.  # noqa: E501

        Address line 2 for employee home address  # noqa: E501

        :return: The address_line2 of this HomeAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this HomeAddress.

        Address line 2 for employee home address  # noqa: E501

        :param address_line2: The address_line2 of this HomeAddress.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this HomeAddress.  # noqa: E501

        Suburb for employee home address  # noqa: E501

        :return: The city of this HomeAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this HomeAddress.

        Suburb for employee home address  # noqa: E501

        :param city: The city of this HomeAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this HomeAddress.  # noqa: E501


        :return: The region of this HomeAddress.  # noqa: E501
        :rtype: State
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this HomeAddress.


        :param region: The region of this HomeAddress.  # noqa: E501
        :type: State
        """

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this HomeAddress.  # noqa: E501

        PostCode for employee home address  # noqa: E501

        :return: The postal_code of this HomeAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this HomeAddress.

        PostCode for employee home address  # noqa: E501

        :param postal_code: The postal_code of this HomeAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this HomeAddress.  # noqa: E501

        Country of HomeAddress  # noqa: E501

        :return: The country of this HomeAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this HomeAddress.

        Country of HomeAddress  # noqa: E501

        :param country: The country of this HomeAddress.  # noqa: E501
        :type: str
        """

        self._country = country
