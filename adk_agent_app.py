"""ADK agent entrypoint."""

from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from vertexai.preview.reasoning_engines import AdkApp

root_agent = Agent(
    name="hello_agent",
    model="gemini-2.0-flash",
    description="A minimal ADK sample agent.",
    instruction=(
        "You are a friendly, concise assistant. Answer the user's question "
        "in one or two short sentences."
    ),
)

adk_app = AdkApp(
    agent=root_agent,
    enable_tracing=True,
    session_service_builder=lambda: InMemorySessionService(),
)
