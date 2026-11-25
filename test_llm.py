from backend.llm_analyzer import analyze_strengths

sample_resume = """
Python, SQL, HTML, Azure internship, Communication skills, mini projects, BSc Computer Science 2024.
"""

print("🔍 Testing model...")
print(analyze_strengths(sample_resume))
