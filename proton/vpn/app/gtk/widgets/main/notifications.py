"""
Error messenger module.
"""
from gi.repository import GLib
from proton.vpn.app.gtk import Gtk
from proton.vpn.app.gtk.widgets.main.notification_bar import NotificationBar


class Notifications:
    """It wraps all types of notifications to be shown by the app."""

    def __init__(
        self, main_window: Gtk.ApplicationWindow,
        notification_bar: NotificationBar,
    ):
        self._main_window = main_window
        self.notification_bar = notification_bar
        self.error_dialogs = []  # only for testing purposes

    def show_error_dialog(self, message: str, title: str):
        """Show an error dialog to the user."""
        GLib.idle_add(
            self._generate_and_show_dialog, title, message
        )

    def _generate_and_show_dialog(self, title: str, message: str):
        """Generates and displays a pop-up dialog to the user, blocking
        the rest of the UI."""
        error_dialog = Gtk.MessageDialog(
            transient_for=self._main_window,
            flags=Gtk.DialogFlags.DESTROY_WITH_PARENT,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=title,
        )
        self.error_dialogs.append(error_dialog)
        error_dialog.format_secondary_text(message)
        error_dialog.run()
        error_dialog.destroy()
        self.error_dialogs.remove(error_dialog)

    def show_error_message(self, message: str):
        """Shows the error message in the notification bar."""
        GLib.idle_add(
            self.notification_bar.show_error_message,
            message
        )

    def show_success_message(self, message: str):
        """Shows a success message in the notification bar."""
        GLib.idle_add(
            self.notification_bar.show_success_message,
            message
        )