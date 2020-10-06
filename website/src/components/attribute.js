import React from "react";
import '../App.css';
import { Input } from 'reactstrap'

export const Attribute = ({
    entity,
    attribute,
    onChange
}) => {
    const attributeName = entity + '.' + attribute
    return (
        <div>
            <span>{attributeName}: </span>
            <Input name={attributeName} onChange={onChange} />
        </div >
    )
}