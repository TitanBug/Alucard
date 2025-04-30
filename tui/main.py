from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static
from audit.scanner import scan_pods
from rich.text import Text
from rich.console import RenderableType
import os

try:
    from ai.assistant import explain_misconfig
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

class KubeAuditApp(App):
    CSS_PATH = "styles.css"

    def compose(self) -> ComposeResult:
        yield Header()
        self.output_box = Static()
        self.table = DataTable()
        yield self.table
        yield self.output_box
        yield Footer()

    def on_mount(self):
        pods = scan_pods()
        self.table.add_columns("Namespace", "Pod", "Privileged?", "RunAsRoot?", "AI Insight")

        for pod in pods:
            privileged = any(
                c.security_context and c.security_context.privileged
                for c in pod.spec.containers
            )
            run_as_root = any(
                c.security_context and c.security_context.run_as_user == 0
                for c in pod.spec.containers
            )

            issue = []
            if privileged:
                issue.append("Privileged container")
            if run_as_root:
                issue.append("Runs as root")

            ai_summary = ""
            if AI_AVAILABLE and issue and os.getenv("OPENAI_API_KEY"):
                try:
                    desc = ", ".join(issue)
                    ai_summary = explain_misconfig(desc, f"Pod: {pod.metadata.name}")
                except Exception as e:
                    ai_summary = f"[AI error: {e}]"

            self.table.add_row(
                pod.metadata.namespace,
                pod.metadata.name,
                "[bold red]Yes[/bold red]" if privileged else "[green]No[/green]",
                "[bold red]Yes[/bold red]" if run_as_root else "[green]No[/green]",
                ai_summary or "[dim]N/A[/dim]"
            )

        summary = f"\nScanned {len(pods)} pod(s). Potential issues are highlighted in red.\n"
        self.output_box.update(Text(summary, style="bold yellow"))