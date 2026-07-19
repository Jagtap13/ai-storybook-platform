import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api/axios";

function StoryReader() {
  const { id } = useParams();
  const [story, setStory] = useState(null);
  const [currentPage, setCurrentPage] = useState(0);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchStory = async () => {
      try {
        const response = await api.get(`/stories/${id}/`);
        setStory(response.data);
      } catch (err) {
        setError("Could not load this story!");
      }
    };
    fetchStory();
  }, [id]);
  if (error) {
    return <p className="p-8 text-red-500">{error}</p>;

  }
  if (!story) {
  return <p className="p-8">Loading...</p>;
}
  const page = story.pages[currentPage];
  const isFirstPage = currentPage == 0;
  const isLastPage = currentPage === story.pages.length - 1;
  return (
    <>
      <div className="min-h-screen bg-slate-100 p-8 flex flex-col items-center">
        <Link to="/dashboard" className="self-start text-blue-600 mb-4">
          ← Back to Dashboard
        </Link>

        <div className="bg-white rounded-lg shadow-md p-8 max-w-xl w-full">
          <h1 className="text-2xl font-bold mb-6">{story.title}</h1>

          <p className="text-lg leading-relaxed mb-8">{page.text}</p>

          <div className="flex justify-between items-center">
            <button
              onClick={() => setCurrentPage((p) => p - 1)}
              disabled={isFirstPage}
              className="px-4 py-2 bg-slate-200 rounded disabled:opacity-40"
            >
              Previous
            </button>

            <span className="text-sm text-gray-500">
              Page {currentPage + 1} of {story.pages.length}
            </span>

            <button
              onClick={() => setCurrentPage((p) => p + 1)}
              disabled={isLastPage}
              className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-40"
            >
              Next
            </button>
          </div>
        </div>
      </div>
    </>
  );
}

export default StoryReader
