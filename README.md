Modular Agentic Workflows System (Gemini SDK & Multi-Agent Architecture)
An enterprise-grade orchestration design pattern tracking the optimization of complex runtime instructions into deterministic, token-efficient, and decoupled AI Agent Skills.

Traditional agent architectures suffer from compounding context window costs, high latency, and degradation of instructional adherence ("lost in the middle" phenomena) due to monolithic system prompting. This repository implements a production-ready, lightweight orchestration pattern that dynamically resolves intent triggers, isolates context windows, and pairs complex modular logic with low-latency execution loops via raw REST interfaces leveraging the Gemini 2.5 infrastructure.

🏗️ Architectural Overview
Instead of forcing exhaustive development checklists and multi-step evaluation rules into every basic generation request, the parent orchestrator acts as a highly optimized, state-free routing layer. Sub-agent definitions, specialized tool configurations, and granular target behavioral constraints remain entirely decoupled until their respective triggers are explicitly evaluated.

Plaintext
[User Task Request] ➔ [Parent Orchestrator Layer]
                             │
                             └── ➔ [Context Match Trigger] 
                                      └── Load '.anthropic/skills/code-reviewer/'
                                               ├── Mounts SKILL.md (System Routing Directives)
                                               └── Executes Isolated Gemini Sub-Agent Env
Key Design Pillars
Runtime Isolation: Sub-agents execute within ephemeral parameter contexts. System directives loaded from external .md containers are cleanly injected on-demand, preventing cross-contamination of multi-agent state histories.

Token Efficiency: Minimizes idle baseline token consumption by holding specialized evaluation criteria out of band until matching intent conditions are matched.

Native REST Resiliency: Skips brittle local client SDK verification filters, making the orchestration system compatible with modern token-shifting enterprise credential infrastructures (AQ. prefix keys) directly over secure HTTP/1.1 pipelines.

🛠️ Repository File Structure
Plaintext
├── .anthropic/
│   └── skills/
│       └── code-reviewer/
│           └── SKILL.md          # Granular instruction sets, anchors, and metric scoring rules
├── src/
│   └── mcp_orchestrator.py       # Core routing engine, REST handler, and payload parser
├── .env                          # Localized secret key configuration (Git-ignored)
├── .gitignore                    # Prevents upstream exposure of deployment variables
└── README.md                     # Architecture specification and execution runbook
⚙️ Core Components
1. The Skill Specification Layer (SKILL.md)
The core capabilities of the sub-agent are codified inside standalone Markdown manifest files. This decouples the agent's logic from the orchestrator's application code, making updates to skills manageable via declarative file modifications.

Triggers Matrix: High-level arrays parsed by the parent orchestrator to map real-time processing demands to specific skills.

Execution Protocols: Highly granular scanning checklists targeting exact code behaviors (e.g., input sanitation checking, cryptographic primitives validation, and scope verification).

Deterministic Contract Formatting: Guarantees that the decoupled model strictly generates structured responses adhering to custom formatting anchors, enabling reliable down-stream string splitting or JSON parsing.

2. The Orchestration Router (mcp_orchestrator.py)
Built cleanly without bulky overhead frameworks, this engine processes targeted payloads through a streamlined lifecycle:

Environment Realignment: Boots up and maps underlying runtime environment variables via python-dotenv.

Context Resolution: Parses the calling criteria, opens target instruction documents using explicit utf-8 standard file streams to handle rich formatting on Windows configurations, and buffers rules into memory.

Bypassing Client Filtering: Assembles raw payloads mapping text inputs, configurations, and system-level prompt overrides into a cohesive query string to execute raw HTTP POST requests securely against Google API endpoints.

Python
# System Instruction Payload Mapping Hook
payload = {
    "contents": [{"parts": [{"text": target_payload_string}]}],
    "systemInstruction": {"parts": [{"text": skill_instructions_buffer}]},
    "generationConfig": {
        "temperature": 0.2,
        "maxOutputTokens": 1500
    }
}
🚀 Installation & Local Verification
Prerequisites
Python 3.11 or higher installed on your local workstation.

An active Google AI Studio developer credential token (AQ. or AIza string patterns).

1. Clone & Workspace Setup
PowerShell
git clone https://github.com/YOUR_GITHUB_USERNAME/Anthropic-Agent-Skills-Lab.git
cd Anthropic-Agent-Skills-Lab
2. Install Dependencies
Initialize your workspace variables and load the required underlying environment management libraries:

PowerShell
pip install python-dotenv
3. Environment Environment Variable Injection
Create an environment verification file named .env in the root workspace folder and configure your authorization token exactly as shown:

Plaintext
GEMINI_API_KEY="AQ.YOUR_GENERIC_AI_STUDIO_TOKEN_HERE"
4. Running the Audit Loop
Trigger the parent script execution block to process the embedded vulnerable test payload through the orchestrator's decoupled sub-agent routine:

PowerShell
python src/mcp_orchestrator.py
🔒 Security & Safe Commits
This workspace includes built-in protective parameters designed to meet modern security compliance controls.

Git Exclusion Mapping: The repository contains an active .gitignore record specifically preventing localized .env configuration files from leaking to public cloud tracking branches.

Pre-Commit Secret Auditing: The project architecture is pre-configured to comply with enterprise-level repository rules like GitHub Push Protection. No hardcoded programmatic strings are evaluated inside any operational runtime constructor (__init__), maintaining a clean boundary between program logic and application configuration.