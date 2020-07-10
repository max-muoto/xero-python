# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Invoice(BaseModel):
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
        "type": "str",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "date": "date[ms-format]",
        "due_date": "date[ms-format]",
        "line_amount_types": "LineAmountTypes",
        "invoice_number": "str",
        "reference": "str",
        "branding_theme_id": "str",
        "url": "str",
        "currency_code": "CurrencyCode",
        "currency_rate": "float",
        "status": "str",
        "sent_to_contact": "bool",
        "expected_payment_date": "date[ms-format]",
        "planned_payment_date": "date[ms-format]",
        "cis_deduction": "float",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "total_discount": "float",
        "invoice_id": "str",
        "has_attachments": "bool",
        "is_discounted": "bool",
        "payments": "list[Payment]",
        "prepayments": "list[Prepayment]",
        "overpayments": "list[Overpayment]",
        "amount_due": "float",
        "amount_paid": "float",
        "fully_paid_on_date": "date[ms-format]",
        "amount_credited": "float",
        "updated_date_utc": "datetime[ms-format]",
        "credit_notes": "list[CreditNote]",
        "attachments": "list[Attachment]",
        "has_errors": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
    }

    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "line_items": "LineItems",
        "date": "Date",
        "due_date": "DueDate",
        "line_amount_types": "LineAmountTypes",
        "invoice_number": "InvoiceNumber",
        "reference": "Reference",
        "branding_theme_id": "BrandingThemeID",
        "url": "Url",
        "currency_code": "CurrencyCode",
        "currency_rate": "CurrencyRate",
        "status": "Status",
        "sent_to_contact": "SentToContact",
        "expected_payment_date": "ExpectedPaymentDate",
        "planned_payment_date": "PlannedPaymentDate",
        "cis_deduction": "CISDeduction",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "total_discount": "TotalDiscount",
        "invoice_id": "InvoiceID",
        "has_attachments": "HasAttachments",
        "is_discounted": "IsDiscounted",
        "payments": "Payments",
        "prepayments": "Prepayments",
        "overpayments": "Overpayments",
        "amount_due": "AmountDue",
        "amount_paid": "AmountPaid",
        "fully_paid_on_date": "FullyPaidOnDate",
        "amount_credited": "AmountCredited",
        "updated_date_utc": "UpdatedDateUTC",
        "credit_notes": "CreditNotes",
        "attachments": "Attachments",
        "has_errors": "HasErrors",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        line_items=None,
        date=None,
        due_date=None,
        line_amount_types=None,
        invoice_number=None,
        reference=None,
        branding_theme_id=None,
        url=None,
        currency_code=None,
        currency_rate=None,
        status=None,
        sent_to_contact=None,
        expected_payment_date=None,
        planned_payment_date=None,
        cis_deduction=None,
        sub_total=None,
        total_tax=None,
        total=None,
        total_discount=None,
        invoice_id=None,
        has_attachments=False,
        is_discounted=None,
        payments=None,
        prepayments=None,
        overpayments=None,
        amount_due=None,
        amount_paid=None,
        fully_paid_on_date=None,
        amount_credited=None,
        updated_date_utc=None,
        credit_notes=None,
        attachments=None,
        has_errors=False,
        status_attribute_string=None,
        validation_errors=None,
        warnings=None,
    ):  # noqa: E501
        """Invoice - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._contact = None
        self._line_items = None
        self._date = None
        self._due_date = None
        self._line_amount_types = None
        self._invoice_number = None
        self._reference = None
        self._branding_theme_id = None
        self._url = None
        self._currency_code = None
        self._currency_rate = None
        self._status = None
        self._sent_to_contact = None
        self._expected_payment_date = None
        self._planned_payment_date = None
        self._cis_deduction = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._total_discount = None
        self._invoice_id = None
        self._has_attachments = None
        self._is_discounted = None
        self._payments = None
        self._prepayments = None
        self._overpayments = None
        self._amount_due = None
        self._amount_paid = None
        self._fully_paid_on_date = None
        self._amount_credited = None
        self._updated_date_utc = None
        self._credit_notes = None
        self._attachments = None
        self._has_errors = None
        self._status_attribute_string = None
        self._validation_errors = None
        self._warnings = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if date is not None:
            self.date = date
        if due_date is not None:
            self.due_date = due_date
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if reference is not None:
            self.reference = reference
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if url is not None:
            self.url = url
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if status is not None:
            self.status = status
        if sent_to_contact is not None:
            self.sent_to_contact = sent_to_contact
        if expected_payment_date is not None:
            self.expected_payment_date = expected_payment_date
        if planned_payment_date is not None:
            self.planned_payment_date = planned_payment_date
        if cis_deduction is not None:
            self.cis_deduction = cis_deduction
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_discount is not None:
            self.total_discount = total_discount
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if is_discounted is not None:
            self.is_discounted = is_discounted
        if payments is not None:
            self.payments = payments
        if prepayments is not None:
            self.prepayments = prepayments
        if overpayments is not None:
            self.overpayments = overpayments
        if amount_due is not None:
            self.amount_due = amount_due
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if fully_paid_on_date is not None:
            self.fully_paid_on_date = fully_paid_on_date
        if amount_credited is not None:
            self.amount_credited = amount_credited
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if credit_notes is not None:
            self.credit_notes = credit_notes
        if attachments is not None:
            self.attachments = attachments
        if has_errors is not None:
            self.has_errors = has_errors
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings

    @property
    def type(self):
        """Gets the type of this Invoice.  # noqa: E501

        See Invoice Types  # noqa: E501

        :return: The type of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Invoice.

        See Invoice Types  # noqa: E501

        :param type: The type of this Invoice.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ACCPAY",
            "ACCPAYCREDIT",
            "APOVERPAYMENT",
            "APPREPAYMENT",
            "ACCREC",
            "ACCRECCREDIT",
            "AROVERPAYMENT",
            "ARPREPAYMENT",
        ]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def contact(self):
        """Gets the contact of this Invoice.  # noqa: E501


        :return: The contact of this Invoice.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Invoice.


        :param contact: The contact of this Invoice.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def line_items(self):
        """Gets the line_items of this Invoice.  # noqa: E501

        See LineItems  # noqa: E501

        :return: The line_items of this Invoice.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Invoice.

        See LineItems  # noqa: E501

        :param line_items: The line_items of this Invoice.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def date(self):
        """Gets the date of this Invoice.  # noqa: E501

        Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :return: The date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Invoice.

        Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :param date: The date of this Invoice.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def due_date(self):
        """Gets the due_date of this Invoice.  # noqa: E501

        Date invoice is due – YYYY-MM-DD  # noqa: E501

        :return: The due_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Invoice.

        Date invoice is due – YYYY-MM-DD  # noqa: E501

        :param due_date: The due_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this Invoice.  # noqa: E501


        :return: The line_amount_types of this Invoice.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this Invoice.


        :param line_amount_types: The line_amount_types of this Invoice.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Invoice.  # noqa: E501

        ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length = 255)  # noqa: E501

        :return: The invoice_number of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Invoice.

        ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length = 255)  # noqa: E501

        :param invoice_number: The invoice_number of this Invoice.  # noqa: E501
        :type: str
        """
        if invoice_number is not None and len(invoice_number) > 255:
            raise ValueError(
                "Invalid value for `invoice_number`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._invoice_number = invoice_number

    @property
    def reference(self):
        """Gets the reference of this Invoice.  # noqa: E501

        ACCREC only – additional reference number (max length = 255)  # noqa: E501

        :return: The reference of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Invoice.

        ACCREC only – additional reference number (max length = 255)  # noqa: E501

        :param reference: The reference of this Invoice.  # noqa: E501
        :type: str
        """
        if reference is not None and len(reference) > 255:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._reference = reference

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this Invoice.  # noqa: E501

        See BrandingThemes  # noqa: E501

        :return: The branding_theme_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this Invoice.

        See BrandingThemes  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def url(self):
        """Gets the url of this Invoice.  # noqa: E501

        URL link to a source document – shown as “Go to [appName]” in the Xero app  # noqa: E501

        :return: The url of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Invoice.

        URL link to a source document – shown as “Go to [appName]” in the Xero app  # noqa: E501

        :param url: The url of this Invoice.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def currency_code(self):
        """Gets the currency_code of this Invoice.  # noqa: E501


        :return: The currency_code of this Invoice.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Invoice.


        :param currency_code: The currency_code of this Invoice.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def currency_rate(self):
        """Gets the currency_rate of this Invoice.  # noqa: E501

        The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length = [18].[6])  # noqa: E501

        :return: The currency_rate of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this Invoice.

        The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length = [18].[6])  # noqa: E501

        :param currency_rate: The currency_rate of this Invoice.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501

        See Invoice Status Codes  # noqa: E501

        :return: The status of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.

        See Invoice Status Codes  # noqa: E501

        :param status: The status of this Invoice.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "DELETED",
            "AUTHORISED",
            "PAID",
            "VOIDED",
        ]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def sent_to_contact(self):
        """Gets the sent_to_contact of this Invoice.  # noqa: E501

        Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved  # noqa: E501

        :return: The sent_to_contact of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._sent_to_contact

    @sent_to_contact.setter
    def sent_to_contact(self, sent_to_contact):
        """Sets the sent_to_contact of this Invoice.

        Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved  # noqa: E501

        :param sent_to_contact: The sent_to_contact of this Invoice.  # noqa: E501
        :type: bool
        """

        self._sent_to_contact = sent_to_contact

    @property
    def expected_payment_date(self):
        """Gets the expected_payment_date of this Invoice.  # noqa: E501

        Shown on sales invoices (Accounts Receivable) when this has been set  # noqa: E501

        :return: The expected_payment_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._expected_payment_date

    @expected_payment_date.setter
    def expected_payment_date(self, expected_payment_date):
        """Sets the expected_payment_date of this Invoice.

        Shown on sales invoices (Accounts Receivable) when this has been set  # noqa: E501

        :param expected_payment_date: The expected_payment_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._expected_payment_date = expected_payment_date

    @property
    def planned_payment_date(self):
        """Gets the planned_payment_date of this Invoice.  # noqa: E501

        Shown on bills (Accounts Payable) when this has been set  # noqa: E501

        :return: The planned_payment_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._planned_payment_date

    @planned_payment_date.setter
    def planned_payment_date(self, planned_payment_date):
        """Sets the planned_payment_date of this Invoice.

        Shown on bills (Accounts Payable) when this has been set  # noqa: E501

        :param planned_payment_date: The planned_payment_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._planned_payment_date = planned_payment_date

    @property
    def cis_deduction(self):
        """Gets the cis_deduction of this Invoice.  # noqa: E501

        CIS deduction for UK contractors  # noqa: E501

        :return: The cis_deduction of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._cis_deduction

    @cis_deduction.setter
    def cis_deduction(self, cis_deduction):
        """Sets the cis_deduction of this Invoice.

        CIS deduction for UK contractors  # noqa: E501

        :param cis_deduction: The cis_deduction of this Invoice.  # noqa: E501
        :type: float
        """

        self._cis_deduction = cis_deduction

    @property
    def sub_total(self):
        """Gets the sub_total of this Invoice.  # noqa: E501

        Total of invoice excluding taxes  # noqa: E501

        :return: The sub_total of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this Invoice.

        Total of invoice excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this Invoice.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this Invoice.  # noqa: E501

        Total tax on invoice  # noqa: E501

        :return: The total_tax of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this Invoice.

        Total tax on invoice  # noqa: E501

        :param total_tax: The total_tax of this Invoice.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this Invoice.  # noqa: E501

        Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts  # noqa: E501

        :return: The total of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Invoice.

        Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts  # noqa: E501

        :param total: The total of this Invoice.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_discount(self):
        """Gets the total_discount of this Invoice.  # noqa: E501

        Total of discounts applied on the invoice line items  # noqa: E501

        :return: The total_discount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """Sets the total_discount of this Invoice.

        Total of discounts applied on the invoice line items  # noqa: E501

        :param total_discount: The total_discount of this Invoice.  # noqa: E501
        :type: float
        """

        self._total_discount = total_discount

    @property
    def invoice_id(self):
        """Gets the invoice_id of this Invoice.  # noqa: E501

        Xero generated unique identifier for invoice  # noqa: E501

        :return: The invoice_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this Invoice.

        Xero generated unique identifier for invoice  # noqa: E501

        :param invoice_id: The invoice_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def has_attachments(self):
        """Gets the has_attachments of this Invoice.  # noqa: E501

        boolean to indicate if an invoice has an attachment  # noqa: E501

        :return: The has_attachments of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this Invoice.

        boolean to indicate if an invoice has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this Invoice.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def is_discounted(self):
        """Gets the is_discounted of this Invoice.  # noqa: E501

        boolean to indicate if an invoice has a discount  # noqa: E501

        :return: The is_discounted of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._is_discounted

    @is_discounted.setter
    def is_discounted(self, is_discounted):
        """Sets the is_discounted of this Invoice.

        boolean to indicate if an invoice has a discount  # noqa: E501

        :param is_discounted: The is_discounted of this Invoice.  # noqa: E501
        :type: bool
        """

        self._is_discounted = is_discounted

    @property
    def payments(self):
        """Gets the payments of this Invoice.  # noqa: E501

        See Payments  # noqa: E501

        :return: The payments of this Invoice.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Invoice.

        See Payments  # noqa: E501

        :param payments: The payments of this Invoice.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def prepayments(self):
        """Gets the prepayments of this Invoice.  # noqa: E501

        See Prepayments  # noqa: E501

        :return: The prepayments of this Invoice.  # noqa: E501
        :rtype: list[Prepayment]
        """
        return self._prepayments

    @prepayments.setter
    def prepayments(self, prepayments):
        """Sets the prepayments of this Invoice.

        See Prepayments  # noqa: E501

        :param prepayments: The prepayments of this Invoice.  # noqa: E501
        :type: list[Prepayment]
        """

        self._prepayments = prepayments

    @property
    def overpayments(self):
        """Gets the overpayments of this Invoice.  # noqa: E501

        See Overpayments  # noqa: E501

        :return: The overpayments of this Invoice.  # noqa: E501
        :rtype: list[Overpayment]
        """
        return self._overpayments

    @overpayments.setter
    def overpayments(self, overpayments):
        """Sets the overpayments of this Invoice.

        See Overpayments  # noqa: E501

        :param overpayments: The overpayments of this Invoice.  # noqa: E501
        :type: list[Overpayment]
        """

        self._overpayments = overpayments

    @property
    def amount_due(self):
        """Gets the amount_due of this Invoice.  # noqa: E501

        Amount remaining to be paid on invoice  # noqa: E501

        :return: The amount_due of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """Sets the amount_due of this Invoice.

        Amount remaining to be paid on invoice  # noqa: E501

        :param amount_due: The amount_due of this Invoice.  # noqa: E501
        :type: float
        """

        self._amount_due = amount_due

    @property
    def amount_paid(self):
        """Gets the amount_paid of this Invoice.  # noqa: E501

        Sum of payments received for invoice  # noqa: E501

        :return: The amount_paid of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this Invoice.

        Sum of payments received for invoice  # noqa: E501

        :param amount_paid: The amount_paid of this Invoice.  # noqa: E501
        :type: float
        """

        self._amount_paid = amount_paid

    @property
    def fully_paid_on_date(self):
        """Gets the fully_paid_on_date of this Invoice.  # noqa: E501

        The date the invoice was fully paid. Only returned on fully paid invoices  # noqa: E501

        :return: The fully_paid_on_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._fully_paid_on_date

    @fully_paid_on_date.setter
    def fully_paid_on_date(self, fully_paid_on_date):
        """Sets the fully_paid_on_date of this Invoice.

        The date the invoice was fully paid. Only returned on fully paid invoices  # noqa: E501

        :param fully_paid_on_date: The fully_paid_on_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._fully_paid_on_date = fully_paid_on_date

    @property
    def amount_credited(self):
        """Gets the amount_credited of this Invoice.  # noqa: E501

        Sum of all credit notes, over-payments and pre-payments applied to invoice  # noqa: E501

        :return: The amount_credited of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._amount_credited

    @amount_credited.setter
    def amount_credited(self, amount_credited):
        """Sets the amount_credited of this Invoice.

        Sum of all credit notes, over-payments and pre-payments applied to invoice  # noqa: E501

        :param amount_credited: The amount_credited of this Invoice.  # noqa: E501
        :type: float
        """

        self._amount_credited = amount_credited

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Invoice.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Invoice.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Invoice.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def credit_notes(self):
        """Gets the credit_notes of this Invoice.  # noqa: E501

        Details of credit notes that have been applied to an invoice  # noqa: E501

        :return: The credit_notes of this Invoice.  # noqa: E501
        :rtype: list[CreditNote]
        """
        return self._credit_notes

    @credit_notes.setter
    def credit_notes(self, credit_notes):
        """Sets the credit_notes of this Invoice.

        Details of credit notes that have been applied to an invoice  # noqa: E501

        :param credit_notes: The credit_notes of this Invoice.  # noqa: E501
        :type: list[CreditNote]
        """

        self._credit_notes = credit_notes

    @property
    def attachments(self):
        """Gets the attachments of this Invoice.  # noqa: E501

        Displays array of attachments from the API  # noqa: E501

        :return: The attachments of this Invoice.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Invoice.

        Displays array of attachments from the API  # noqa: E501

        :param attachments: The attachments of this Invoice.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments

    @property
    def has_errors(self):
        """Gets the has_errors of this Invoice.  # noqa: E501

        A boolean to indicate if a invoice has an validation errors  # noqa: E501

        :return: The has_errors of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._has_errors

    @has_errors.setter
    def has_errors(self, has_errors):
        """Sets the has_errors of this Invoice.

        A boolean to indicate if a invoice has an validation errors  # noqa: E501

        :param has_errors: The has_errors of this Invoice.  # noqa: E501
        :type: bool
        """

        self._has_errors = has_errors

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this Invoice.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this Invoice.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this Invoice.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Invoice.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Invoice.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Invoice.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Invoice.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

    @property
    def warnings(self):
        """Gets the warnings of this Invoice.  # noqa: E501

        Displays array of warning messages from the API  # noqa: E501

        :return: The warnings of this Invoice.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this Invoice.

        Displays array of warning messages from the API  # noqa: E501

        :param warnings: The warnings of this Invoice.  # noqa: E501
        :type: list[ValidationError]
        """

        self._warnings = warnings
