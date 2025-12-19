const form = document.getElementById("profile-form");
const resultDiv = document.getElementById("result");

// Change this if your backend runs on another host/port
const BACKEND_URL = "http://127.0.0.1:8000";

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  resultDiv.innerHTML = "Thinking...";

  const name = document.getElementById("name").value;
  const ageValue = document.getElementById("age").value;
  const age = ageValue ? parseInt(ageValue) : null;
  const education = document.getElementById("education").value;
  const skills = document
    .getElementById("skills")
    .value.split(",")
    .map((s) => s.trim())
    .filter((s) => s.length > 0);
  const interests = document
    .getElementById("interests")
    .value.split(",")
    .map((s) => s.trim())
    .filter((s) => s.length > 0);
  const goals = document.getElementById("goals").value;
  const countriesRaw = document.getElementById("countries").value;
  const preferredCountries = countriesRaw
    ? countriesRaw.split(",").map((c) => c.trim()).filter((c) => c.length > 0)
    : null;

  const payload = {
    profile: {
      name,
      age,
      current_education: education,
      skills,
      interests,
      goals,
      preferred_countries: preferredCountries
    }
  };

  try {
    const response = await fetch(`${BACKEND_URL}/recommend`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error("Server error: " + response.status);
    }

    const data = await response.json();
    const rec = data.recommendation;

    resultDiv.innerHTML = `
      <h2>Suggested Career Paths</h2>
      <ul>${rec.career_paths.map((p) => `<li>${p}</li>`).join("")}</ul>

      <h2>Learning Roadmap</h2>
      <ol>
        ${rec.learning_roadmap
          .map((step) => `<li><strong>${step.title}:</strong> ${step.description}</li>`)
          .join("")}
      </ol>

      <h2>Next Actions</h2>
      <ol>
        ${rec.next_actions
          .map((step) => `<li><strong>${step.title}:</strong> ${step.description}</li>`)
          .join("")}
      </ol>

      <h2>Reasoning</h2>
      <p>${rec.reasoning}</p>
    `;
  } catch (err) {
    console.error(err);
    resultDiv.innerHTML = "Something went wrong. Check the browser console and backend logs.";
  }
});

