--- Initializing Agents with Security Profiles ---
2025-04-20 20:34:26,752 - tbh_secure_agents.agent - INFO - Gemini API configured.
2025-04-20 20:34:26,753 - tbh_secure_agents.agent - INFO - Agent 'Multilingual Translator' initialized with Gemini model 'gemini-2.0-flash-lite' and security profile 'translator_general'.
2025-04-20 20:34:26,753 - tbh_secure_agents.agent - INFO - Gemini API configured.
2025-04-20 20:34:26,753 - tbh_secure_agents.agent - INFO - Agent 'PII-Aware Multilingual Translator' initialized with Gemini model 'gemini-2.0-flash-lite' and security profile 'translator_no_pii'.

--- Defining Task ---

--- Creating and Running General Translation Crew ---
2025-04-20 20:34:26,753 - tbh_secure_agents.crew - INFO - Crew initialized with 1 agents and 1 tasks. Process: sequential
2025-04-20 20:34:26,753 - tbh_secure_agents.crew - INFO - Crew kickoff initiated...
2025-04-20 20:34:26,753 - tbh_secure_agents.crew - INFO - Task 'Translate the following text t...' already assigned to Agent 'Multilingual Translator'
2025-04-20 20:34:26,753 - tbh_secure_agents.task - INFO - Task 'Translate the following text to Spanish: 'Please c...' starting execution by agent 'Multilingual Translator'.
2025-04-20 20:34:26,753 - tbh_secure_agents.agent - INFO - Agent 'Multilingual Translator' starting task execution: Translate the following text to Spanish: 'Please contact support@example.com for assistance.'...
2025-04-20 20:34:37,118 - tbh_secure_agents.agent - INFO - Agent 'Multilingual Translator' successfully executed task on attempt 1.
2025-04-20 20:34:37,119 - tbh_secure_agents.task - INFO - Task 'Translate the following text to Spanish: 'Please c...' finished execution successfully.
2025-04-20 20:34:37,119 - tbh_secure_agents.crew - INFO - Crew kickoff finished.
General Translation Crew Finished.

--- Creating and Running PII-Safe Translation Crew ---
2025-04-20 20:34:37,119 - tbh_secure_agents.crew - INFO - Crew initialized with 1 agents and 1 tasks. Process: sequential
2025-04-20 20:34:37,119 - tbh_secure_agents.crew - INFO - Crew kickoff initiated...
2025-04-20 20:34:37,119 - tbh_secure_agents.crew - INFO - Task 'Translate the following text t...' already assigned to Agent 'PII-Aware Multilingual Translator'
2025-04-20 20:34:37,119 - tbh_secure_agents.task - INFO - Task 'Translate the following text to Spanish: 'Please c...' starting execution by agent 'PII-Aware Multilingual Translator'.
2025-04-20 20:34:37,119 - tbh_secure_agents.agent - INFO - Agent 'PII-Aware Multilingual Translator' starting task execution: Translate the following text to Spanish: 'Please contact support@example.com for assistance.'...
2025-04-20 20:34:40,297 - tbh_secure_agents.agent - INFO - Agent 'PII-Aware Multilingual Translator' successfully executed task on attempt 1.
2025-04-20 20:34:40,297 - tbh_secure_agents.task - INFO - Task 'Translate the following text to Spanish: 'Please c...' finished execution successfully.
2025-04-20 20:34:40,297 - tbh_secure_agents.crew - INFO - Crew kickoff finished.
PII-Safe Translation Crew Finished.

==================== Task Result (General Translator) ====================
Profile: translator_general
Okay, I can do that. Here's the translation of "Please contact support@example.com for assistance." into Spanish:

**Por favor, contacte con support@example.com para obtener ayuda.**

======================================================================

==================== Task Result (PII-Safe Translator) ====================
Profile: translator_no_pii
Here's the Spanish translation, with PII masked:

"Por favor, contacte al departamento de soporte técnico para asistencia."

======================================================================

--- Example Script 7 Finished ---
WARNING: This example demonstrates PROFILE ASSIGNMENT CONCEPT ONLY.
WARNING: Actual PII masking based on profile requires implementation in Agent's _is_output_secure method.
