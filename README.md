# Modular Agentic Workflows System (Gemini SDK & Multi-Agent Architecture)

An enterprise-grade design pattern tracking the optimization of complex system prompts into deterministic, token-efficient runtime **AI Agent Skills**. Originally designed around open-standard configurations, this repository showcases a decoupled, multi-agent orchestration architecture using the production-ready Google GenAI SDK.

## 🏗️ Architectural Overview
Instead of forcing massive instructions into every basic LLM generation request, this layout isolates heavy workflows until matching intent triggers are encountered.

```text
[User Task Request] ➔ [Parent Orchestrator Layer]
                             │
                             └── ➔ [Context Match Trigger] 
                                        └── Load '.anthropic/skills/code-reviewer/'
                                                 ├── Mounts SKILL.md (System Routing Directives)
                                                 └── Executes Isolated Gemini Sub-Agent Env