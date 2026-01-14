from watchdog.events import FileSystemEventHandler


class LegacyFileHandler(FileSystemEventHandler):
    def __init__(self, bus, loop):
        self.bus = bus
        self.loop = loop

    def on_created(self, event):
        if not event.is_directory:
            print(f"📂 Nuevo archivo detectado: {event.src_path}")
            with open(event.src_path, "r") as f:
                content = f.read()

            # Disparamos el evento al Bus de forma asíncrona
            self.loop.call_soon_threadsafe(
                lambda: self.loop.create_task(
                    self.bus.publish(
                        "FILE_UPLOADED",
                        {
                            "filename": event.src_path,
                            "content": content,
                            "lang": "python",
                        },
                    )
                )
            )
