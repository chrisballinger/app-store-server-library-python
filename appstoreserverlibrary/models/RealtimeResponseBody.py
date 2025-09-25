# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr

@define
class RealtimeResponseBody:
    """
    A response you provide to choose, in real time, a retention message the system displays to the customer.

    https://developer.apple.com/documentation/retentionmessaging/realtimeresponsebody
    """

    message: Optional[str] = attr.ib(default=None)
    """
    A retention message that's text-based and can include an optional image. If you supply this field, don't include the other fields.

    https://developer.apple.com/documentation/retentionmessaging/message
    """

    alternateProduct: Optional[str] = attr.ib(default=None)
    """
    A retention message with a switch-plan option. If you supply this field, don't include the other fields.

    https://developer.apple.com/documentation/retentionmessaging/alternateproduct
    """

    promotionalOffer: Optional[str] = attr.ib(default=None)
    """
    A retention message that includes a promotional offer. If you supply this field, don't include the other fields.

    https://developer.apple.com/documentation/retentionmessaging/promotionaloffer
    """