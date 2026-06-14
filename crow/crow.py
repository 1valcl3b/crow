from threading import Thread

from scheduler import iniciar_scheduler

from app.views import app


scheduler_thread = Thread(
    target=iniciar_scheduler,
    daemon=True
)

scheduler_thread.start()


app.run(
    host="0.0.0.0",
    port=5000
)