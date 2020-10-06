import React from "react";
import '../App.css';
import { userFriendlyNames } from '../App'

export const SelectEntity = props => {
    return (
        <div onClick={props.onClick}>
            <button type="button" class="btn btn-light">
                <input
                    type="checkbox"
                    checked={props.selectedEntities}
                    onChange={() => console.log("changed")} />
                <span className="selectEntity"> {userFriendlyNames[props.entity]}</span>
            </button>
        </div>
    );
};