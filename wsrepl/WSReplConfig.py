from typing import List, Optional


class WSReplConfig:
    def __init__(
      self,
      # URL is the only required argument
      url: str,

      # UI settings
      small: bool = False,

      # Websocket settings
      cookies            : Optional[List[str]] = None,
      headers            : Optional[List[str]] = None,
      user_agent         : Optional[str] = None,
      origin             : Optional[str] = None,
      headers_file       : Optional[str] = None,
      proxy              : Optional[str] = None,
      reconnect_interval : int  = 0,
      verify_tls         : bool = True,

      hide_ping_pong     : bool = False,
      ping_interval      : int | float = 24, # 0 -> disable auto ping
      ping_0x1_interval  : int | float = 24, # 0 -> disable fake ping
      ping_0x1_payload   : Optional[str] = None,
      pong_0x1_payload   : Optional[str] = None,
      hide_0x1_ping_pong : bool = False,

      # Other
      initial_msgs_file   : Optional[str]  = None,
      plugin_path         : Optional[str]  = None,
      plugin_provided_url : Optional[bool] = None,
      verbosity           : int = 0
    ) -> None:
        if not url:
            raise ValueError("URL is required")

        if not isinstance(ping_interval, (int, float)) or ping_interval < 0:
            raise ValueError("Ping interval must be a non-negative number")

        if not isinstance(ping_0x1_interval, (int, float)) or ping_0x1_interval < 0:
            raise ValueError("Ping 0x1 interval must be a non-negative number")

        if not isinstance(verbosity, (int, float)) or verbosity < 0:
            raise ValueError("Verbosity must be a non-negative number")

        self.url                 : str                 = url
        self.small               : bool                = small
        self.user_agent          : Optional[str]       = user_agent
        self.origin              : Optional[str]       = origin
        self.cookies             : Optional[List[str]] = cookies
        self.headers             : Optional[List[str]] = headers
        self.headers_file        : Optional[str]       = headers_file
        self.ping_interval       : float               = ping_interval
        self.hide_ping_pong      : bool                = hide_ping_pong
        self.ping_0x1_interval   : float               = ping_0x1_interval
        self.ping_0x1_payload    : Optional[str]       = ping_0x1_payload
        self.pong_0x1_payload    : Optional[str]       = pong_0x1_payload
        self.hide_0x1_ping_pong  : bool                = hide_0x1_ping_pong
        self.reconnect_interval  : int                 = reconnect_interval
        self.proxy               : Optional[str]       = proxy
        self.verify_tls          : bool                = verify_tls
        self.initial_msgs_file   : Optional[str]       = initial_msgs_file
        self.plugin_path         : Optional[str]       = plugin_path
        self.plugin_provided_url : Optional[bool]      = plugin_provided_url
        self.verbosity           : int                 = verbosity
