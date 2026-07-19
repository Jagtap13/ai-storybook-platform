import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import api from "../api/axios";

function Dashboard() {
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("easy");
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState("");
  const [error, setError] = useState("");

  const fetchStorires = async () => {
    try {
      const response = await api.get("/stories/");
      setStories(response.data);
    } catch (err) {
      setError("Could not load stories!!");
    }
  };
  useEffect(() => {
    fetchStorires();
  }, []);

  const handleGenerate = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      await api.post("/stories/generate/", {
        topic,
        difficulty,
      });
      setTopic("");
      setError("");
      fetchStories();
    } catch (err) {
      setError("Failed to generate a story!!!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="min-h-screen bg-slate-100 p-8">
        <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
        <form
          action=""
          onSubmit={handleGenerate}
          className="bg-white p-6 rounded-lg shadow-md mb-8 max-w-md"
        >
          <h2 className="text-xl font-semibold mb-4">Generate a new story</h2>
          {error && <p className="text-red-500 text-sm mb-4">{error}</p>}

          <input
            type="text"
            placeholder="Topic (e.g. space, animals )"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            className="w-full border rounded px-3 py-2 mb-4"
          />

          <select
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            className="w-full border rounded px-3 py-2 mb-4"
          >
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? "Generating..." : "Generate Story"}
          </button>
        </form>
        <h2 className="text-xl font-semibold mb-4">My Stories</h2>
        <div className="grid gap-4 max-w-md">
          {stories.map((story) => (
            <Link
              key={story.id}
              to={`/story/${story.id}`}
              className="bg-white p-4 rounded shadow hover:shadow-md transition"
            >
              <h3 className="font-bold">{story.title}</h3>
              <p className="text-sm text-gray-500">
                {story.topic} · {story.difficulty}
              </p>
            </Link>
          ))}
        </div>
      </div>
    </>
  );
}
export default Dashboard;
