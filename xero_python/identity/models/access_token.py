# coding: utf-8

"""
    Xero oAuth 2 identity service

    This specifing endpoints related to managing authentication tokens and identity for Xero API  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class AccessToken(BaseModel):
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
        "id_token": "str",
        "access_token": "str",
        "expires_in": "float",
        "token_type": "str",
        "refresh_token": "str",
    }

    attribute_map = {
        "id_token": "id_token",
        "access_token": "access_token",
        "expires_in": "expires_in",
        "token_type": "token_type",
        "refresh_token": "refresh_token",
    }

    def __init__(
        self,
        id_token=None,
        access_token=None,
        expires_in=None,
        token_type=None,
        refresh_token=None,
    ):  # noqa: E501
        """AccessToken - a model defined in OpenAPI"""  # noqa: E501

        self._id_token = None
        self._access_token = None
        self._expires_in = None
        self._token_type = None
        self._refresh_token = None
        self.discriminator = None

        if id_token is not None:
            self.id_token = id_token
        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if token_type is not None:
            self.token_type = token_type
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def id_token(self):
        """Gets the id_token of this AccessToken.  # noqa: E501

        Xero unique identifier  # noqa: E501

        :return: The id_token of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this AccessToken.

        Xero unique identifier  # noqa: E501

        :param id_token: The id_token of this AccessToken.  # noqa: E501
        :type: str
        """

        self._id_token = id_token

    @property
    def access_token(self):
        """Gets the access_token of this AccessToken.  # noqa: E501

        access token provided during authentication flow  # noqa: E501

        :return: The access_token of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this AccessToken.

        access token provided during authentication flow  # noqa: E501

        :param access_token: The access_token of this AccessToken.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this AccessToken.  # noqa: E501

        time in milliseconds until access token expires.  # noqa: E501

        :return: The expires_in of this AccessToken.  # noqa: E501
        :rtype: float
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AccessToken.

        time in milliseconds until access token expires.  # noqa: E501

        :param expires_in: The expires_in of this AccessToken.  # noqa: E501
        :type: float
        """

        self._expires_in = expires_in

    @property
    def token_type(self):
        """Gets the token_type of this AccessToken.  # noqa: E501

        type of token i.e. Bearer  # noqa: E501

        :return: The token_type of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this AccessToken.

        type of token i.e. Bearer  # noqa: E501

        :param token_type: The token_type of this AccessToken.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AccessToken.  # noqa: E501

        token used to refresh an expired access token  # noqa: E501

        :return: The refresh_token of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AccessToken.

        token used to refresh an expired access token  # noqa: E501

        :param refresh_token: The refresh_token of this AccessToken.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token
