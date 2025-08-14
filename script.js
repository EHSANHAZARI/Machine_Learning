async function getRecommendation() {
  const movieTitle = document.getElementById("movie-input").value.trim();
  if (!movieTitle) {
    alert("Please enter a movie title");
    return;
  }

  try {
    const response = await fetch(`/api/recommend?title=${encodeURIComponent(movieTitle)}`);

    if (!response.ok) {
      // Try to read error message from server, else use a fallback
      let serverMsg = "Movie not found";
      try {
        const errJson = await response.json();
        serverMsg = errJson.message || serverMsg;
      } catch (_) {}
      throw new Error(serverMsg);
    }

    // Success path
    const data = await response.json();
    // If API returns { results: [...] }, use data.results; if it returns [...], use data
    const recommendations = Array.isArray(data) ? data : (data.results || []);

    const resultList = document.getElementById("results");
    resultList.innerHTML = "";

    recommendations.forEach(movie => {
      const li = document.createElement("li");
      li.textContent = movie;
      resultList.appendChild(li);
    });

  } catch (error) {
    console.error(error);
    alert("Error: " + (error.message || error));
  }
}
