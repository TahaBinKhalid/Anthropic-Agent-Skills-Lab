echo "[System-Tool] Initiating automated local test suite execution..."

python3 -m py_compile src/*.py 2>&1
if [ $? -eq 0 ]; then
    echo "✅ [Success] All Python codebase compilation checks passed safely."
else
    echo "❌ [Error] Syntax flaws or compilation blocks identified in codebase pipeline."
fi