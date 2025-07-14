import React from "react";
import "../styles/Research.css"

function Research({ paper, onDelete }) {
    const formattedDate = new Date(paper.research_date).toLocaleDateString("en-UK")

    return (
        <div className="paper_container">
            <p className="paper_title">{paper.topic}</p>
            <p className="paper_content">{paper.research_papers}</p>
            <p className="paper_date">{formattedDate}</p>
            <button className="delete_button" onClick={() => onDelete(paper.id)}>
                Delete
            </button>
        </div>
    );
}

export default Research