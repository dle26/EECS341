import React from "react";
import '../App.css';
import { FormGroup } from 'react-bootstrap';

export const EnterEmail = (props) => {
  return (
    <FormGroup className="email" class="form-group">
      <label>Email address</label>
      <input class="form-control" placeholder="Enter email" value={props.value} onChange={props.changed}></input>
      <small id="emailHelp" class="form-text text-muted">We'll send the query results to your email.</small>
    </FormGroup>
  )
}