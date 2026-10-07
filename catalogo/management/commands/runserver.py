from django.contrib.staticfiles.management.commands.runserver import (
    Command as StaticRunserverCommand,
)


class Command(StaticRunserverCommand):
    """Muestra de forma visible la URL principal al iniciar el proyecto."""

    default_addr = "127.0.0.1"
    default_port = "8000"

    def inner_run(self, *args, **options):
        host = self.addr
        if host in {"0", "0.0.0.0", "::"}:
            host = "127.0.0.1"

        self.stdout.write(
            self.style.SUCCESS(f"Sitio principal: http://{host}:{self.port}/")
        )
        super().inner_run(*args, **options)
