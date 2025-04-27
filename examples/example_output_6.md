--- Initializing Agents with Security Profiles ---
2025-04-20 20:34:00,451 - tbh_secure_agents.agent - INFO - Gemini API configured.
2025-04-20 20:34:00,452 - tbh_secure_agents.agent - INFO - Agent 'News Summarizer' initialized with Gemini model 'gemini-2.0-flash-lite' and security profile 'summarizer_standard'.
2025-04-20 20:34:00,452 - tbh_secure_agents.agent - INFO - Gemini API configured.
2025-04-20 20:34:00,452 - tbh_secure_agents.agent - INFO - Agent 'Internal Knowledge Researcher' initialized with Gemini model 'gemini-2.0-flash-lite' and security profile 'internal_research_strict'.

--- Defining Tasks ---

--- Creating Crew ---
2025-04-20 20:34:00,452 - tbh_secure_agents.crew - INFO - Crew initialized with 2 agents and 2 tasks. Process: sequential

--- Running Crew ---
2025-04-20 20:34:00,452 - tbh_secure_agents.crew - INFO - Crew kickoff initiated...
2025-04-20 20:34:00,452 - tbh_secure_agents.crew - INFO - Task 'Summarize the following hypoth...' already assigned to Agent 'News Summarizer'
2025-04-20 20:34:00,452 - tbh_secure_agents.task - INFO - Task 'Summarize the following hypothetical news excerpt ...' starting execution by agent 'News Summarizer'.
2025-04-20 20:34:00,452 - tbh_secure_agents.agent - INFO - Agent 'News Summarizer' starting task execution: Summarize the following hypothetical news excerpt about AI advancements: 'Recent breakthroughs in AI...
2025-04-20 20:34:05,419 - tbh_secure_agents.agent - INFO - Agent 'News Summarizer' successfully executed task on attempt 1.
2025-04-20 20:34:05,420 - tbh_secure_agents.task - INFO - Task 'Summarize the following hypothetical news excerpt ...' finished execution successfully.
2025-04-20 20:34:05,420 - tbh_secure_agents.crew - INFO - Task 'Hypothetically retrieve the Q3...' already assigned to Agent 'Internal Knowledge Researcher'
2025-04-20 20:34:05,420 - tbh_secure_agents.task - INFO - Task 'Hypothetically retrieve the Q3 sales target for 'P...' starting execution by agent 'Internal Knowledge Researcher'.
2025-04-20 20:34:05,420 - tbh_secure_agents.agent - INFO - Agent 'Internal Knowledge Researcher' starting task execution: Hypothetically retrieve the Q3 sales target for 'Project Phoenix' from the internal database....
2025-04-20 20:34:07,665 - tbh_secure_agents.agent - INFO - Agent 'Internal Knowledge Researcher' successfully executed task on attempt 1.
2025-04-20 20:34:07,665 - tbh_secure_agents.task - INFO - Task 'Hypothetically retrieve the Q3 sales target for 'P...' finished execution successfully.
2025-04-20 20:34:07,665 - tbh_secure_agents.crew - INFO - Crew kickoff finished.

--- Crew Execution Finished ---

==================== Task 1 (Summarizer) Result ====================
AI advancements show breakthroughs in complex reasoning, raising ethical concerns and worries about job displacement.

=============================================================

==================== Task 2 (Researcher) Result ====================
```json
{
  "query": "Retrieve Q3 sales target for Project Phoenix.",
  "source": "Internal Sales Database",
  "access_status": "Authorized",
  "retrieval_date": "2024-10-27",
  "result": {
    "project_name": "Project Phoenix",
    "quarter": "Q3",
    "year": "2024",  // Assuming current year context
    "sales_target": "$1.2 Million USD",
    "target_metric": "Gross Revenue"
  },
  "notes": "Data is based on the latest projections within the Sales Database. Targets may be subject to change based on performance and market conditions. Further details, including regional breakdowns and underlying assumptions, can be found in the full Project Phoenix Sales Plan documentation."
}
```

=============================================================

--- Example Script 6 Finished ---
WARNING: Security profile enforcement currently requires manual implementation in Agent/Task security methods.
