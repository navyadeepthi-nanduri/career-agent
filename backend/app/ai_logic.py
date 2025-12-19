from .schemas import StudentProfile, CareerRecommendation, StepItem, RecommendationResponse

def generate_recommendation(profile: StudentProfile) -> RecommendationResponse:
    # Very simple rule-based "AI" for now
    # Later, this will call a real LLM API.

    # 1. Infer a rough career path from interests/skills
    interests_text = " ".join(profile.interests).lower()
    skills_text = " ".join(profile.skills).lower()

    career_paths = []

    if "web" in interests_text or "frontend" in interests_text:
        career_paths.append("Full Stack Web Developer")
    if "data" in interests_text or "ml" in skills_text or "machine learning" in interests_text:
        career_paths.append("Data Scientist / ML Engineer")
    if "ai" in interests_text or "llm" in skills_text:
        career_paths.append("AI Engineer / LLM Engineer")
    if not career_paths:
        career_paths.append("Explore multiple fields (software dev, data, AI)")

    # 2. Very rough learning roadmap
    roadmap = [
        StepItem(
            title="Strengthen programming fundamentals",
            description="Practice Python or Java daily for 30–60 minutes using basic problems."
        ),
        StepItem(
            title="Build 1–2 small projects",
            description="Choose a simple project in your chosen area, like a to-do app or data analysis notebook."
        ),
        StepItem(
            title="Create a GitHub portfolio",
            description="Push your projects to GitHub and write clear README files."
        ),
    ]

    # 3. Next concrete actions
    next_actions = [
        StepItem(
            title="Write your current skills list",
            description="List all languages, tools, and subjects you know, even at basic level."
        ),
        StepItem(
            title="Block 1 hour daily",
            description="Fix a daily time slot only for focused learning with no distractions."
        ),
        StepItem(
            title="Pick 1 main target role",
            description=f"From suggested paths {career_paths}, choose 1 to focus on for the next 3 months."
        ),
    ]

    reasoning = (
        "The suggested career paths are based on your stated skills and interests. "
        "The roadmap starts from fundamentals, then projects, then portfolio, which is a proven sequence for beginners. "
        "Next actions are kept very small so that you can start immediately."
    )

    recommendation = CareerRecommendation(
        career_paths=career_paths,
        learning_roadmap=roadmap,
        next_actions=next_actions,
        reasoning=reasoning,
    )

    return RecommendationResponse(recommendation=recommendation)
