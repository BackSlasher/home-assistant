"""Web socket API for Z-Wave."""

import logging

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import callback

from . import (
    _collect_networks,
)

from .const import (
    CONF_AUTOHEAL,
    CONF_DEBUG,
    CONF_POLLING_INTERVAL,
    CONF_USB_STICK_PATH,
    DATA_NETWORKS,
    DATA_ZWAVE_CONFIG,
)

_LOGGER = logging.getLogger(__name__)

TYPE = "type"
ID = "id"

# XXX bad
from typing import NamedTuple, Any
class DummyService
    data: Any

@websocket_api.require_admin
@websocket_api.websocket_command({vol.Required(TYPE): "zwave/network_status"})
def websocket_network_status(hass, connection, msg):
    """Get Z-Wave network status."""
    # XXX provide a better solution
    dummy_service = Dummyservice(data=msg)
    networks = _collect_networks(dummy_service)
    network = (networks.values())[0]
    _LOGGER.info("aaaaaa", network)
    connection.send_result(msg[ID], {"state": network.state})


@websocket_api.require_admin
@websocket_api.websocket_command({vol.Required(TYPE): "zwave/get_config"})
def websocket_get_config(hass, connection, msg):
    """Get Z-Wave configuration."""
    config = hass.data[DATA_ZWAVE_CONFIG]
    connection.send_result(
        msg[ID],
        {
            CONF_AUTOHEAL: config[CONF_AUTOHEAL],
            CONF_DEBUG: config[CONF_DEBUG],
            CONF_POLLING_INTERVAL: config[CONF_POLLING_INTERVAL],
            # XXX we're going to change this interface
            CONF_USB_STICK_PATH: config[CONF_USB_STICK_PATH],
        },
    )


@callback
def async_load_websocket_api(hass):
    """Set up the web socket API."""
    websocket_api.async_register_command(hass, websocket_network_status)
    websocket_api.async_register_command(hass, websocket_get_config)
