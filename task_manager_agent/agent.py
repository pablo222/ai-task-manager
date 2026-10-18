from google.adk.agents import Agent
from task_manager import add_task, list_tasks, complete_task, remove_task


root_agent = Agent(name="task_manager_agent", model="gemini-3.1-flash-lite",
                   description="AI assistant for managing tasks",
                   instruction="You help users manage their tasks. "
                               "You can only add, list, complete, or remove tasks."
                               "Use the available tools to perform task management operations."
                               "Inform the user when a requested feature is not supported.",
                   tools=[add_task, list_tasks, complete_task, remove_task]
                   )

print(root_agent.name)
print(root_agent.model)
