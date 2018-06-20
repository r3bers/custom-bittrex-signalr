#!/usr/bin/python
# -*- coding: utf-8 -*-

# bittrex_signalr/constants.py
# Stanislav Lazarov


class Constant(object):
    """
    Event is base class providing an interface
    for all subsequent(inherited) constants.
    """


class EventTypes(Constant):
    CONNECT = 'CONNECT'
    SUBSCRIBE = 'SUBSCRIBE'
    CLOSE = 'CLOSE'
    RECONNECT = 'RECONNECT'


class BittrexParameters(Constant):
    # Connection parameters
    URL = 'https://socket.bittrex.com/signalr'
    HUB = 'c2'
    # Callbacks
    MARKET_DELTA = 'uE'
    SUMMARY_DELTA = 'uS'
    SUMMARY_DELTA_LITE = 'uL'
    BALANCE_DELTA = 'uB'
    ORDER_DELTA = 'uO'


class BittrexMethods(Constant):
    SUBSCRIBE_TO_EXCHANGE_DELTAS = 'SubscribeToExchangeDeltas'
    SUBSCRIBE_TO_SUMMARY_DELTAS = 'SubscribeToSummaryDeltas'
    SUBSCRIBE_TO_SUMMARY_LITE_DELTAS = 'SubscribeToSummaryLiteDeltas'
    SUBSCRIBE_TO_BALANCE_DELTAS = 'BalanceDelta'
    SUBSCRIBE_TO_ORDER_DELTAS = 'OrderDelta'
    QUERY_SUMMARY_STATE = 'QuerySummaryState'
    QUERY_EXCHANGE_STATE = 'QueryExchangeState'
    GET_AUTH_CONTENT = 'GetAuthContext'
    AUTHENTICATE = 'Authenticate'


class ErrorMessages(Constant):
    INVALID_TICKER_INPUT = 'Tickers must be submitted as a list.'


class OtherConstants(Constant):
    CF_SESSION_TYPE = '<class \'cfscrape.CloudflareScraper\'>'
