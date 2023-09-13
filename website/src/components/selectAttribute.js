import React from "react";
import '../App.css';
import Select from 'react-select';
import { userFriendlyNames } from "../App";

export const SelectAttribute = ({
    onChange,
    attributeOptions,
    selectedAttributes
}) => {
    //console.log(selectedAttributes);
    const options = attributeOptions.map(attr => ({ value: attr, label: userFriendlyNames[attr] }))
    return (
        <Select
            onChange={onChange}
            value={selectedAttributes}
            options={options}
            isMulti
            isSearchable
            isClearable={false}
            placeholder='Select attributes...'
        />
    )
}