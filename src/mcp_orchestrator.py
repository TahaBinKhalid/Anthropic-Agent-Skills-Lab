import os
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv

# Load local environment keys
load_dotenv()

class GeminiAgentOrchestrator:
    def __init__(self):
        # Read your AQ. key from the environment variable file
        self.api_key = os.getenv("GEMINI_APIKEY")
        
        # Hardcoded fallback safety if .env file can't be found across directories on Windows
        if not self.api_key:
            self.api_key = "GEMINI_API_KEY"
            
        self.sub_agent_skill_path = ".anthropic/skills/code-reviewer/SKILL.md"

    def _load_isolated_skill(self) -> str:
        """Reads the modular skill setup to append as system instructions on-demand."""
        with open(self.sub_agent_skill_path, "r", encoding="utf-8") as file:
            return file.read()

    def delegate_to_sub_agent(self, target_code: str) -> str:
        """Spins up a routine by hitting the Gemini REST endpoint directly, bypassing the broken SDK."""
        print("[Orchestrator] Dynamic trigger match found. Injecting SKILL.md rules...")
        skill_instructions = self._load_isolated_skill()
        
        print("[Orchestrator] Invoking Gemini Sub-Agent via Direct REST Pipeline...")
        
        # Target the raw Google v1beta endpoint directly
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        
        # Build the exact json payload payload mapping system instructions and configurations
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Please run a strict code audit on the following file payload:\n\n```python\n{target_code}\n```"
                }]
            }],
            "systemInstruction": {
                "parts": [{
                    "text": skill_instructions
                }]
            },
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 1500
            }
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, 
            data=data, 
            headers={"Content-Type": "application/json"}
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                # Parse out the returned text content cleanly
                return result["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            error_msg = e.read().decode("utf-8")
            return f"API Connection Error: {e.code} - {error_msg}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    flawed_code_sample = """
import os
import mysql.connector

def connect_database():
    db = mysql.connector.connect(host="localhost", user="root", password="SuperSecretPassword123!", database="app_db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + input("Enter user: ") + "'")
    return cursor.fetchall()
    """
    
    orchestrator = GeminiAgentOrchestrator()
    audit_report = orchestrator.delegate_to_sub_agent(flawed_code_sample)
    print("\n--- GEMINI SUB-AGENT AUDIT REPORT ---")
    print(audit_report)