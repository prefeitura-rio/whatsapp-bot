"""
Message objects are a way of easing interaction with the messages
sent from the WhatsApp client.
"""
import json
from typing import List

from handler_api.utils import get_key


class Message: # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """
    Message objects are a way of easing interaction with the messages
    sent from the WhatsApp client.

    Attributes:
        - ack (int)
        - body (str)
        - broadcast (bool)
        - device_type (str)
        - ephemeral_out_of_sync (bool)
        - forwarding_score (int)
        - from (str)
        - from_me (bool)
        - has_media (bool)
        - has_quoted_message (bool)
        - has_reaction (bool)
        - id (str)
        - id_remote (str)
        - id_serialized (str)
        - is_dynamic_reply_buttons_message (bool)
        - is_ephemeral (bool)
        - is_forwarded (bool)
        - is_from_template (bool)
        - is_gif (bool)
        - is_md_history_message (bool)
        - is_new_message (bool)
        - is_starred (bool)
        - is_status (bool)
        - is_vcard_over_mms_document (bool)
        - last_playback_progress (int)
        - links (List[str])
        - mentioned_ids (List[str])
        - notify_name (str)
        - product_header_image_rejected (bool)
        - ppt_forwarded_features_enabled (bool)
        - recv_fresh (bool)
        - requires_direct_connection (bool)
        - service (str)
        - timestamp (int)
        - to (str)
        - type (str)
        - vcards (List[str])
    """


    def __init__(self, message_dict: dict):
        """
        Message objects are a way of easing interaction with the messages
        sent from the WhatsApp client.

        Attributes:
            - ack (int)
            - body (str)
            - broadcast (bool)
            - device_type (str)
            - ephemeral_out_of_sync (bool)
            - forwarding_score (int)
            - from (str)
            - from_me (bool)
            - has_media (bool)
            - has_quoted_message (bool)
            - has_reaction (bool)
            - id (str)
            - id_remote (str)
            - id_serialized (str)
            - is_dynamic_reply_buttons_message (bool)
            - is_ephemeral (bool)
            - is_forwarded (bool)
            - is_from_template (bool)
            - is_gif (bool)
            - is_md_history_message (bool)
            - is_new_message (bool)
            - is_starred (bool)
            - is_status (bool)
            - is_vcard_over_mms_document (bool)
            - last_playback_progress (int)
            - links (List[str])
            - mentioned_ids (List[str])
            - notify_name (str)
            - product_header_image_rejected (bool)
            - ppt_forwarded_features_enabled (bool)
            - recv_fresh (bool)
            - requires_direct_connection (bool)
            - service (str)
            - timestamp (int)
            - to (str)
            - type (str)
            - vcards (List[str])
        """
        # Let's keep the raw message
        self._raw_message: dict = message_dict

        # Then parse all attributes
        self._ack: int = get_key(message_dict, "ack", None)
        self._body: str = get_key(message_dict, "body") # This will raise if not found
        self._broadcast: bool = get_key(message_dict, "broadcast", None)
        self._device_type: str = get_key(message_dict, "deviceType", None)
        self._ephemeral_out_of_sync: bool = get_key(message_dict["_data"], "ephemeralOutOfSync", None)
        self._forwarding_score: int = get_key(message_dict, "forwardingScore", None)
        self._from: str = get_key(message_dict, "from") # This will raise if not found
        self._from_me: bool = get_key(message_dict, "fromMe", None)
        self._id: str = get_key(message_dict["id"], "id", None)
        self._id_remote: str = get_key(message_dict["id"], "remote", None)
        self._id_serialized: str = get_key(message_dict["id"], "_serialized", None)
        self._has_media: bool = get_key(message_dict, "hasMedia", None)
        self._has_quoted_message: bool = get_key(message_dict, "hasQuotedMessage", None)
        self._has_reaction: bool = get_key(message_dict["_data"], "hasReaction", None)
        self._is_dynamic_reply_buttons_message: bool = get_key(message_dict["_data"], "isDynamicReplyButtonsMsg", None)
        self._is_ephemeral: bool = get_key(message_dict, "isEphemeral", None)
        self._is_forwarded: bool = get_key(message_dict, "isForwarded", None)
        self._is_from_template: bool = get_key(message_dict["_data"], "isFromTemplate", None)
        self._is_gif: bool = get_key(message_dict, "isGif", None)
        self._is_md_history_message: bool = get_key(message_dict["_data"], "isMdHistoryMsg", None)
        self._is_new_message: bool = get_key(message_dict["_data"], "isNewMsg", None)
        self._is_starred: bool = get_key(message_dict, "isStarred", None)
        self._is_status: bool = get_key(message_dict, "isStatus", None)
        self._is_vcard_over_mms_document: bool = get_key(message_dict["_data"], "isVcardOverMmsDocument", None)
        self._last_playback_progress: int = get_key(message_dict["_data"], "lastPlaybackProgress", None)
        self._links: List[str] = get_key(message_dict, "links", None)
        self._mentioned_ids: List[str] = get_key(message_dict, "mentionedIds", None)
        self._notify_name: str = get_key(message_dict["_data"], "notifyName", None)
        self._product_header_image_rejected: bool = get_key(message_dict["_data"], "productHeaderImageRejected", None)
        self._ppt_forwarded_features_enabled: bool = get_key(message_dict["_data"], "pttForwardedFeaturesEnabled", None)
        self._recv_fresh: bool = get_key(message_dict["_data"], "recvFresh", None)
        self._requires_direct_connection: bool = get_key(message_dict["_data"], "requiresDirectConnection", None)
        self._service: str = get_key(message_dict, "service", None)
        self._timestamp: int = get_key(message_dict, "timestamp") # This will raise if not found
        self._to: str = get_key(message_dict, "to", None)
        self._type: str = get_key(message_dict, "type", None)
        self._vcards: List[str] = get_key(message_dict, "vCards", None)

    def __str__(self):
        return f"Message from \"{self._from}\" to \"{self._to}\" with body \"{self._body}\""

    def __repr__(self):
        return self.__str__()

    @property
    def ack(self) -> int:
        """
        The ack value of the message.

        Returns:
            - int: The ack value of the message.
        """
        return self._ack

    @property
    def body(self) -> str:
        """
        The body of the message.

        Returns:
            - str: The body of the message.
        """
        return self._body

    @property
    def broadcast(self) -> bool:
        """
        Whether the message is broadcast.

        Returns:
            - bool: Whether the message is broadcast.
        """
        return self._broadcast

    @property
    def device_type(self) -> str:
        """
        The device type of the message.

        Returns:
            - str: The device type of the message.
        """
        return self._device_type

    @property
    def ephemeral_out_of_sync(self) -> bool:
        """
        Whether the ephemeral message is out of sync.

        Returns:
            - bool: Whether the ephemeral message is out of sync.
        """
        return self._ephemeral_out_of_sync

    @property
    def forwarding_score(self) -> int:
        """
        The forwarding score of the message.

        Returns:
            - int: The forwarding score of the message.
        """
        return self._forwarding_score

    @property
    def from_ (self) -> str:
        """
        The sender of the message.

        Returns:
            - str: The sender of the message.
        """
        return self._from

    @property
    def from_me(self) -> bool:
        """
        Whether the message is from me.

        Returns:
            - bool: Whether the message is from me.
        """
        return self._from_me

    @property
    def has_media(self) -> bool:
        """
        Whether the message has media.

        Returns:
            - bool: Whether the message has media.
        """
        return self._has_media

    @property
    def has_quoted_message(self) -> bool:
        """
        Whether the message has a quoted message.

        Returns:
            - bool: Whether the message has a quoted message.
        """
        return self._has_quoted_message

    @property
    def has_reaction(self) -> bool:
        """
        Whether the message has a reaction.

        Returns:
            - bool: Whether the message has a reaction.
        """
        return self._has_reaction

    @property
    def id_(self) -> str:
        """
        The id of the message.

        Returns:
            - str: The id of the message.
        """
        return self._id

    @property
    def id_remote(self) -> str:
        """
        The remote id of the message.

        Returns:
            - str: The remote id of the message.
        """
        return self._id_remote

    @property
    def id_serialized(self) -> str:
        """
        The serialized id of the message.

        Returns:
            - str: The serialized id of the message.
        """
        return self._id_serialized

    @property
    def is_dynamic_reply_buttons_message(self) -> bool:
        """
        Whether the message is a dynamic reply buttons message.

        Returns:
            - bool: Whether the message is a dynamic reply buttons message.
        """
        return self._is_dynamic_reply_buttons_message

    @property
    def is_ephemeral(self) -> bool:
        """
        Whether the message is an ephemeral message.

        Returns:
            - bool: Whether the message is an ephemeral message.
        """
        return self._is_ephemeral

    @property
    def is_forwarded(self) -> bool:
        """
        Whether the message is forwarded.

        Returns:
            - bool: Whether the message is forwarded.
        """
        return self._is_forwarded

    @property
    def is_from_template(self) -> bool:
        """
        Whether the message is from a template.

        Returns:
            - bool: Whether the message is from a template.
        """
        return self._is_from_template

    @property
    def is_gif(self) -> bool:
        """
        Whether the message is a gif.

        Returns:
            - bool: Whether the message is a gif.
        """
        return self._is_gif

    @property
    def is_md_history_message(self) -> bool:
        """
        Whether the message is a markdown history message.

        Returns:
            - bool: Whether the message is a markdown history message.
        """
        return self._is_md_history_message

    @property
    def is_new_message(self) -> bool:
        """
        Whether the message is a new message.

        Returns:
            - bool: Whether the message is a new message.
        """
        return self._is_new_message

    @property
    def is_starred(self) -> bool:
        """
        Whether the message is starred.

        Returns:
            - bool: Whether the message is starred.
        """
        return self._is_starred

    @property
    def is_status(self) -> bool:
        """
        Whether the message is a status message.

        Returns:
            - bool: Whether the message is a status message.
        """
        return self._is_status

    @property
    def is_vcard_over_mms_document(self) -> bool:
        """
        Whether the message is a vcard over mms document.

        Returns:
            - bool: Whether the message is a vcard over mms document.
        """
        return self._is_vcard_over_mms_document

    @property
    def last_playback_progress(self) -> int:
        """
        The last playback progress of the message.

        Returns:
            - int: The last playback progress of the message.
        """
        return self._last_playback_progress

    @property
    def links(self) -> List[str]:
        """
        The links of the message.

        Returns:
            - List[str]: The links of the message.
        """
        return self._links

    @property
    def mentioned_ids(self) -> List[str]:
        """
        The mentioned ids of the message.

        Returns:
            - List[str]: The mentioned ids of the message.
        """
        return self._mentioned_ids

    @property
    def notify_name(self) -> str:
        """
        The notify name of the message.

        Returns:
            - str: The notify name of the message.
        """
        return self._notify_name

    @property
    def product_header_image_rejected(self) -> bool:
        """
        Whether the product header image is rejected.

        Returns:
            - bool: Whether the product header image is rejected.
        """
        return self._product_header_image_rejected

    @property
    def ppt_forwarded_features_enabled(self) -> bool:
        """
        Whether the ppt forwarded features are enabled.

        Returns:
            - bool: Whether the ppt forwarded features are enabled.
        """
        return self._ppt_forwarded_features_enabled

    @property
    def recv_fresh(self) -> bool:
        """
        Whether the message is received fresh.

        Returns:
            - bool: Whether the message is received fresh.
        """
        return self._recv_fresh

    @property
    def requires_direct_connection(self) -> bool:
        """
        Whether the message requires direct connection.

        Returns:
            - bool: Whether the message requires direct connection.
        """
        return self._requires_direct_connection

    @property
    def service(self) -> str:
        """
        The service of the message.

        Returns:
            - str: The service of the message.
        """
        return self._service

    @property
    def timestamp(self) -> int:
        """
        The timestamp of the message.

        Returns:
            - int: The timestamp of the message.
        """
        return self._timestamp

    @property
    def to_(self) -> str:
        """
        The to of the message.

        Returns:
            - str: The to of the message.
        """
        return self._to

    @property
    def type_(self) -> str:
        """
        The type of the message.

        Returns:
            - str: The type of the message.
        """
        return self._type

    @property
    def vcards(self) -> List[str]:
        """
        The vcards of the message.

        Returns:
            - List[str]: The vcards of the message.
        """
        return self._vcards
