import React, { useEffect }  from "react";
import './index.css';
import { useState } from 'react';

function HomePage(){
    const[state,setState] = useState("Chennai");

    useEffect(()=>{

    },[])
    return(
        <div className="homepage-grid-split">
            <div className="left">
                <h2>Current Temperature</h2>
                <p>25°C</p>
            </div>
            <div className="right">
                <h2>Weather Information</h2>
                <p>Temperature: 25°C</p>
                <p>Condition: Sunny</p>
            </div>
        </div>
    );
}
export default HomePage;