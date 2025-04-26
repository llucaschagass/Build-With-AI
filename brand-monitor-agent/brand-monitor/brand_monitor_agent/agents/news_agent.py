"""News Agent module.

Returns:
    LlmAgent: Agent that analyzes recent news articles for the target company.
"""

from google.adk.agents import LlmAgent
from ..tools import get_posts


def create_news_agent() -> LlmAgent:
    """Creates an agent to analyze recent news articles for the target company.

    Args:
        None

    Returns:
        LlmAgent: Configured News analysis agent.
    """
    return LlmAgent(
        name="NewsFetcher",
        model="gemini-2.0-flash",
        description="Analyze recent news articles for the target company.",
        instruction=(
            "Use the get_posts tool with source='news' and company=state['company'] to fetch the 5 latest articles. "
            "Then write a concise report highlighting the main themes and sentiment in the news coverage."
        ),
        tools=[get_posts],
        output_key="news_report",
    )


news_agent = create_news_agent()
