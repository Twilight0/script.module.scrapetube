# -*- coding: utf-8 -*-

'''
    Scrapetube library
    Author dermasmid, Twilight0

    SPDX-License-Identifier: MIT Licence
    See LICENSE for more information.
'''

from __future__ import absolute_import

from scrapetube import *


yt_prefix = 'https://www.youtube.com/watch?v={0}'


def duration_converter(duration):

    """
    Converts duration in string (minutes:seconds) to integer in seconds
    """

    result = duration.split(':')

    result = int(result[0]) * 60 + int(result[1])

    return result


def list_channel_videos(
    channel_id=None, channel_url=None, limit=None, sleep=1, sort_by="newest",
    add_prefix=True, thumb_quality=3
    ):

    items_list = list(get_channel(channel_id, channel_url, limit, sleep, sort_by))

    items_list = [
        dict(
            title=i['title']['runs'][0]['text'], url=yt_prefix.format(i['videoId']) if add_prefix else i['videoId'],
            image=i['thumbnail'][thumb_quality]['url'],
            duration=duration_converter(i['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['text']['simpleText'])
            ) for i in items_list
        ]
    
    return items_list
    

def list_playlists(
    url, api='https://www.youtube.com/youtubei/v1/browse', renderer='gridPlaylistRenderer', limit=None, sleep=1
    ):

    items_list = list(get_videos(url, api, renderer, limit, sleep))

    items_list = [
        dict(
            title=['title']['runs'][0]['text'], url=['playlistId'],
            image=i['thumbnail'][0]['url']
            ) for i in items_list
    ]


def list_playlist_videos(url, limit=None, sleep=1, sort_by="newest",
    add_prefix=True, thumb_quality=3):

    items_list = list(get_playlist(url, limit, sleep))

    items_list = [
        dict(
            title=i['title']['runs'][0]['text'], url=yt_prefix.format(i['videoId']) if add_prefix else i['videoId'],
            image=i['thumbnail'][thumb_quality]['url'],
            duration=duration_converter(i['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['text']['simpleText'])
            ) for i in items_list
        ]

    return items_list


def list_search(
    query, limit=None, sleep=1, sort_by="relevance", results_type="video", add_prefix=True, thumb_quality=3
    ):

    if results_type == 'video':

        items_list = [
        dict(
            title=i['title']['runs'][0]['text'], url=yt_prefix.format(i['videoId']) if add_prefix else i['videoId'],
            image=i['thumbnail'][thumb_quality]['url'],
            duration=duration_converter(i['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['text']['simpleText'])
            ) for i in items_list
        ]

    elif results_type == 'playlist':

        items_list = [
        dict(
            title=['title']['runs'][0]['text'], url=['playlistId'],
            image=i['thumbnail'][0]['url']
            ) for i in items_list
    ]

    else:

        return
