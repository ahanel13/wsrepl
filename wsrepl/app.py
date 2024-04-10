import asyncio
import inspect
import logging

from textual import events, on
from textual.app import App, ComposeResult
from textual.logging import TextualHandler
from textual.widgets import Input

from wsrepl import WSReplConfig
from wsrepl.log import log, register_log_handler
from wsrepl.widgets import History, Parent
from wsrepl.MessageHandler import MessageHandler


logging.basicConfig(
    level="DEBUG",
    # https://textual.textualize.io/guide/devtools/
    handlers=[TextualHandler()],
)


class WSRepl(App):
    CSS_PATH = "app.css"

    def __init__(self, config: WSReplConfig) -> None:
        super().__init__()

        # Small UI
        self.small = config.small

        # Verbosity for logging level
        self.verbosity = config.verbosity

        # Message handler, spawns a thread to handle the websocket connection
        self.message_handler = MessageHandler(app=self, conf=config)

        # These are set in compose()
        self.history = None
        self.input_widget = None

    @on(History.Ready)
    async def _history_mount(self, event: events.Mount) -> None:
        """Called when the history widget is mounted and we're ready to connect to the websocket."""
        # Set up logging, allows adding messages to UI by logging them
        register_log_handler(self, self.verbosity)
        # Pass asyncio event loop to the message handler so that it can schedule tasks on main thread
        await self.message_handler.init(asyncio.get_running_loop())

    def compose(self) -> ComposeResult:
        """Compose the Textual app layout."""
        self.history = History(self.small)
        self.input_widget = Input(placeholder="Enter websocket message", disabled=True)

        classes = ["app"]
        if self.small:
            classes.append("small")

        yield Parent(classes=classes)

    async def on_input_submitted(self, event) -> None:
        await self.message_handler.send_str(event.value)
        self.input_widget.value = ''

    def disable_input(self) -> None:
        """Disable the input widget."""
        self.input_widget.disabled = True

    def enable_input(self) -> None:
        """Enable the input widget."""
        self.input_widget.disabled = False
        self.input_widget.focus()

