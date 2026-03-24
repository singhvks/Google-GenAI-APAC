import pytest
from unittest.mock import MagicMock
from google.adk.tools.tool_context import ToolContext
from agent import add_prompt_to_state, root_agent, tour_guide_workflow

def test_add_prompt_to_state():
    # Setup
    mock_tool_context = MagicMock(spec=ToolContext)
    mock_tool_context.state = {}
    prompt = "Tell me about the best food in Tokyo"

    # Execute
    result = add_prompt_to_state(mock_tool_context, prompt)

    # Verify
    assert result == {"status": "success"}
    assert mock_tool_context.state["PROMPT"] == prompt

def test_agent_structure():
    # Verify the root agent's name and model
    assert root_agent.name == "greeter"
    assert root_agent.model is not None
    
    # Verify sub-agents
    assert len(root_agent.sub_agents) == 1
    assert root_agent.sub_agents[0] == tour_guide_workflow
    
    # Verify tools
    tool_names = [tool.name for tool in root_agent.tools]
    assert "add_prompt_to_state" in tool_names

def test_workflow_structure():
    # Verify the workflow name and sub-agents
    assert tour_guide_workflow.name == "food_guide_workflow"
    assert len(tour_guide_workflow.sub_agents) == 2
    
    sub_agent_names = [agent.name for agent in tour_guide_workflow.sub_agents]
    assert "comprehensive_researcher" in sub_agent_names
    assert "response_formatter" in sub_agent_names
