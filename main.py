from tui.main import KubeAuditApp

if __name__ == "__main__":
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text

    console = Console()
    banner_text = Text("ALUCARD", style="bold magenta", justify="center")
    banner_panel = Panel(
        banner_text,
        title="KubeAudit TUI",
        subtitle="Cloud Misconfiguration Scanner",
        border_style="bright_red"
    )
    console.print(banner_panel)

    credit = Text("Created by Brian Bange | For Ethical Use Only\nUnauthorized or malicious use is strictly prohibited.", style="bold white on black", justify="center")
    console.print(Panel(credit, border_style="red", title="Notice"))

    KubeAuditApp().run()
