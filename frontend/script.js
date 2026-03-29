async function uploadData() {

    let jobTitle = document.getElementById("jobTitle").value;
    let jobDesc = document.getElementById("jobDesc").value;

    let fullJob = jobTitle + " " + jobDesc;

    let files = document.getElementById("resumeFiles").files;

    let formData = new FormData();
    formData.append("job_description", fullJob); // ✅ FIXED

    for (let i = 0; i < files.length; i++) {
        formData.append("resumes", files[i]);
    }

    let response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    // 🔥 MAIN SCORE
    let score = data[0].score;
    document.getElementById("mainScore").innerText = score;

    // 🎯 MAIN CIRCLE ANIMATION
    let circle = document.querySelector(".progress");
    let radius = 65;
    let circumference = 2 * Math.PI * radius;

    let offset = circumference - (score / 100) * circumference;
    circle.style.strokeDashoffset = offset;

    // 🔥 RESULTS
    let resultDiv = document.getElementById("results");
    resultDiv.innerHTML = "<h2>Results</h2>";

    data.forEach((res, index) => {

        resultDiv.innerHTML += `
        <div style="background:white; padding:20px; margin:15px 0; border-radius:12px;">

            <h3>
                ${index + 1}. ${res.id}
                ${index === 0 ? " ⭐ Top Candidate" : ""}
            </h3>

            <p><b>Overall Score:</b> ${res.score}</p>

            <div class="breakdown">
                ${createCircle("skills", res.skills, index)}
                ${createCircle("experience", res.experience, index)}
                ${createCircle("keyword", res.keyword, index)}
                ${createCircle("projects", res.projects, index)}
            </div>

            <p><b>Missing Keywords:</b></p>
            <ul>
                ${res.missing.map(m => `<li>${m}</li>`).join("")}
            </ul>

            <p><b>Recommendations:</b></p>
            <ul>
                ${res.recommendations.map(r => `<li>${r}</li>`).join("")}
            </ul>

        </div>
        `;
    });

    // 🔥 ANIMATE MINI CIRCLES
    setTimeout(() => {
        data.forEach((res, index) => {
            animateCircle("skills" + index, res.skills);
            animateCircle("experience" + index, res.experience);
            animateCircle("keyword" + index, res.keyword);
            animateCircle("projects" + index, res.projects);
        });
    }, 100);
}