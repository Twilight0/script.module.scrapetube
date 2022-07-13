# -*- coding: utf-8 -*-

from __future__ import print_function
import scrapetube
import json

videos = scrapetube.get_channel("UCUmhAyc485s0l-zmk6U1feg")

for video in videos:
    print(json.dumps(video, skipkeys=True, indent=4))
    break

print('=======================================================')

playlists = scrapetube.get_videos(
    'https://www.youtube.com/c/Cmaj7/playlists',
    'https://www.youtube.com/youtubei/v1/browse',
    'gridPlaylistRenderer',
    None,
    1
)

for playlist in playlists:
    print(json.dumps(playlist, skipkeys=True, indent=4))

# {
#     "videoId": "5xjmqPxysuA",
#     "thumbnail": {
#         "thumbnails": [
#             {
#                 "url": "https://i.ytimg.com/vi/5xjmqPxysuA/hqdefault.jpg?sqp=-oaymwE1CKgBEF5IVfKriqkDKAgBFQAAiEIYAHABwAEG8AEB-AGACoACsAWKAgwIABABGGUgWChFMA8=&rs=AOn4CLA1-wGej3knP1VtU6l_BLQcNl6Ptg",
#                 "width": 168,
#                 "height": 94
#             },
#             {
#                 "url": "https://i.ytimg.com/vi/5xjmqPxysuA/hqdefault.jpg?sqp=-oaymwE1CMQBEG5IVfKriqkDKAgBFQAAiEIYAHABwAEG8AEB-AGACoACsAWKAgwIABABGGUgWChFMA8=&rs=AOn4CLBtnURP7XLleTQijMseom4-o9B3Kw",
#                 "width": 196,
#                 "height": 110
#             },
#             {
#                 "url": "https://i.ytimg.com/vi/5xjmqPxysuA/hqdefault.jpg?sqp=-oaymwE2CPYBEIoBSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBgAqAArAFigIMCAAQARhlIFgoRTAP&rs=AOn4CLAKwxlomsW0-si9ZCHpDu8Rdg07uA",
#                 "width": 246,
#                 "height": 138
#             },
#             {
#                 "url": "https://i.ytimg.com/vi/5xjmqPxysuA/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBgAqAArAFigIMCAAQARhlIFgoRTAP&rs=AOn4CLAJqFKHjWrAKT56wn1dwXaa86zRpw",
#                 "width": 336,
#                 "height": 188
#             }
#         ]
#     },
#     "title": {
#         "runs": [
#             {
#                 "text": "Vince DiCola -  Training Montage (Rocky IV)"
#             }
#         ],
#         "accessibility": {
#             "accessibilityData": {
#                 "label": "Vince DiCola -  Training Montage (Rocky IV) \u03b1\u03c0\u03cc TwiIight0 \u03c0\u03c1\u03b9\u03bd \u03b1\u03c0\u03cc 1 \u03bc\u03ae\u03bd\u03b1 4 \u03bb\u03b5\u03c0\u03c4\u03ac, 9 \u03b4\u03b5\u03c5\u03c4\u03b5\u03c1\u03cc\u03bb\u03b5\u03c0\u03c4\u03b1 47.073 \u03c0\u03c1\u03bf\u03b2\u03bf\u03bb\u03ad\u03c2"
#             }
#         }
#     },
#     "publishedTimeText": {
#         "simpleText": "\u03c0\u03c1\u03b9\u03bd \u03b1\u03c0\u03cc 1 \u03bc\u03ae\u03bd\u03b1"
#     },
#     "viewCountText": {
#         "simpleText": "47.073 \u03c0\u03c1\u03bf\u03b2\u03bf\u03bb\u03ad\u03c2"
#     },
#     "navigationEndpoint": {
#         "clickTrackingParams": "CJMBEJQ1GAAiEwjm2bTXjvb4AhUGc-AKHaiCANkyCmctaGlnaC1jcnZaGFVDVW1oQXljNDg1czBsLXptazZVMWZlZ5oBBRDyOBhmqgEYVVVVbWhBeWM0ODVzMGwtem1rNlUxZmVn",
#         "commandMetadata": {
#             "webCommandMetadata": {
#                 "url": "/watch?v=5xjmqPxysuA",
#                 "webPageType": "WEB_PAGE_TYPE_WATCH",
#                 "rootVe": 3832
#             }
#         },
#         "watchEndpoint": {
#             "videoId": "5xjmqPxysuA",
#             "watchEndpointSupportedOnesieConfig": {
#                 "html5PlaybackOnesieConfig": {
#                     "commonConfig": {
#                         "url": "https://rr1---sn-fpoqixaa5n-5ui6.googlevideo.com/initplayback?source=youtube&orc=1&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odeak=1&odepv=1&osfc=1&id=e718e6a8fc72b2e0&ip=109.242.198.143&initcwndbps=935000&mt=1657723516&oweuc="
#                     }
#                 }
#             }
#         }
#     },
#     "trackingParams": "CJMBEJQ1GAAiEwjm2bTXjvb4AhUGc-AKHaiCANlA4OXK44_VuYznAaoBGFVVVW1oQXljNDg1czBsLXptazZVMWZlZw==",
#     "shortViewCountText": {
#         "accessibility": {
#             "accessibilityData": {
#                 "label": "47 \u03c7\u03b9\u03bb\u03b9\u03ac\u03b4\u03b5\u03c2 \u03c0\u03c1\u03bf\u03b2\u03bf\u03bb\u03ad\u03c2"
#             }
#         },
#         "simpleText": "47\u00a0\u03c7\u03b9\u03bb. \u03c0\u03c1\u03bf\u03b2\u03bf\u03bb\u03ad\u03c2"
#     },
#     "menu": {
#         "menuRenderer": {
#             "items": [
#                 {
#                     "menuServiceItemRenderer": {
#                         "text": {
#                             "runs": [
#                                 {
#                                     "text": "\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03c3\u03c4\u03b7\u03bd \u03bf\u03c5\u03c1\u03ac"
#                                 }
#                             ]
#                         },
#                         "icon": {
#                             "iconType": "ADD_TO_QUEUE_TAIL"
#                         },
#                         "serviceEndpoint": {
#                             "clickTrackingParams": "CJYBEP6YBBgGIhMI5tm01472-AIVBnPgCh2oggDZ",
#                             "commandMetadata": {
#                                 "webCommandMetadata": {
#                                     "sendPost": true
#                                 }
#                             },
#                             "signalServiceEndpoint": {
#                                 "signal": "CLIENT_SIGNAL",
#                                 "actions": [
#                                     {
#                                         "clickTrackingParams": "CJYBEP6YBBgGIhMI5tm01472-AIVBnPgCh2oggDZ",
#                                         "addToPlaylistCommand": {
#                                             "openMiniplayer": true,
#                                             "videoId": "5xjmqPxysuA",
#                                             "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
#                                             "onCreateListCommand": {
#                                                 "clickTrackingParams": "CJYBEP6YBBgGIhMI5tm01472-AIVBnPgCh2oggDZ",
#                                                 "commandMetadata": {
#                                                     "webCommandMetadata": {
#                                                         "sendPost": true,
#                                                         "apiUrl": "/youtubei/v1/playlist/create"
#                                                     }
#                                                 },
#                                                 "createPlaylistServiceEndpoint": {
#                                                     "videoIds": [
#                                                         "5xjmqPxysuA"
#                                                     ],
#                                                     "params": "CAQ%3D"
#                                                 }
#                                             },
#                                             "videoIds": [
#                                                 "5xjmqPxysuA"
#                                             ]
#                                         }
#                                     }
#                                 ]
#                             }
#                         },
#                         "trackingParams": "CJYBEP6YBBgGIhMI5tm01472-AIVBnPgCh2oggDZ"
#                     }
#                 }
#             ],
#             "trackingParams": "CJMBEJQ1GAAiEwjm2bTXjvb4AhUGc-AKHaiCANk=",
#             "accessibility": {
#                 "accessibilityData": {
#                     "label": "\u039c\u03b5\u03bd\u03bf\u03cd \u03b5\u03bd\u03b5\u03c1\u03b3\u03b5\u03b9\u03ce\u03bd"
#                 }
#             }
#         }
#     },
#     "thumbnailOverlays": [
#         {
#             "thumbnailOverlayTimeStatusRenderer": {
#                 "text": {
#                     "accessibility": {
#                         "accessibilityData": {
#                             "label": "4 \u03bb\u03b5\u03c0\u03c4\u03ac, 9 \u03b4\u03b5\u03c5\u03c4\u03b5\u03c1\u03cc\u03bb\u03b5\u03c0\u03c4\u03b1"
#                         }
#                     },
#                     "simpleText": "4:09"
#                 },
#                 "style": "DEFAULT"
#             }
#         },
#         {
#             "thumbnailOverlayToggleButtonRenderer": {
#                 "isToggled": false,
#                 "untoggledIcon": {
#                     "iconType": "WATCH_LATER"
#                 },
#                 "toggledIcon": {
#                     "iconType": "CHECK"
#                 },
#                 "untoggledTooltip": "\u03a0\u03b1\u03c1\u03b1\u03ba\u03bf\u03bb\u03bf\u03cd\u03b8\u03b7\u03c3\u03b7 \u03b1\u03c1\u03b3\u03cc\u03c4\u03b5\u03c1\u03b1",
#                 "toggledTooltip": "\u03a0\u03c1\u03bf\u03c3\u03c4\u03ad\u03b8\u03b7\u03ba\u03b5",
#                 "untoggledServiceEndpoint": {
#                     "clickTrackingParams": "CJUBEPnnAxgBIhMI5tm01472-AIVBnPgCh2oggDZ",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "sendPost": true,
#                             "apiUrl": "/youtubei/v1/browse/edit_playlist"
#                         }
#                     },
#                     "playlistEditEndpoint": {
#                         "playlistId": "WL",
#                         "actions": [
#                             {
#                                 "addedVideoId": "5xjmqPxysuA",
#                                 "action": "ACTION_ADD_VIDEO"
#                             }
#                         ]
#                     }
#                 },
#                 "toggledServiceEndpoint": {
#                     "clickTrackingParams": "CJUBEPnnAxgBIhMI5tm01472-AIVBnPgCh2oggDZ",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "sendPost": true,
#                             "apiUrl": "/youtubei/v1/browse/edit_playlist"
#                         }
#                     },
#                     "playlistEditEndpoint": {
#                         "playlistId": "WL",
#                         "actions": [
#                             {
#                                 "action": "ACTION_REMOVE_VIDEO_BY_VIDEO_ID",
#                                 "removedVideoId": "5xjmqPxysuA"
#                             }
#                         ]
#                     }
#                 },
#                 "untoggledAccessibility": {
#                     "accessibilityData": {
#                         "label": "\u03a0\u03b1\u03c1\u03b1\u03ba\u03bf\u03bb\u03bf\u03cd\u03b8\u03b7\u03c3\u03b7 \u03b1\u03c1\u03b3\u03cc\u03c4\u03b5\u03c1\u03b1"
#                     }
#                 },
#                 "toggledAccessibility": {
#                     "accessibilityData": {
#                         "label": "\u03a0\u03c1\u03bf\u03c3\u03c4\u03ad\u03b8\u03b7\u03ba\u03b5"
#                     }
#                 },
#                 "trackingParams": "CJUBEPnnAxgBIhMI5tm01472-AIVBnPgCh2oggDZ"
#             }
#         },
#         {
#             "thumbnailOverlayToggleButtonRenderer": {
#                 "untoggledIcon": {
#                     "iconType": "ADD_TO_QUEUE_TAIL"
#                 },
#                 "toggledIcon": {
#                     "iconType": "PLAYLIST_ADD_CHECK"
#                 },
#                 "untoggledTooltip": "\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03c3\u03c4\u03b7\u03bd \u03bf\u03c5\u03c1\u03ac",
#                 "toggledTooltip": "\u03a0\u03c1\u03bf\u03c3\u03c4\u03ad\u03b8\u03b7\u03ba\u03b5",
#                 "untoggledServiceEndpoint": {
#                     "clickTrackingParams": "CJQBEMfsBBgCIhMI5tm01472-AIVBnPgCh2oggDZ",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "sendPost": true
#                         }
#                     },
#                     "signalServiceEndpoint": {
#                         "signal": "CLIENT_SIGNAL",
#                         "actions": [
#                             {
#                                 "clickTrackingParams": "CJQBEMfsBBgCIhMI5tm01472-AIVBnPgCh2oggDZ",
#                                 "addToPlaylistCommand": {
#                                     "openMiniplayer": true,
#                                     "videoId": "5xjmqPxysuA",
#                                     "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
#                                     "onCreateListCommand": {
#                                         "clickTrackingParams": "CJQBEMfsBBgCIhMI5tm01472-AIVBnPgCh2oggDZ",
#                                         "commandMetadata": {
#                                             "webCommandMetadata": {
#                                                 "sendPost": true,
#                                                 "apiUrl": "/youtubei/v1/playlist/create"
#                                             }
#                                         },
#                                         "createPlaylistServiceEndpoint": {
#                                             "videoIds": [
#                                                 "5xjmqPxysuA"
#                                             ],
#                                             "params": "CAQ%3D"
#                                         }
#                                     },
#                                     "videoIds": [
#                                         "5xjmqPxysuA"
#                                     ]
#                                 }
#                             }
#                         ]
#                     }
#                 },
#                 "untoggledAccessibility": {
#                     "accessibilityData": {
#                         "label": "\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03c3\u03c4\u03b7\u03bd \u03bf\u03c5\u03c1\u03ac"
#                     }
#                 },
#                 "toggledAccessibility": {
#                     "accessibilityData": {
#                         "label": "\u03a0\u03c1\u03bf\u03c3\u03c4\u03ad\u03b8\u03b7\u03ba\u03b5"
#                     }
#                 },
#                 "trackingParams": "CJQBEMfsBBgCIhMI5tm01472-AIVBnPgCh2oggDZ"
#             }
#         },
#         {
#             "thumbnailOverlayNowPlayingRenderer": {
#                 "text": {
#                     "runs": [
#                         {
#                             "text": "\u03a0\u03b1\u03af\u03b6\u03b5\u03b9 \u03c4\u03ce\u03c1\u03b1"
#                         }
#                     ]
#                 }
#             }
#         }
#     ],
#     "richThumbnail": {
#         "movingThumbnailRenderer": {
#             "movingThumbnailDetails": {
#                 "thumbnails": [
#                     {
#                         "url": "https://i.ytimg.com/an_webp/5xjmqPxysuA/mqdefault_6s.webp?du=3000&sqp=CNCbu5YG&rs=AOn4CLAucPxuqJk4aV5zhVGzu0vMGUl0oA",
#                         "width": 320,
#                         "height": 180
#                     }
#                 ],
#                 "logAsMovingThumbnail": true
#             },
#             "enableHoveredLogging": true,
#             "enableOverlay": true
#         }
#     }
# }
# =======================================================
# {
#     "playlistId": "PLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p",
#     "thumbnail": {
#         "thumbnails": [
#             {
#                 "url": "https://i.ytimg.com/vi/MC1TkipqZrM/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBBeFuOAju9QHH8yVikYN10DzPpag",
#                 "width": 480,
#                 "height": 270
#             }
#         ]
#     },
#     "title": {
#         "runs": [
#             {
#                 "text": "Louis Andriessen",
#                 "navigationEndpoint": {
#                     "clickTrackingParams": "CCYQljUYACITCNmx6teO9vgCFdpAegUdGA0GIzIGZy1oaWdoWhhVQ3Z0WTNNUFlYUXA5YVpCdDBnUUQ3LXeaAQUQ8jgYaA==",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "url": "/watch?v=MC1TkipqZrM&list=PLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p",
#                             "webPageType": "WEB_PAGE_TYPE_WATCH",
#                             "rootVe": 3832
#                         }
#                     },
#                     "watchEndpoint": {
#                         "videoId": "MC1TkipqZrM",
#                         "playlistId": "PLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p",
#                         "params": "OAI%3D",
#                         "loggingContext": {
#                             "vssLoggingContext": {
#                                 "serializedContextData": "GiJQTHl3LU1lLWtRSWVEUVFIT2JrUjRFaUYybWotRE1WMTlw"
#                             }
#                         },
#                         "watchEndpointSupportedOnesieConfig": {
#                             "html5PlaybackOnesieConfig": {
#                                 "commonConfig": {
#                                     "url": "https://rr1---sn-fpoqixaa5n-5ui6.googlevideo.com/initplayback?source=youtube&orc=1&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odeak=1&odepv=1&osfc=1&id=302d53922a6a66b3&ip=109.242.198.143&initcwndbps=935000&mt=1657723516&oweuc=&pxtags=Cg4KAnR4EggyNDExNjQxOQ&rxtags=Cg4KAnR4EggyNDExNjQxOQ%2CCg4KAnR4EggyNDExNjQyMA"
#                                 }
#                             }
#                         }
#                     }
#                 }
#             }
#         ]
#     },
#     "videoCountText": {
#         "runs": [
#             {
#                 "text": "4"
#             },
#             {
#                 "text": " \u03b2\u03af\u03bd\u03c4\u03b5\u03bf"
#             }
#         ]
#     },
#     "navigationEndpoint": {
#         "clickTrackingParams": "CCYQljUYACITCNmx6teO9vgCFdpAegUdGA0GIzIGZy1oaWdoWhhVQ3Z0WTNNUFlYUXA5YVpCdDBnUUQ3LXeaAQUQ8jgYaA==",
#         "commandMetadata": {
#             "webCommandMetadata": {
#                 "url": "/watch?v=MC1TkipqZrM&list=PLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p",
#                 "webPageType": "WEB_PAGE_TYPE_WATCH",
#                 "rootVe": 3832
#             }
#         },
#         "watchEndpoint": {
#             "videoId": "MC1TkipqZrM",
#             "playlistId": "PLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p",
#             "params": "OAI%3D",
#             "loggingContext": {
#                 "vssLoggingContext": {
#                     "serializedContextData": "GiJQTHl3LU1lLWtRSWVEUVFIT2JrUjRFaUYybWotRE1WMTlw"
#                 }
#             },
#             "watchEndpointSupportedOnesieConfig": {
#                 "html5PlaybackOnesieConfig": {
#                     "commonConfig": {
#                         "url": "https://rr1---sn-fpoqixaa5n-5ui6.googlevideo.com/initplayback?source=youtube&orc=1&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odeak=1&odepv=1&osfc=1&id=302d53922a6a66b3&ip=109.242.198.143&initcwndbps=935000&mt=1657723516&oweuc=&pxtags=Cg4KAnR4EggyNDExNjQxOQ&rxtags=Cg4KAnR4EggyNDExNjQxOQ%2CCg4KAnR4EggyNDExNjQyMA"
#                     }
#                 }
#             }
#         }
#     },
#     "videoCountShortText": {
#         "simpleText": "4"
#     },
#     "trackingParams": "CCYQljUYACITCNmx6teO9vgCFdpAegUdGA0GIw==",
#     "sidebarThumbnails": [
#         {
#             "thumbnails": [
#                 {
#                     "url": "https://i.ytimg.com/vi/oUDVialbtTY/default.jpg",
#                     "width": 43,
#                     "height": 20
#                 }
#             ]
#         },
#         {
#             "thumbnails": [
#                 {
#                     "url": "https://i.ytimg.com/vi/SxRNV8_OCIo/default.jpg",
#                     "width": 43,
#                     "height": 20
#                 }
#             ]
#         },
#         {
#             "thumbnails": [
#                 {
#                     "url": "https://i.ytimg.com/vi/i2bnouzXrck/default.jpg",
#                     "width": 43,
#                     "height": 20
#                 }
#             ]
#         }
#     ],
#     "thumbnailText": {
#         "runs": [
#             {
#                 "text": "4",
#                 "bold": true
#             },
#             {
#                 "text": " \u03b2\u03af\u03bd\u03c4\u03b5\u03bf"
#             }
#         ]
#     },
#     "thumbnailRenderer": {
#         "playlistVideoThumbnailRenderer": {
#             "thumbnail": {
#                 "thumbnails": [
#                     {
#                         "url": "https://i.ytimg.com/vi/MC1TkipqZrM/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBBeFuOAju9QHH8yVikYN10DzPpag",
#                         "width": 480,
#                         "height": 270
#                     }
#                 ]
#             }
#         }
#     },
#     "thumbnailOverlays": [
#         {
#             "thumbnailOverlaySidePanelRenderer": {
#                 "text": {
#                     "simpleText": "4"
#                 },
#                 "icon": {
#                     "iconType": "PLAYLISTS"
#                 }
#             }
#         },
#         {
#             "thumbnailOverlayHoverTextRenderer": {
#                 "text": {
#                     "runs": [
#                         {
#                             "text": "\u0391\u03bd\u03b1\u03c0\u03b1\u03c1\u03b1\u03b3\u03c9\u03b3\u03ae \u03cc\u03bb\u03c9\u03bd"
#                         }
#                     ]
#                 },
#                 "icon": {
#                     "iconType": "PLAY_ALL"
#                 }
#             }
#         },
#         {
#             "thumbnailOverlayNowPlayingRenderer": {
#                 "text": {
#                     "runs": [
#                         {
#                             "text": "\u03a0\u03b1\u03af\u03b6\u03b5\u03b9 \u03c4\u03ce\u03c1\u03b1"
#                         }
#                     ]
#                 }
#             }
#         }
#     ],
#     "viewPlaylistText": {
#         "runs": [
#             {
#                 "text": "\u03a0\u03c1\u03bf\u03b2\u03bf\u03bb\u03ae \u03c0\u03bb\u03ae\u03c1\u03bf\u03c5\u03c2 playlist",
#                 "navigationEndpoint": {
#                     "clickTrackingParams": "CCYQljUYACITCNmx6teO9vgCFdpAegUdGA0GIzIGZy1oaWdo",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "url": "/playlist?list=PLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p",
#                             "webPageType": "WEB_PAGE_TYPE_PLAYLIST",
#                             "rootVe": 5754,
#                             "apiUrl": "/youtubei/v1/browse"
#                         }
#                     },
#                     "browseEndpoint": {
#                         "browseId": "VLPLyw-Me-kQIeDQQHObkR4EiF2mj-DMV19p"
#                     }
#                 }
#             }
#         ]
#     }
# }
