import React from "react";
import '../App.css';

export const SelectEntity = props => {
    return (
        <div
            onClick={props.onClick}
            className="selectEntity-container">
            <input
                type="checkbox"
                checked={props.selectedEntities}
                onChange={() => console.log("changed")} />
            <span className="selectEntity"> {props.entity}</span>
        </div>
    );
};