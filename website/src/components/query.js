import React from "react";
import { Alert } from "reactstrap";
import '../App.css';

export const Query = (props) => {
    return (
        <div>
            <Alert color="secondary">
                < h1 className="header" > SQL Query: &nbsp;</h1 >
                Option to modify/review SQL query before submitting form.
            </Alert>
            <textarea
                class="form-control"
                id="exampleFormControlTextarea1"
                rows="3"
                value={props.query}
                onChange={props.changed}></textarea>
        </div>
    )
}