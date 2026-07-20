"""Application entrypoint."""


class SampleAgent:
    """A minimal agent."""

    def query(self, **kwargs):
        message = kwargs.get("message", "")
        return {"reply": f"You said: {message}"}

    def stream_query(self, **kwargs):
        message = kwargs.get("message", "")
        for token in f"You said: {message}".split():
            yield {"chunk": token}


agent = SampleAgent()
