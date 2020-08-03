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


class Element(BaseModel):
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
        "validation_errors": "list[ValidationError]",
        "batch_payment_id": "str",
        "bank_transaction_id": "str",
        "credit_note_id": "str",
        "contact_id": "str",
        "invoice_id": "str",
        "item_id": "str",
        "purchase_order_id": "str",
    }

    attribute_map = {
        "validation_errors": "ValidationErrors",
        "batch_payment_id": "BatchPaymentID",
        "bank_transaction_id": "BankTransactionID",
        "credit_note_id": "CreditNoteID",
        "contact_id": "ContactID",
        "invoice_id": "InvoiceID",
        "item_id": "ItemID",
        "purchase_order_id": "PurchaseOrderID",
    }

    def __init__(
        self,
        validation_errors=None,
        batch_payment_id=None,
        bank_transaction_id=None,
        credit_note_id=None,
        contact_id=None,
        invoice_id=None,
        item_id=None,
        purchase_order_id=None,
    ):  # noqa: E501
        """Element - a model defined in OpenAPI"""  # noqa: E501

        self._validation_errors = None
        self._batch_payment_id = None
        self._bank_transaction_id = None
        self._credit_note_id = None
        self._contact_id = None
        self._invoice_id = None
        self._item_id = None
        self._purchase_order_id = None
        self.discriminator = None

        if validation_errors is not None:
            self.validation_errors = validation_errors
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if bank_transaction_id is not None:
            self.bank_transaction_id = bank_transaction_id
        if credit_note_id is not None:
            self.credit_note_id = credit_note_id
        if contact_id is not None:
            self.contact_id = contact_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if item_id is not None:
            self.item_id = item_id
        if purchase_order_id is not None:
            self.purchase_order_id = purchase_order_id

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Element.  # noqa: E501

        Array of Validation Error message  # noqa: E501

        :return: The validation_errors of this Element.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Element.

        Array of Validation Error message  # noqa: E501

        :param validation_errors: The validation_errors of this Element.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

    @property
    def batch_payment_id(self):
        """Gets the batch_payment_id of this Element.  # noqa: E501

        Unique ID for batch payment object with validation error  # noqa: E501

        :return: The batch_payment_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        """Sets the batch_payment_id of this Element.

        Unique ID for batch payment object with validation error  # noqa: E501

        :param batch_payment_id: The batch_payment_id of this Element.  # noqa: E501
        :type: str
        """

        self._batch_payment_id = batch_payment_id

    @property
    def bank_transaction_id(self):
        """Gets the bank_transaction_id of this Element.  # noqa: E501


        :return: The bank_transaction_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._bank_transaction_id

    @bank_transaction_id.setter
    def bank_transaction_id(self, bank_transaction_id):
        """Sets the bank_transaction_id of this Element.


        :param bank_transaction_id: The bank_transaction_id of this Element.  # noqa: E501
        :type: str
        """

        self._bank_transaction_id = bank_transaction_id

    @property
    def credit_note_id(self):
        """Gets the credit_note_id of this Element.  # noqa: E501


        :return: The credit_note_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, credit_note_id):
        """Sets the credit_note_id of this Element.


        :param credit_note_id: The credit_note_id of this Element.  # noqa: E501
        :type: str
        """

        self._credit_note_id = credit_note_id

    @property
    def contact_id(self):
        """Gets the contact_id of this Element.  # noqa: E501


        :return: The contact_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this Element.


        :param contact_id: The contact_id of this Element.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this Element.  # noqa: E501


        :return: The invoice_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this Element.


        :param invoice_id: The invoice_id of this Element.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def item_id(self):
        """Gets the item_id of this Element.  # noqa: E501


        :return: The item_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Element.


        :param item_id: The item_id of this Element.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def purchase_order_id(self):
        """Gets the purchase_order_id of this Element.  # noqa: E501


        :return: The purchase_order_id of this Element.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, purchase_order_id):
        """Sets the purchase_order_id of this Element.


        :param purchase_order_id: The purchase_order_id of this Element.  # noqa: E501
        :type: str
        """

        self._purchase_order_id = purchase_order_id
