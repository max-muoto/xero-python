# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ReportWithRow(BaseModel):
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
        "report_id": "str",
        "report_name": "str",
        "report_title": "str",
        "report_type": "str",
        "report_titles": "list[str]",
        "report_date": "str",
        "rows": "list[ReportRows]",
        "updated_date_utc": "datetime[ms-format]",
        "fields": "list[ReportFields]",
    }

    attribute_map = {
        "report_id": "ReportID",
        "report_name": "ReportName",
        "report_title": "ReportTitle",
        "report_type": "ReportType",
        "report_titles": "ReportTitles",
        "report_date": "ReportDate",
        "rows": "Rows",
        "updated_date_utc": "UpdatedDateUTC",
        "fields": "Fields",
    }

    def __init__(
        self,
        report_id=None,
        report_name=None,
        report_title=None,
        report_type=None,
        report_titles=None,
        report_date=None,
        rows=None,
        updated_date_utc=None,
        fields=None,
    ):  # noqa: E501
        """ReportWithRow - a model defined in OpenAPI"""  # noqa: E501

        self._report_id = None
        self._report_name = None
        self._report_title = None
        self._report_type = None
        self._report_titles = None
        self._report_date = None
        self._rows = None
        self._updated_date_utc = None
        self._fields = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if report_title is not None:
            self.report_title = report_title
        if report_type is not None:
            self.report_type = report_type
        if report_titles is not None:
            self.report_titles = report_titles
        if report_date is not None:
            self.report_date = report_date
        if rows is not None:
            self.rows = rows
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if fields is not None:
            self.fields = fields

    @property
    def report_id(self):
        """Gets the report_id of this ReportWithRow.  # noqa: E501

        Report id  # noqa: E501

        :return: The report_id of this ReportWithRow.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportWithRow.

        Report id  # noqa: E501

        :param report_id: The report_id of this ReportWithRow.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def report_name(self):
        """Gets the report_name of this ReportWithRow.  # noqa: E501

        Name of the report  # noqa: E501

        :return: The report_name of this ReportWithRow.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ReportWithRow.

        Name of the report  # noqa: E501

        :param report_name: The report_name of this ReportWithRow.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_title(self):
        """Gets the report_title of this ReportWithRow.  # noqa: E501

        Title of the report  # noqa: E501

        :return: The report_title of this ReportWithRow.  # noqa: E501
        :rtype: str
        """
        return self._report_title

    @report_title.setter
    def report_title(self, report_title):
        """Sets the report_title of this ReportWithRow.

        Title of the report  # noqa: E501

        :param report_title: The report_title of this ReportWithRow.  # noqa: E501
        :type: str
        """

        self._report_title = report_title

    @property
    def report_type(self):
        """Gets the report_type of this ReportWithRow.  # noqa: E501

        The type of report (BalanceSheet,ProfitLoss, etc)  # noqa: E501

        :return: The report_type of this ReportWithRow.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportWithRow.

        The type of report (BalanceSheet,ProfitLoss, etc)  # noqa: E501

        :param report_type: The report_type of this ReportWithRow.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def report_titles(self):
        """Gets the report_titles of this ReportWithRow.  # noqa: E501

        Report titles array (3 to 4 strings with the report name, orgnisation name and time frame of report)  # noqa: E501

        :return: The report_titles of this ReportWithRow.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_titles

    @report_titles.setter
    def report_titles(self, report_titles):
        """Sets the report_titles of this ReportWithRow.

        Report titles array (3 to 4 strings with the report name, orgnisation name and time frame of report)  # noqa: E501

        :param report_titles: The report_titles of this ReportWithRow.  # noqa: E501
        :type: list[str]
        """

        self._report_titles = report_titles

    @property
    def report_date(self):
        """Gets the report_date of this ReportWithRow.  # noqa: E501

        Date of report  # noqa: E501

        :return: The report_date of this ReportWithRow.  # noqa: E501
        :rtype: str
        """
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        """Sets the report_date of this ReportWithRow.

        Date of report  # noqa: E501

        :param report_date: The report_date of this ReportWithRow.  # noqa: E501
        :type: str
        """

        self._report_date = report_date

    @property
    def rows(self):
        """Gets the rows of this ReportWithRow.  # noqa: E501


        :return: The rows of this ReportWithRow.  # noqa: E501
        :rtype: list[ReportRows]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ReportWithRow.


        :param rows: The rows of this ReportWithRow.  # noqa: E501
        :type: list[ReportRows]
        """

        self._rows = rows

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this ReportWithRow.  # noqa: E501

        Updated Date  # noqa: E501

        :return: The updated_date_utc of this ReportWithRow.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this ReportWithRow.

        Updated Date  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this ReportWithRow.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def fields(self):
        """Gets the fields of this ReportWithRow.  # noqa: E501


        :return: The fields of this ReportWithRow.  # noqa: E501
        :rtype: list[ReportFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ReportWithRow.


        :param fields: The fields of this ReportWithRow.  # noqa: E501
        :type: list[ReportFields]
        """

        self._fields = fields
