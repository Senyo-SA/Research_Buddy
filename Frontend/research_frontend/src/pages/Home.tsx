import api from "../api"
import Research from "../components/Research"
import { useState, useEffect } from "react";
import "../styles/Home.css"

function Home() {
    const [research, setResearch] = useState([]);
    const [research_papers, setResearch_Papers] = useState("");
    const [topic, setTopic] = useState("");

    useEffect(() => {
        getResearch();
    }, []);

    const getResearch = () => {
        api
            .get("/api/research/")
            .then((response) => response.data)
            .then((data) => {
                setResearch(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    const deleteResearch = (id : any) => {
        api
            .delete(`/api/research/delete/${id}/`)
            .then((response) => {
                if (response.status === 204) alert("Research deleted!");
                else alert("Failed to delete note.");
                getResearch();
            })
            .catch((error) => alert(error));
            
    };

    const createResearch = (e : any) => {
        e.preventDefault();
        api
            .post("/api/research/", {topic})
            .then((response) => {
                if (response.status === 201) alert("Note created!");
                else alert("Failed to make note.");
                getResearch();
            })
            .catch((err) => alert(err));
    }; 

    return (
        <div >
            <div>
                <h2>Research Papers</h2>
                {research.map((paper : any) => (
                    <Research paper={paper} onDelete={deleteResearch} key={paper.id}/>
                ))}
            </div>
            <h2>Create Research</h2>
            <form onSubmit={createResearch}>
                <label htmlFor="topic">Topic:</label>
                <br />
                <input
                    type="text"
                    id="topic"
                    name="topic" 
                    required
                    onChange={(e) => setTopic(e.target.value)}
                    value={topic}
                />
                <label htmlFor="research_papers">Research_papers:</label>
                <br />
                <div>
                     {research_papers}        
               </div>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}

export default Home;